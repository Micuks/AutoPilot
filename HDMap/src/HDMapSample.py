import os
import pySimOneIO
import time

from SimOneIOStruct import *

M_PI = 3.14159265358979323846

# Global
PosX = 0;
PosY = 0;
PosZ = 0;


def SampleGetNearMostLane(pos):
	SoBridgeLogOutput(0, "SampleGetNearMostLane:")
	info = pySimOneIO.getNearMostLane(pos)
	if info.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	SoBridgeLogOutput(0, "lane id:%s" % info.laneId.GetString())
	return info.laneId


def SampleGetNearLanes(pos, radius):
	SoBridgeLogOutput(0, "SampleGetNearLanes:")
	nearLanesInfo = pySimOneIO.getNearLanes(pos, radius)
	if nearLanesInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	lanesInfo = nearLanesInfo.laneIdList
	SoBridgeLogOutput(0, "lanesInfo size:%s" % lanesInfo.Size())
	SoBridgeLogOutput(0, "lanesInfo id list:")
	for i in range(lanesInfo.Size()):
		element = lanesInfo.GetElement(i)
		SoBridgeLogOutput(0, "%s" % element.GetString())
		SoBridgeLogOutput(0, ",")


def SampleGetNearLanesWithAngle(pos, radius, headingAngle, shiftAngle):
	SoBridgeLogOutput(0, "SampleGetNearLanesWithAngle:")
	nearLanesInfo = pySimOneIO.getNearLanesWithAngle(pos, radius, headingAngle, shiftAngle)
	if nearLanesInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	lanesInfo = nearLanesInfo.laneIdList
	SoBridgeLogOutput(0, "lanesInfo size:%s"%lanesInfo.Size())
	SoBridgeLogOutput(0, "lanesInfo id list:")
	for i in range(lanesInfo.Size()):
		element = lanesInfo.GetElement(i)
		SoBridgeLogOutput(0, "%s" % element.GetString())
		SoBridgeLogOutput(0, ",")


def SampleGetDistanceToLaneBoundary(pos):
	SoBridgeLogOutput(0, "SampleGetDistanceToLaneBoundary:")
	distanceToLaneBoundaryInfo = pySimOneIO.getDistanceToLaneBoundary(pos);
	if distanceToLaneBoundaryInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return

	SoBridgeLogOutput(0, "laneId:%s" % distanceToLaneBoundaryInfo.laneId.GetString())
	SoBridgeLogOutput(0, "distToLeft:%s" % distanceToLaneBoundaryInfo.distToLeft)
	SoBridgeLogOutput(0, "distToRight:%s" % distanceToLaneBoundaryInfo.distToRight)
	SoBridgeLogOutput(0, "distToLeft2D:%s" % distanceToLaneBoundaryInfo.distToLeft2D)
	SoBridgeLogOutput(0, "distToRight2D:%s" % distanceToLaneBoundaryInfo.distToRight2D)


def SampleGetLaneSample(laneId):
	SoBridgeLogOutput(0, "SampleGetLaneSample:")
	sampleInfo = pySimOneIO.getLaneSample(laneId)
	if sampleInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	leftBoundary = sampleInfo.laneInfo.leftBoundary

	SoBridgeLogOutput(0, "leftBoundary knot size:%s"%leftBoundary.Size())
	SoBridgeLogOutput(0, "leftBoundary knot list:")
	for i in range(leftBoundary.Size()):
		element = leftBoundary.GetElement(i)
		print("(", element.x, ",", element.y, ",", element.z, "),")

	rightBoundary = sampleInfo.laneInfo.rightBoundary

	SoBridgeLogOutput(0, "rightBoundary knot size:%s"%rightBoundary.Size())
	SoBridgeLogOutput(0, "rightBoundary knot list:")

	for i in range(rightBoundary.Size()):
		element = rightBoundary.GetElement(i)
		print("(", element.x, ",", element.y, ",", element.z, "),")

	centerLine = sampleInfo.laneInfo.centerLine

	SoBridgeLogOutput(0, "centerLine knot size:%s"%centerLine.Size())
	SoBridgeLogOutput(0, "centerLine knot list:")

	for i in range(centerLine.Size()):
		element = centerLine.GetElement(i)
		SoBridgeLogOutput(0, "(%s,%s,%s)" % element.x,element.y,element.z)
		SoBridgeLogOutput(0, "centerLine knot list:")


