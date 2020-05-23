#!/usr/bin/python3

import cv2
#checking version
print(cv2.__version__)

#image reading
img=cv2.imread("a.jpg")
print(img)
#print shape
#print(img.shape)

print(type(img))

#to display image
cv2.imshow("a",img)

cv2.waitKey(30) #mili/micro seconds
