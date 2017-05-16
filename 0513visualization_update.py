# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 22:37:55 2016

@author: Jiamin Sun 
"""

#!/usr/bin/env python
#sun vector refer 0.243219, -0.756384, 0.607229

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import serial
import re
import time
from graphics import *
import math as m

import solar_calculation as s

time_begin = '2017-05-13 13:08:00 ypr'
time_end = '2017-05-13 13:13:00 ypr'
time_range = []
#data from arduino are yaw, pitch, rolls
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
global solar_vector
solar_vector = s.solar(time_begin)

solarvertice = ((0,0,0), solar_vector)
solarvertical = ((0, 0, 0), (0, 3, 0))
print(solarvertice)
solaredges = ((0, 1), (1, 0))


# datafile_gui = open('data.txt')
# datafile_face = open('dataFile_facedection.txt')
# datafile_ro = open('dataFile_rotation.txt')
datafile_ti = open('./motiondata/dataFile_tilt.txt', 'r')


ax = ay = az = 0.0
yaw_mode = True





def resize(width, height):
	if height==0:
		height=1
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45, 1.0*width/height, 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def init():
	glShadeModel(GL_SMOOTH)
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClearDepth(1.0)
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LEQUAL)
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

def drawText(position, textString):     
	font = pygame.font.SysFont ("Courier", 18, True)
	textSurface = font.render(textString, True, (255,255,255,255), (0,0,0,255))     
	textData = pygame.image.tostring(textSurface, "RGBA", True)     
	glRasterPos3d(*position)     
	glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

def draw():
	global rquad
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);	
	glPolygonMode (GL_FRONT_AND_BACK, GL_LINE)
	glLoadIdentity()
	glTranslatef(0,0.0,-7.0)

	glRotatef(45, 0.0, 1.0, 0.0)

	glPointSize(5)
	glBegin(GL_POINTS)
	glColor3f(0.0,0,0.0)
	glEnd()


	glPushMatrix()
	# glRotatef(45, 0.0, 1.0, 0.0)
	glBegin(GL_LINES)
	glColor3f(255,255,255)
	for edge in solaredges:
		for ver in edge:
			glVertex3fv(solarvertice[ver])
	glEnd()
	glPopMatrix()



	glPushMatrix()

	# glRotatef(az-45, 0.0, 1.0, 0.0) #（az - 45 put it face the screen）
	glRotatef(az-45, 0.0, 1.0, 0.0)
	glRotatef(ay ,1.0,0.0,0.0)        # Pitch, rotate around x-axis
	glRotatef(-1*ax ,0.0,0.0,1.0)     # Roll,  rotate around z-axis	

	glBegin(GL_LINES)
	glColor3f(255, 255, 255)
	for edge in solaredges:
		for ver in edge:
			glVertex3fv(solarvertical[ver])
	glEnd()

	glBegin(GL_QUADS)	
	# glVertex2i(10,10)	#point drawing
	glColor3f(0.0,1.0,0.0)
	glVertex3f( 1.0, 0.05,-1.0)
	glVertex3f(-1.0, 0.05,-1.0)		
	glVertex3f(-1.0, 0.05, 1.0)		
	glVertex3f( 1.0, 0.05, 1.0)		
	
	glColor3f(1.0,0.5,0.0)	
	glVertex3f( 1.0,-0.05, 1.0)
	glVertex3f(-1.0,-0.05, 1.0)		
	glVertex3f(-1.0,-0.05,-1.0)		
	glVertex3f( 1.0,-0.05,-1.0)		

	glColor3f(1.0,0.0,0.0)		
	glVertex3f( 1.0, 0.05, 1.0)
	glVertex3f(-1.0, 0.05, 1.0)		
	glVertex3f(-1.0,-0.05, 1.0)		
	glVertex3f( 1.0,-0.05, 1.0)		

	glColor3f(1.0,1.0,0.0)	
	glVertex3f( 1.0,-0.05,-1.0)
	glVertex3f(-1.0,-0.05,-1.0)
	glVertex3f(-1.0, 0.05,-1.0)		
	glVertex3f( 1.0, 0.05,-1.0)		

	glColor3f(0.0,0.0,1.0)	
	glVertex3f(-1.0, 0.05, 1.0)
	glVertex3f(-1.0, 0.05,-1.0)		
	glVertex3f(-1.0,-0.05,-1.0)		
	glVertex3f(-1.0,-0.05, 1.0)		

	glColor3f(1.0,0.0,1.0)	
	glVertex3f( 1.0, 0.05,-1.0)
	glVertex3f( 1.0, 0.05, 1.0)
	glVertex3f( 1.0,-0.05, 1.0)		
	glVertex3f( 1.0,-0.05,-1.0)		
	glEnd()

	glPopMatrix()	
		 
def read_data_range():
	datafile_ti_inrange = open('./motiondata/dataFile_tilt_inrange.txt', 'w')
	# global ax, ay, az
	# ax = ay = az = 0.0


	# request data by sending a dot
#    ser.write(".".encode())
	#while not line_done:
	content = data_gui.readlines()
	# print(content)
	lines = []
	for i in content:
		# print(i)
		patt = re.compile("[^\t]+")
		each_line = patt.findall(i)
		lines.append(each_line)
	index = []    
	for i in range(0, len(lines)):

#        if lines[i][0] == '2017-02-25 09:53:28 ypr':
		if lines[i][0] == time_begin:
			index.append(i)
#        elif lines[i][0] == '2017-02-25 10:04:04 ypr':
		elif lines[i][0] == time_end:
			index.append(i)
	# print("index", index)
	line_wanted = []    
	for i in (lines[index[0]: index[-1]]):
		if i != ['\n']:
			line_wanted.append(i)
	for i in line_wanted:
		# print(i)
		i_string = " ".join(i)
		datafile_ti_inrange.write(i_string)

		# ax = float(i[1])
		# ay = float(i[2])
		# az = float(i[3])
	datafile_ti_inrange.close()
		# time.sleep(1)

# data_gui = datafile_ti
# read_data_range()

def read_data(item):
	datafile_ti_inrange = open('./motiondata/dataFile_tilt_inrange.txt')
	global ax, ay, az
	ax = ay = az = 0.0	
	lines = datafile_ti_inrange.readlines()
	lines_done = []
	for i in lines:
		each_line = i.split(' ')
		lines_done.append(each_line)


	# print(lines_done)
	for line in lines_done:
		# ax = line[5]
		# ay = line[4]
		# az = line[]
		#ax roll
		if float(lines_done[item][5]):
			ax = float(lines_done[item][5])
		#ay pich
			ay = float(lines_done[item][4])
		#az yaw
			az = float(lines_done[item][3])
	print(ax, ay, az)

def main():
	read_data_range()
	global yaw_mode

	video_flags = OPENGL|DOUBLEBUF
	
	pygame.init()
	screen = pygame.display.set_mode((800, 600), video_flags)
	pygame.display.set_caption("Press Esc to quit")
	background_color = (255, 255, 255)
	# screen.fill(background_color)
#    resize((640, 480))
	resize(800, 600)
  
	init()
	frames = 0
	ticks = pygame.time.get_ticks()

	item = 0

	while 1:
		event = pygame.event.poll()
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			break       
		if event.type == KEYDOWN and event.key == K_z:
			yaw_mode = not yaw_mode
			ser.write("z".encode())
		read_data(item)
		item += 1
		draw()
	  
		pygame.display.flip()
		frames = frames+1

	print("fps:  %d" % ((frames*1000)/(pygame.time.get_ticks()-ticks)))
	# ser.close()

if __name__ == '__main__': 
	data_gui = datafile_ti
	main()


