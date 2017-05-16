# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 22:37:55 2016

@author: Jiamin Sun 
"""

#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import serial
import csv
import time

datafile = open('./motiondata/dataFile_rotation.txt','a')
ser = serial.Serial('com5', 115200, timeout = 1)
time.sleep(3)
ser.write("r".encode())

while (1 == 1):	

	line = ser.readline().decode()
	print(line)
	if line:
		datafile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ")
		datafile.write(line)
	else:
		ser.write("r".encode())
datafile.close()

