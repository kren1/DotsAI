#!/usr/bin/env python
import unittest
from DotsBoard import *
from pyparsing import ParseException
from dotsSampleData import *
import cv2
import numpy as np

class TestDotsBoard(unittest.TestCase):
  def setUp(self):
    self.board = DotsBoard(None)

  def test_printBoard(self):
    self.board._dots = allGreenDots
    self.assertEqual(self.board.printBoard(), greenBoard)
    self.board._dots = sampleBoard1
    self.assertEqual(self.board.printBoard(), boardSample1)
  def test_constructFromImage(self):
    image = cv2.imread("dots1.png")
    cv2.rectangle(image, (0,0),(670,120), (255,255,255), -1)
    cv2.rectangle(image, (0,780),(670,900), (255,255,255), -1)
	
    self.board = DotsBoard(image)
    self.assertEqual(self.board.printBoard(), dots1PMG)

  def test_translateCommands(self):
      self.board._dots = sampleBoard1
      self.assertEqual(self.board.convertCommands(sampleBoardCommands), sampleBoardCommandsResult)

  def test_parserExcpetionTesting(self):
      self.board._dots = sampleBoard1
      self.assertRaises(ParseException, self.board.convertCommands, "1,2 3,4")


class TestDot(unittest.TestCase):
  
  def setUp(self):
    self.dot = Dot(1,2,10,20,[137,237,144])

  def test_canCreateDotWithCoordinates(self):
    self.assertEqual(self.dot.x, 1)
    self.assertEqual(self.dot.y, 2)

  def test_hasRealCoordinates(self):
    self.assertEqual(self.dot.externX, 10)
    self.assertEqual(self.dot.externY, 20)

  def test_canGetColour(self):
    self.assertEqual(self.dot.getColour(), 'G')
    self.assertEqual(Dot(0,0,0,0,[157,90,183]).getColour(),'P')
    self.assertEqual(Dot(0,0,0,0,[231,221,30]).getColour(),'Y')
    self.assertEqual(Dot(0,0,0,0,[235,91,78]).getColour(),'R')

  def test_canGetColourWithRoughData(self):
    self.assertEqual(Dot(0,0,0,0,[159,88,182]).getColour(),'P')

  def test_throwsExceptionForInvalidColours(self):
    self.assertRaises(ValueError, Dot,0,0,0,0,[159,88,142])

  
unittest.main()
