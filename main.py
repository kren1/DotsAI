#!/usr/bin/env python
from DotsBoard import *
import cv2

image = cv2.imread("dots.png")

dots = DotsBoard(image)
print "\n" + dots.printBoard()




