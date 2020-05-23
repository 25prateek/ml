#!/usr/bin/python3

import cv2

cap=cv2.VideoCapture(0)
while cap.isOpened() :
  status,frame=cap.read()
  #converting image frame into gray scale
  grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  print(frame.shape)
  #line
  cv2.line(frame,(0,0),(200,300),(0,255,0),3)
  #rectangle
  cv2.rectangle(frame,(50,50),(150,200),(0,0,255),2)
  #circle
  cv2.circle(frame,(200,300),100,(13,44,123),2)
  #text writing
  font=cv2.FONT_HERSHEY_SIMPLEX #this is font  type
  cv2.putText(frame,"prateek",(10,50),font,2,(0,2,55),2,cv2.LINE_AA)
  cv2.imshow('live',frame)
  #cv2.imshow('livegray',grayimg)
  #cv2.imshow('live2',frame)
  #cv2.imshow('liv3',frame)
  if cv2.waitKey(10) & 0xff == ord('q'):
      break
cv2.destroyAllWindows()

cap.release()