def SampleGetLaneLink(laneId):
	SoBridgeLogOutput(0, "SampleGetLaneLink:")
	laneLinkInfo = pySimOneIO.getLaneLink(laneId)
	if laneLinkInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	laneLink = laneLinkInfo.laneLink
	predecessorIds = laneLink.predecessorLaneIds

	SoBridgeLogOutput(0, "predecessorLaneIds size:%ds"%predecessorIds.Size())
	if predecessorIds.Size() > 0:
		SoBridgeLogOutput(0, "predecessorLaneIds:")
	for i in range(predecessorIds.Size()):
		element = predecessorIds.GetElement(i)
		print(element.GetString())
	successorIds = laneLink.successorLaneIds

	SoBridgeLogOutput(0, "successorLaneIds size:%s"%successorIds.Size())
	if successorIds.Size() > 0:
		SoBridgeLogOutput(0, "successorLaneIds:")
	for i in range(successorIds.Size()):
		element = successorIds.GetElement(i)
		SoBridgeLogOutput(0, "%s"%element.GetString())
	SoBridgeLogOutput(0, "leftNeighborLaneId:%s"%laneLink.leftNeighborLaneId.GetString())
	SoBridgeLogOutput(0, "rightNeighborLaneId:%s" % laneLink.rightNeighborLaneId.GetString())


def SampleGetLaneType(laneId):
	SoBridgeLogOutput(0, "SampleGetLaneType:")
	laneType = pySimOneIO.getLaneType(laneId)
	if laneType.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	SoBridgeLogOutput(0, "lane type:%s"%laneType.laneType)


def SampleGetLaneWidth(laneId, pos):
	SoBridgeLogOutput(0, "SampleGetLaneWidth:")
	laneWidthInfo = pySimOneIO.getLaneWidth(laneId, pos)
	if laneWidthInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	SoBridgeLogOutput(0, "lane width:%s"%laneType.width)


def SampleGetLaneST(laneId, pos):
	SoBridgeLogOutput(0, "SampleGetLaneST:")
	stInfo = pySimOneIO.getLaneST(laneId, pos)
	if stInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	SoBridgeLogOutput(0, "[%s,%s] relative to this lane:"%(stInfo.s,stInfo.t))


def SampleGetRoadST(laneId, pos):
	SoBridgeLogOutput(0, "SampleGetRoadST:")
	stzInfo = pySimOneIO.getRoadST(laneId, pos)
	if stzInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	SoBridgeLogOutput(0, "[%s,%s] relative to this road:"%(stInfo.s,stInfo.t))
	SoBridgeLogOutput(0, "height of input point:%s" %stzInfo.z)


def SampleGetInertialFromLaneST(laneId, s, t):
	SoBridgeLogOutput(0, "SampleGetInertialFromLaneST:")
	inertialFromLaneSTInfo = pySimOneIO.getInertialFromLaneST(laneId, s, t)
	if inertialFromLaneSTInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return

	SoBridgeLogOutput(0, "inertial vector: (%s,%s,%s)"%(inertialFromLaneSTInfo.inertial.x,inertialFromLaneSTInfo.inertial.y,inertialFromLaneSTInfo.inertial.z))
	SoBridgeLogOutput(0, "dir vector: (%s,%s,%s)"%(inertialFromLaneSTInfo.dir.x,inertialFromLaneSTInfo.dir.y,inertialFromLaneSTInfo.dir.z))


def SampleContainsLane(laneId):
	SoBridgeLogOutput(0, "SampleContainsLane:")
	ret = pySimOneIO.containsLane(laneId)
	SoBridgeLogOutput(0, "return state:%s"%ret)


def SampleGetParkingSpaceList():
	SoBridgeLogOutput(0, "SampleGetParkingSpaceList:")
	parkingSpaceList = pySimOneIO.getParkingSpaceList()

	SoBridgeLogOutput(0, "parkingSpace count:%d"%parkingSpaceList.Size())
	for i in range(parkingSpaceList.Size()):
		parkingSpace = parkingSpaceList.GetElement(i)
		front = parkingSpace.front
		knots = parkingSpace.boundaryKnots
		knot0 = knots.GetElement(0)

		SoBridgeLogOutput(0, "parkingSpace count:%s" % parkingSpaceList.Size())
		SoBridgeLogOutput(0,"parkingSpace id:%s"%parkingSpace.id)
		SoBridgeLogOutput(0,"roadMark at which side:%s"%front.side.GetString())
		SoBridgeLogOutput(0,"roadMark type:%s"%front.type)
		SoBridgeLogOutput(0,"roadMark color:%s"%front.color)
		SoBridgeLogOutput(0,"roadMark width:%s"%front.width)
		SoBridgeLogOutput(0,"boundaryKnots count:%s"%knots.Size())
		SoBridgeLogOutput(0,"knot0 point: (%s,%s,%s)"%(knot0.x, knot0.y, knot0.z))


