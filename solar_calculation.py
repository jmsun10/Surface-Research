import serial
import re
import time
from graphics import *
import math as m
import numpy


time_begin = '2017-02-26 11:46:00 ypr'
time_end = '2017-02-26 11:47:00 ypr'
#data from arduino are yaw, pitch, roll
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solar(time):

	time = time_begin.split(' ')
	
	standard_time_a = time[1].split(':')
	standard_time = round(int(standard_time_a[0]) + int(standard_time_a[1])/60, 2)
	
	od_a = time[0].split('-')
	od = 0
	for i in range(0, int(od_a[1])-1):
		od += months[i]
	od += int(od_a[2])

	standard_l = 75
	obs_l = 71
	lat =42
	d = 23.45

	equation_time = 60*(0.17*m.sin(2*0.0174532*(od - 80)) - 0.129*m.sin(0.0174532*(od - 8)))
	solar_time = standard_time +4*(standard_l - obs_l) + equation_time/60
	azimuth = m.atan((m.cos(23.45)*m.sin(solar_time/24))/(-m.cos(lat)*m.sin(23.45)*m.cos(solar_time/24)))
	altitude = m.asin(m.sin(lat)*m.sin(d) -m.cos(lat)*m.cos(d)*m.cos(solar_time/24))

	vec_z = 1
	vec_x = -1*m.tan(azimuth)
	vec_third = 1/m.cos(azimuth)
	vec_y = vec_third*m.tan(altitude)
	# print(vec_x, vec_y, vec_z)
	return vec_x, vec_y, vec_z

# solar(time_begin)
