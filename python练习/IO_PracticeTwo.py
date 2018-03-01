#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
import os
dd = os.getcwd()
def findFile(fileName,dir):
    li = os.listdir(dir)
    for fi in li:
        route = os.path.join(dir,fi)
        if os.path.isfile(route) and fileName in fi:
            print(os.path.relpath(route,dd))
        if os.path.isdir(route):
            findFile(fileName,route)
dir = os.getcwd()
findFile('reduce',dir)

