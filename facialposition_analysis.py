#Author: Jiamin Sun
#Start date: 02/13/2017

import numpy as np
import re
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, show


data = open('./facialdata/dataFile_facedection.txt')


def gui_analysis(data_gui):

    content = data_gui.readlines()
    lines = []

    for i in content:
        patt = re.compile("[^\t]+")
        each_line = patt.findall(i)
        lines.append(each_line)


    index = []   
    dist = []
    clusters = []
     
    for i in range(0, len(lines)):
        for j in lines[i]:
        
            list_after = j.split(" ")
            index.append(list_after)
            print(list_after)
#            if list_after[3] != '0.0\n':
            num = list_after[3].replace("\n", "")
            cluster = list_after[2].split(",")
            x = float(cluster[0])
            y = float(cluster[1])

            if float(num) < 800 and float(num) > 200:
                dist.append(float(num))
                clusters.append((x, y))
                
    for (x, y) in clusters:
        plt.plot(x, y, '+')
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.savefig('destination_path.eps', format='eps', dpi=300)
#    show()
            

#    print(dist)
#    dist_nor = []
#    average = []
#    for i in dist:
#        average.append(i)
#        if len(average) == 9:
##            print(average)
#            ave = sum(average)/len(average)
#            dist_nor.append(ave)
#            average = []
#            
#        
#    plt.plot(dist_nor)
#    plt.ylim(ymin=100)
#    plt.ylim(ymax = 700)
#    
#    plt.xlabel("Counting")
#    plt.ylabel("Distance between face and reading surface")
#    plt.legend(["Yaw", "Pitch", "Roll"])         
    # savefig('fig.png')


gui_analysis(data)









