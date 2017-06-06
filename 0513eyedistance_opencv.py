# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:55:14 2017
@author: Jiamin Sun

Working version
"""

import numpy as np
import cv2
import time
from datetime import datetime
#print time.strftime('%Y-%m-%d',time.localtime(time.time()))


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

"""
important: With webcam get(CV_CAP_PROP_FPS) does not work. That only works for videos. 
Below is the code to get the estimated rate manually. 
My test of the estimate rate:
Estimated frames per second -> 28.2685519988.
When finished this test, comment the lines below until (and including) cap.release. 
"""

"""       
propId is a number from 0 to 18. 
Each number denotes a property of the video (if it is applicable to that video)
below is the size of the capture. 
"""
width = cap.get(3)
height = cap.get(4)
print(width)
print(height)

font = cv2.FONT_HERSHEY_SIMPLEX

"""
0127_2017 definition to calculate the distance between camera and object
"""

def distance_to_camera(known_width, focal_length, per_width):
    return (known_width * focal_length) / per_width

"""
distance to calibrate
"""
    
known_distance = 500.0
#inches
#known_distance = 20

known_face_width = 110.0
#inches
#known_face_width = 4.3

#known_eye_width = 30.0

#focal length calculation

"""
export and save the video
"""
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 2, (640,480))

#out = cv2.VideoWriter('./data/'+ str(datetime.now()) +'_output.avi',fourcc, 20, (640,480))
casenumber = 11
out = cv2.VideoWriter('./facialdata/case' + str(casenumber) + '_output.avi',fourcc, 20, (640,480))
focals = []
focal_ave = 0
sum = 0

"""
the first wile loop for calibration

"""

while(True):
    # Capture frame-by-frame
#    try: 

        
    ret, frame = cap.read()
    start = time.time()
    if ret == True:
        #frame = cv2.flip(frame,0)
        out.write(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(frame, 1.1, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #print(w)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        px = str(x)
        py = str(y)
        position = px + "," + py
        #print("face width in pic: ", w)
        #print("face height in pic: ", h)
        """
        calculate focal lenth.
        """
        #need to convert the unit of w. 
        focal_length = (w * known_distance)/known_face_width        
        focals.append(focal_length)
        
        #print("focals: ", focals)
        if len(focals) == 25:

            for i in range(0, 10):
                sum += focals[i]
            focal_ave = sum/10
            print ("calibrating...")
            time.sleep(3)
            
#        if focal_ave!= 0:
#            print("focal calibration done!") #take 10 seconds
            
        #print("focal_length: ", focal_ave)
        
        distance_tocamera = distance_to_camera(known_face_width, focal_ave, w)
        with open('./facialdata/dataFile_facedection.txt', 'a') as datafile:
            datafile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " ")
            datafile.write(position + " ")
            datafile.write(str(distance_tocamera) + "\n")
        
        #cv2.putText(frame, distance_to_camera)
        print("Current time: ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
        print("Face position（px）: ", position)
        print("Distance between face and camera: ", distance_tocamera)
        
        
        
        """
        eye detection
        """

 
    try:
        cv2.imshow("frame", frame)
        end = time.time()
        interval = end - start
 #       print(interval)
    except:
        print("Fail")
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
datafile.close()
out.release()

cap.release()
cv2.destroyAllWindows()