def SampleGetPredefinedRoute():
	SoBridgeLogOutput(0, "SampleGetPredefinedRoute:")
	routeInfo = pySimOneIO.getPredefinedRoute()
	if routeInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return

	SoBridgeLogOutput(0, "route point count:%s"%routeInfo.route.Size())
	for i in range(routeInfo.route.Size()):
		pt = routeInfo.route.GetElement(i)
		SoBridgeLogOutput(0, "route point: (%s,%s,%s)" % (pt.x,pt.y,pt.z))


def SampleNavigate(inputPoints):
	SoBridgeLogOutput(0, "SampleNavigate:")
	navigateInfo = pySimOneIO.navigate(inputPoints)
	if navigateInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	SoBridgeLogOutput(0, "roadIdListcount:%s"%navigateInfo.roadIdList.Size())

	for i in range(navigateInfo.roadIdList.Size()):
		roadId = navigateInfo.roadIdList.GetElement(i)
		SoBridgeLogOutput(0, "roadId:%s" %roadId)

	SoBridgeLogOutput(0, "indexOfValidPoints count:%s"%navigateInfo.indexOfValidPoints.Size())
	for i in range(navigateInfo.indexOfValidPoints.Size()):
		index = navigateInfo.indexOfValidPoints.GetElement(i)
		SoBridgeLogOutput(0, "index:%s" % index)


def SampleGetRoadMark(pos, laneId):
	SoBridgeLogOutput(0, "SampleGetRoadMark:")
	roadMarkInfo = pySimOneIO.getRoadMark(pos, laneId)
	if roadMarkInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	left = roadMarkInfo.left
	right = roadMarkInfo.right

	SoBridgeLogOutput(0,"left roadMark sOffset:%s"%left.sOffset)
	SoBridgeLogOutput(0,"left roadMark type:%s"% left.type)
	SoBridgeLogOutput(0,"left roadMark color:%s"% left.color)
	SoBridgeLogOutput(0,"left roadMark width:%s"% left.width)
	SoBridgeLogOutput(0,"right roadMark sOffset:%s"% right.sOffset)
	SoBridgeLogOutput(0,"right roadMark type:%s"% right.type)
	SoBridgeLogOutput(0,"right roadMark color:%s"% right.color)
	SoBridgeLogOutput(0,"right roadMark width:%s"% right.width)


def SampleGetTrafficLightList():
	SoBridgeLogOutput(0, "SampleGetTrafficLightList:")
	trafficLightList = pySimOneIO.getTrafficLightList()

	SoBridgeLogOutput(0, "trafficLight count:%s"%trafficLightList.Size())
	for i in range(trafficLightList.Size()):
		light = trafficLightList.GetElement(i)
		SoBridgeLogOutput(0, "light id:%s"% light.id)
		SoBridgeLogOutput(0, "light type:%s"% light.type.GetString())
		SoBridgeLogOutput(0, "light isDynamic:%s"% light.isDynamic)
		SoBridgeLogOutput(0, "validity count:%a"%light.validities.Size())

		for j in range(light.validities.Size()):
			validity = light.validities.GetElement(j)
			SoBridgeLogOutput(0,"validity roadId:%s"% validity.roadId)
			SoBridgeLogOutput(0,"validity fromLaneId:%s"% validity.fromLaneId)
			SoBridgeLogOutput(0,"validity toLaneId:%s"%validity.toLaneId)


def SampleGetTrafficSignList():
	SoBridgeLogOutput(0, "SampleGetTrafficSignList:")
	trafficSignList = pySimOneIO.getTrafficSignList()

	SoBridgeLogOutput(0, "trafficSign count:%s"% trafficSignList.Size())
	for i in range(trafficSignList.Size()):
		sign = trafficSignList.GetElement(i)
		SoBridgeLogOutput(0,"sign id:%s"%sign.id)
		SoBridgeLogOutput(0,"sign type:%s"%sign.type.GetString())
		SoBridgeLogOutput(0,"sign isDynamic:%s"% sign.isDynamic)
		SoBridgeLogOutput(0,"validity count:%s"% sign.validities.Size())
		for j in range(sign.validities.Size()):
			validity = sign.validities.GetElement(j)
			SoBridgeLogOutput(0,"validity roadId:%s"% validity.roadId)
			SoBridgeLogOutput(0,"validity fromLaneId:%s"% validity.fromLaneId)
			SoBridgeLogOutput(0,"validity toLaneId:%s"% validity.toLaneId)

