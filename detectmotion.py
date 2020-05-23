#!/usr/bin/python3

import cv2
#start camera
cap=cv2.VideoCapture(0)

tp1=cap.read()[0] #take1
tp2=cap.read()[0] #take2
tp3=cap.read()[0] #take3

#to make more perfect converting its into gray or we can say that black and white
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)

#now creating image diff

def img_diff(x,y,z):
    #diffrence b/w x,y--gray1,gray2
    d1=cv2.absdiff(x,y)
    #diff b/w y,z --gray2,gray3 --d2
    d2=cv2.absdiff(y,z)
    #abs diff d1-d2
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg
#now appling fun
while cap.isOpened():
    status,frame=cap.read()# continious image taker
    motionimg=img_diff(gray1,gray2,gray3)
    #replacing img  frame
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtcolour(frame,cv2.COLOR_BGR2GRAY) #passing live image to gray3
    cv2.imshow('live',frame)
    cv2.imshow('motion',motionimg)
    if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
