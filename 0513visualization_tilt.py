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


#ser = serial.Serial('/dev/tty.usbserial', 38400, timeout=1)
ser = serial.Serial('com4', 115200, timeout = 1)
time.sleep(3)
ser.write("r".encode("utf-8"))
datafile = open('./motiondata/dataFile_tilt.txt', 'a')
while (1 == 1):	

	line = ser.readline().decode()
	print(line)
	if line:
		datafile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+" ")
		datafile.write(line)
	else:
		ser.write("r".encode())
datafile.close()

"""
#test debug
#while (1==1):
#	data = ser.readline()
#	print("data:", data)
"""