def SampleGetStoplineList(laneId):
	pt = pySimOneIO.pySimPoint3D(-16,60.63,0)
	info = pySimOneIO.getNearMostLane(pt)
	if info.exists == False:
		SoBridgeLogOutput(0, "Can't find near most lane for input point!")
		return
	trafficLightList = pySimOneIO.getTrafficLightList()
	if trafficLightList.Size() < 1:
		SoBridgeLogOutput(0,"No traffic light exists!")
		return
	light0 = trafficLightList.GetElement(0)
	SoBridgeLogOutput(0, "SampleGetStoplineList:")
	stoplineList = pySimOneIO.getStoplineList(light0, laneId)

	SoBridgeLogOutput(0, "stopline count:%s"%stoplineList.Size())
	for i in range(stoplineList.Size()):
		stopline = stoplineList.GetElement(i)
		SoBridgeLogOutput(0, "stopline id:%s"% stopline.id)

def SampleGetCrosswalkList():
	pt=pySimOneIO.pySimPoint3D(-16,60.63,0)
	info=pySimOneIO.getNearMostLane(pt)
	if info.exists == False:
		SoBridgeLogOutput(0, "Can't find near most lane for input point!")
		return
	trafficLightList = pySimOneIO.getTrafficLightList()
	if trafficLightList.Size() < 1:
		SoBridgeLogOutput(0, "No traffic light exists!")
		return
	light0 = trafficLightList.GetElement(0)
	SoBridgeLogOutput(0, "SampleGetCrosswalkList:")
	crosswalkList = pySimOneIO.getCrosswalkList(light0, info.laneId)

	SoBridgeLogOutput(0, "crosswalk count:%s"% crosswalkList.Size())
	for i in range(crosswalkList.Size()):
		crosswalk = crosswalkList.GetElement(i)
		SoBridgeLogOutput(0, "crosswalk id:%s"% crosswalk.id)

def SampleGetCrossHatchList():
	pt=pySimOneIO.pySimPoint3D(-16,60.63,0)
	info=pySimOneIO.getNearMostLane(pt)
	if info.exists == False:
		SoBridgeLogOutput(0, "Can't find near most lane for input point!")
		return
	SoBridgeLogOutput(0,"SampleGetCrossHatchList:")
	crossHatchList = pySimOneIO.getCrossHatchList(info.laneId)

	SoBridgeLogOutput(0,"crossHatch count:%s"% crossHatchList.Size())
	for i in range(crossHatchList.Size()):
		crossHatch = crossHatchList.GetElement(i)
		SoBridgeLogOutput(0, "crossHatch id:%s"% crossHatch.id)

def SampleGetLaneMiddlePoint(pos, laneId):
	SoBridgeLogOutput(0, "SampleGetLaneMiddlePoint:")
	laneMiddlePointInfo = pySimOneIO.getLaneMiddlePoint(pos, laneId)
	if laneMiddlePointInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return

	SoBridgeLogOutput(0, "targetPoint vector: (%s,%s,%s)"%(laneMiddlePointInfo.targetPoint.x,laneMiddlePointInfo.targetPoint.y,laneMiddlePointInfo.targetPoint.z))
	SoBridgeLogOutput(0, "dir vector: (%s,%s,%s)"%laneMiddlePointInfo.dir.x,laneMiddlePointInfo.dir.y,laneMiddlePointInfo.dir.z)

def SampleGetHeights(pos):
	HeightsInfo = pySimOneIO.getHeights(pos, 10.0)
	if HeightsInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	for i in range(HeightsInfo.heights.Size()):
		SoBridgeLogOutput(0, "heights = %s" % HeightsInfo.heights.GetElement(i))

	for i in range(HeightsInfo.roadIdList.Size()):
		SoBridgeLogOutput(0, "roadId = %s" % HeightsInfo.roadIdList.GetElement(i))

	for i in range(HeightsInfo.insideRoadStates.Size()):
		SoBridgeLogOutput(0, "insideRoadState = %s" % HeightsInfo.insideRoadStates.GetElement(i))


