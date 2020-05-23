#!/usr/bin/python3

import cv2
#starting camera
cap=cv2.VideoCapture(0)
#adding plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
#saving video
#output=cv2.VideoWriter("class.avi",plugin,20,(640,480))#width,height
output=cv2.VideoWriter("class1.avi",plugin,80,(640,480))# after pluging 80is the speed for mat if u use 0-5 it goes slow 
while cap.isOpened() :
  status,frame=cap.read()
  cv2.imshow('liv',frame)
  #draw pattern
  output.write(frame)#sending data to VideoWrite
  if cv2.waitKey(10) & 0xff == ord('q'):
      break
cv2.destroyAllWindows() #this will destroy all windows

cap.release()
