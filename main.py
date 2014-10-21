#!/usr/bin/env python
import cv2
import numpy as np
from time import sleep
from operator import itemgetter, attrgetter


def printDots(circles, img):

	circles = sorted(circles, key=itemgetter(0,1))
	s = ""
	for i in range(0, len(circles)):
		if i % 6 == 0:
			print s
			s = ""
	s += str(img[circles[i][0],circles[i][1]][0]) + " "
	

image = cv2.imread("dots.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow('img',gray)
#cv2.waitKey()
circles = cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=13,maxRadius=0)

circles = np.round(circles[0, :]).astype("int")

printDots(circles,image)