def SampleGenerateRoute():
	inputPts = pySimOneIO.pySimPoint3DVector()
	pt1 = pySimOneIO.pySimPoint3D(-194.625, -6.500037, 0)
	pt2 = pySimOneIO.pySimPoint3D(172.493987, -2.731247, 0)
	inputPts.AddElement(pt1)
	inputPts.AddElement(pt2)
	generateRouteInfo = pySimOneIO.generateRoute(inputPts)
	if generateRouteInfo.exists == False:
		SoBridgeLogOutput(0, "Not exists!")
		return
	indexOfValidPoints = generateRouteInfo.indexOfValidPoints

	SoBridgeLogOutput(0, "indexOfValidPoints.Size() = %s" % indexOfValidPoints.Size())
	route = generateRouteInfo.route

	SoBridgeLogOutput(0, "route = %s" % route.Size())


def gpsCB(mainVehicleId, data):
	global PosX, PosY, PosZ
	PosX = data[0].posX
	PosY = data[0].posY
	PosZ = data[0].posZ
	#print("gpsCB: V:{0} X:{1} Y:{2} Z:{3}".format(mainVehicleId, PosX, PosY, PosZ))


def Samples(pos):
	#1. SampleGetNearMostLane
	laneId = SampleGetNearMostLane(pos)
	#2. SampleGetNearLanes
	SampleGetNearLanes(pos, 5)
	#3. SampleGetNearLanesWithAngle
	headingAngle = 30 / 180 * M_PI
	shiftAngle = 90 / 180 * M_PI
	SampleGetNearLanesWithAngle(pos, 5, headingAngle, shiftAngle)
	#4. GetDistanceToLaneBoundary
	SampleGetDistanceToLaneBoundary(pos)
	#5. GetLaneSample
	SampleGetLaneSample(laneId)
	#6. GetLaneLink
	SampleGetLaneLink(laneId)
	#7. GetLaneType
	SampleGetLaneType(laneId)
	#8. GetLaneWidth
	SampleGetLaneWidth(laneId, pos)
	#9. GetLaneST
	SampleGetLaneST(laneId, pos)
	#10. GetRoadST
	SampleGetRoadST(laneId, pos)
	#11. ContainsLane
	SampleContainsLane(laneId)
	#12. GetCrossHatchList
	SampleGetCrossHatchList()
	#13. GetTrafficLightList
	SampleGetTrafficLightList()
	#14. GetCrosswalkList
	SampleGetCrosswalkList()
	#15. GetHeights
	SampleGetHeights(pos)
	#16. GetInertialFromLaneST
	SampleGetInertialFromLaneST(laneId, 0, -3.5)
	#17. GetLaneMiddlePoint
	SampleGetLaneMiddlePoint(pos, laneId)
	#18. GetParkingSpaceList
	SampleGetParkingSpaceList()
	#19. GetPredefinedRoute
	SampleGetPredefinedRoute()
	#20. GetRoadMark
	SampleGetRoadMark(pos, laneId)
	#21. GetStoplineList
	SampleGetStoplineList(laneId)
	#22. GetTrafficSignList
	SampleGetTrafficSignList()
	#23. Navigate
	inputPoints = pySimOneIO.pySimPoint3DVector()
	pt1 = pySimOneIO.pySimPoint3D(562.7,531.4,0)
	pt2 = pySimOneIO.pySimPoint3D(837.9,618.4,0)
	inputPoints.AddElement(pt1)
	inputPoints.AddElement(pt2)
	SampleNavigate(inputPoints)
	# 24. GenerateRoute
	SampleGenerateRoute()
	
def main():
	#usage. Test api online with SimOne
	SoApiStart()
	ret = pySimOneIO.loadHDMap(100)
	SoBridgeLogOutput(0, "Load xodr success:", ret)

	#pos = pySimOneIO.pySimPoint3D(-5.41140, 156.28286, -0.53761)

	SoApiSetGpsUpdateCB(gpsCB)

	while (1):
		if PosX != 0:
			# print("gpsCB:  X:{0} Y:{1} Z:{2}".format( PosX, PosY, PosZ))
			pos = pySimOneIO.pySimPoint3D(PosX, PosY, PosZ)
			Samples(pos)
			time.sleep(2)

if __name__ == '__main__':
	main()

