#!/bin/bash
export LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH
echo $LD_LIBRARY_PATH
python PredefinedRoute.py
