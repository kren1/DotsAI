#!/usr/bin/env python
import unittest
from DotsBoard import *
from dotsSampleData import *

class TestDotsBoard(unittest.TestCase):
  def setUp(self):
    self.board = DotsBoard()

  def test_printBoard(self):
    self.board._dots = allGreenDots
    self.assertEqual(self.board.printBoard(), greenBoard)
    self.board._dots = sampleBoard1
    self.assertEqual(self.board.printBoard(), boardSample1)

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
    self.assertEqual(Dot(0,0,0,0,[231,221,0]).getColour(),'Y')
    self.assertEqual(Dot(0,0,0,0,[241,91,59]).getColour(),'R')

  def test_canGetColourWithRoughData(self):
    self.assertEqual(Dot(0,0,0,0,[159,88,182]).getColour(),'P')

  def test_throwsExceptionForInvalidColours(self):
    self.assertRaises(ValueError, Dot,0,0,0,0,[159,88,142])

  def test_isSortable(self): 
    self.assertTrue(all(map(lambda s, o: s.x == o.x and s.y == o.y ,
                    sorted(scrambledSampleBoard1, key=Dot.__lt__), sampleBoard1)))

unittest.main()
