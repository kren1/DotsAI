#!/usr/bin/python
import subprocess
from DotsBoard import *
import cv2
import os
from time import sleep

def sendEvents(commands):
    adbshell("sendevent /dev/input/event0 1 330 1")
    
    map(lambda p: tapPoint(p[0],p[1]),commands)
    adbshell("sendevent /dev/input/event0 1 330 0")
    adbshell("sendevent /dev/input/event0 0 0 0")

def adbshell(command, serial=None, adbpath='adb'):
    args = [adbpath]
    args.append('shell')
    args.append(command)
    s = subprocess.Popen(args, shell=True)
    s.wait()

def tapPoint(x,y):
    adbshell("sendevent /dev/input/event0 3 0 {}".format(x))
    adbshell("sendevent /dev/input/event0 3 1 {}".format(y))
    adbshell("sendevent /dev/input/event0 0 0 0")

while True:
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


#    print dots._dots
    print "\n"

    move = raw_input("Please enter your move: ")
    sendEvents(dots.convertCommands(move))
    sleep(1)

