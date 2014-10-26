#!/usr/bin/python
import subprocess
from DotsBoard import *
import cv2

cmd = "adb shell screencap -p /sdcard/dotsScreen.png && adb pull /sdcard/dotsScreen.png dots1.png && adb shell rm /sdcard/dotsScreen.png"

s = subprocess.Popen(cmd, shell=True)
s.wait()

image = cv2.imread("dots1.png")
cv2.rectangle(image, (0,0),(670,120), (255,255,255), -1)
cv2.rectangle(image, (0,780),(670,900), (255,255,255), -1)
#cv2.imshow('img',image)
#cv2.waitKey()

dots = DotsBoard(image)
print "\n" + dots.printBoard()

