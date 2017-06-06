import numpy as npopen('data.txt')
import re
import matplotlib.pyplot as plt

data_control = open('./controldata/controldata.txt')
def readtimeling(data):
	content = data.readlines()
	lines = []
	for i in content:
		patt = re.compile("[^\t]+")
		each_line = patt.findall(i)
		lines.append(each_line)


    
    index = []    
    for i in range(0, len(lines)):
#        if lines[i][0] == '2017-02-25 09:53:28 ypr':
        if lines[i][0] == '2017-02-26 11:43:28 ypr':
            index.append(i)
#        elif lines[i][0] == '2017-02-25 10:04:04 ypr':
        elif lines[i][0] == '2017-02-26 11:53:41 ypr':
            index.append(i)
#    print(index)

    line_wanted = []    
    for i in (lines[index[0]: index[-1]]):
        if i != ['\n']:
            line_wanted.append(i)
    
    y = []
    p = []
    r = []
    for i in line_wanted:
        y.append(i[1])
        p.append(i[2])
        r.append(i[3])
