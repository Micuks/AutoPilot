#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
import pySimOneIO
import math
import heapq
import time
from SimOneIOStruct import *

case_info = SimOne_Data_CaseInfo()
SimOne_Data_Gps_Test = SimOne_Data_Gps()
SimOne_Data_MainVehicle_Info_Test = SimOne_Data_MainVehicle_Info()
SimOne_Data_MainVehicle_Status_Test = SimOne_Data_MainVehicle_Status()
control = SimOne_Data_Control()
wayPoints = SimOne_Data_WayPoints()


M_PI = 3.14159265358979323846
# Global
PosX = 0;
PosY = 0;
PosZ = 0;

def gpsCB(mainVehicleId, data):
	global PosX, PosY, PosZ
	PosX = data[0].posX
	PosY = data[0].posY
	PosZ = data[0].posZ


def SampleGetNearMostLane(pos):
	SoBridgeLogOutput(0, "SampleGetNearMostLane:")

	info = pySimOneIO.getNearMostLane(pos)
	if info.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	SoBridgeLogOutput(0, "lane id:%s" % info.laneId.GetString())

	return info.laneId


def apiAllStart(isJoinTimeLoop):
    SoAPIStartSimOneNode(0, 0)
    SoAPISimOneNodeReady()
    if SoAPIGetCaseInfo(case_info):
        SoBridgeLogOutput(0, "GetCaseInfo caseName: %s" % case_info.caseName)
        SoBridgeLogOutput(0, "GetCaseInfo caseId: %s" % case_info.caseId)
        SoBridgeLogOutput(0, "GetCaseInfo taskId: %s" % case_info.taskId)
        SoBridgeLogOutput(0, "GetCaseInfo sessionId: %s" % case_info.sessionId)
        SoBridgeLogOutput(0, "SoAPIGetCaseRunStatus: %s" % SoAPIGetCaseRunStatus())

    if SoAPIGetMainVehicleList(SimOne_Data_MainVehicle_Info_Test):
        SoBridgeLogOutput(0, "MainVehicle size: %s" % SimOne_Data_MainVehicle_Info_Test.size)

    while (1):
        SoAPISubMainVehicle_result = SoAPISubMainVehicle(0, isJoinTimeLoop)
        SoBridgeLogOutput(0, "SoAPISubMainVehicle_result:%s" % SoAPISubMainVehicle_result)

        if SoAPISubMainVehicle_result:
            break

    if SoAPIGetMainVehicleStatus(SimOne_Data_MainVehicle_Status_Test):
        SoBridgeLogOutput(0, "mainVehicleId:%s" % SimOne_Data_MainVehicle_Status_Test.mainVehicleId)
        SoBridgeLogOutput(0, "mainVehicleStatus:%s" % SimOne_Data_MainVehicle_Status_Test.mainVehicleStatus)

    ret = pySimOneIO.loadHDMap(100)
    SoBridgeLogOutput(0, "Load xodr success:%s" % ret)


def GetGenerateRoutePath():
    routePath = list()
    routeInfo = pySimOneIO.getPredefinedRoute()
    if routeInfo.exists == False:
        SoBridgeLogOutput(0, "Not exists!")
        return
    SoBridgeLogOutput(0, "route point count:%s"% routeInfo.route.Size())

    for i in range(routeInfo.route.Size()):
        pt = routeInfo.route.GetElement(i)
        routePath.append({"x": pt.x, "y": pt.y, "z": pt.z})
    return routePath


def calculateSteering(targetPath, GpsData, lastTargetPathIndex):
    pts = list()
    for i in targetPath:
        tmp_value = pow(GpsData.posX-i.get('x'), 2) + pow(GpsData.posY-i.get('y'), 2)
        pts.append(tmp_value)
    minIndex = list(map(pts.index, heapq.nsmallest(1, pts)))[0]

    while(1):
        if minIndex >= lastTargetPathIndex:
            lastTargetPathIndex = minIndex
            break
        else:
            if len(targetPath) > 0:
                del targetPath[minIndex]
                minIndex = list(map(pts.index, heapq.nsmallest(1, pts)))[0]

    forwardIndex = 0
    MinProgDist = 3
    ProgTime = 0.8
    MainVehicleSpeed = math.sqrt(pow(GpsData.velX, 2) + pow(GpsData.velY, 2) + pow(GpsData.velZ, 2))

    if MainVehicleSpeed * ProgTime > MinProgDist:
        progDist = MainVehicleSpeed * ProgTime
    else:
        progDist = MinProgDist

    for index in range(minIndex, len(targetPath)):
        forwardIndex = index
        distance = math.sqrt(pow(targetPath[index].get('x') - GpsData.posX, 2) + pow(targetPath[index].get('y') - GpsData.posY, 2))
        if distance >= progDist:
            break

    psi = GpsData.oriZ
    Alfa = math.atan2(targetPath[forwardIndex].get('y') - GpsData.posY, targetPath[forwardIndex].get('x') - GpsData.posX) - psi
    ld = math.sqrt(pow(targetPath[forwardIndex].get('y') - GpsData.posY, 2) + pow(targetPath[forwardIndex].get('x') - GpsData.posX, 2))
    steering = -(math.atan2(2 * (1.3 + 1.55) * math.sin(Alfa), ld) * 36 / (7 * M_PI))
    return steering, lastTargetPathIndex


def setDriver(throttle, brake, steering):
    control.throttle = throttle
    control.brake = brake
    control.steering = steering
    control.isManualGear = False
    control.gear = EGearMode.EGearManualMode_1
    SoApiSetDrive(0, control)


def getTargetPath():
    SoApiSetGpsUpdateCB(gpsCB)
    pos = pySimOneIO.pySimPoint3D(PosX, PosY, PosZ)
    if SoGetWayPoints(wayPoints):
        SoBridgeLogOutput(0, "wayPoints.wayPointsSize:%s" % wayPoints.wayPointsSize)

        if wayPoints.wayPointsSize >= 2:
            targetPath = GetGenerateRoutePath()
        else:
            targetPath = list()
            laneId = SampleGetNearMostLane(pos)
            sampleInfo = pySimOneIO.getLaneSample(laneId)
            centerLine = sampleInfo.laneInfo.centerLine
            SoBridgeLogOutput(0, "centerLine knot size:%s" % centerLine.Size())

            for i in range(centerLine.Size()):
                element = centerLine.GetElement(i)
                targetPath.append({"x": element.x, "y": element.y, "z": element.z})
        return targetPath


if __name__ == '__main__':
    apiAllStart(False)
    SoSetDriverName(0, "Predefined")
    lastTargetPathIndex = -1
    targetPath = getTargetPath()

    while(1):
        if SoAPIGetCaseRunStatus() == 1:
            SoBridgeLogOutput(0, "case stop")
            break
        SoGetGps(0, SimOne_Data_Gps_Test)

        steering, lastTargetPathIndex = calculateSteering(targetPath, SimOne_Data_Gps_Test, lastTargetPathIndex)
        SoBridgeLogOutput(0, "steering:%s" % steering)

        if math.sqrt(pow(SimOne_Data_Gps_Test.velX, 2) + pow(SimOne_Data_Gps_Test.velY, 2) * 3.6) > 40:
            setDriver(0, 1, steering)
        else:
            setDriver(0.2, 0, steering)



