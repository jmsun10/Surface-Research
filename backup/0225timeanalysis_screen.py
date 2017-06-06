#Author: Jiamin Sun
#Start date: 02/13/2017

import numpy as np
import re
import matplotlib.pyplot as plt


#time_paper = 636
time_screen = 620

#datafile_gui = open('data.txt')
#datafile_face = open('dataFile_facedection.txt')
#datafile_ro = open('./motiondata/dataFile_rotation.txt')
datafile_ti = open('./motiondata/dataFile_tilt.txt')

def gui_analysis(data_gui):

    content = data_gui.readlines()
    lines = []

    for i in content:
#        print(i)
        patt = re.compile("[^\t]+")
        each_line = patt.findall(i)

        lines.append(each_line)

    
    index = []    
    for i in range(0, len(lines)):
#        if lines[i][0] == '2017-02-25 09:53:28 ypr':
        if lines[i][0] == '2017-05-13 12:45:41 ypr':
            index.append(i)
#        elif lines[i][0] == '2017-02-25 10:04:04 ypr':
        elif lines[i][0] == '2017-05-13 13:13:00 ypr':
            index.append(i)
#    print(index)

    line_wanted = []    
    for i in (lines[index[0]: index[-1]]):
        if i != ['\n']:
            line_wanted.append(i)
    print(line_wanted)
    
    y = []
    p = []
    r = []
    for i in line_wanted:
        if len(i) == 4:
            y.append(i[1])
            p.append(i[2])
            r.append(i[3])

#yaw
#    plt.set_xticklabels(range(0, 58))
    length = len(y)
    print(length)
    
    x_range = []
    x_original = 0
    for i in range(0, length):
        x_original += time_screen/length
        x_range.append(x_original)
    print(len(x_range))        
        
    plt.plot(x_range, y)
#pitch
    plt.plot(x_range, p)
#roll
    plt.plot(x_range, r)
    plt.xlabel("Time/s")
    plt.ylabel("Degrees of Yaw, Pitch, Roll")
    plt.legend(["Yaw", "Pitch", "Roll"])            

            
    
#    re_lines = []
#
#    for line in lines:
#        for i in line:
#            re_line = i.split(" ")
#        re_lines.append(re_line)
#        re_line = []
#
#
#    count = []
#    for i in range(0, len(re_lines)):
#        for word in re_lines[i]:
#            if word == 'case':
#                count.append(i)
#    # print(count)
#
#
#    re_organize = []
#    for i in range(0, len(count) -1):
#        re_organize.append(re_lines[count[i]: count[i+1]])
#    # print(re_organize)
#    # print(re_organize[1][0][2] == "\n")
#    # print(type(re_organize[0][0][2]))
#    return re_organize


gui_analysis(datafile_ti)









