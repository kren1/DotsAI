import numpy
import cv2
import collections

from operator import itemgetter
from pyparsing import *


class DotsBoard:
  
  def __init__(self, image):
    if image is None:
      return
    self._dots = []
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,2,20,
                            param1=2,param2=26,minRadius=15,maxRadius=22)
    circles = numpy.round(circles[0, :]).astype("int")
	
    
    if circles is not None:
      map(foo,circles)
#     print image.shape
#     print str([h for h in image[0:900, 0:600] if numpy.array_equal(h ,[255, 255, 255])])
      circles = sorted(circles,key=itemgetter(0))  
      circles = sorted(circles,key=itemgetter(1))
	#print str(circles[0..len(circles)][1]) + "\n"
     # circles = filterCircles(circles,image)
#      cv2.imshow('img',gray)
#      cv2.waitKey()
      assert len(circles) == 36, "too many circles found: %r \n\n %r" % (len(circles),  str(circles))
      for i in range(0, len(circles)):
        x = circles[i][0]
        y = circles[i][1]
        px = image[y][x][::-1]
       # print "x: " + str(x) + " y: " + str(y) + " col: " + determineColour(px) + "\n"
        self._dots.append(Dot(i % 6,  i // 6,x ,y, px ))
		
  def printBoard(self):
    s = ""
    for i in range(0,6):
      for j in range(0,6):
        s += self._dots[j + i*6].getColour() +  " "
      s += "\n"
    return s

  def matchPair(self, pair):
      for dot in self._dots:
          if dot.x == pair[0] and dot.y == pair[1]:
              return (dot.externX , dot.externY)

  def convertCommands(self,commands):
      ts = transition.parseString(commands)
      return map(self.matchPair, ts)



coordinate = Word("123450", max=1) + "," + Word("123450", max=1)
coordinate.setParseAction(lambda s,l,t:(int(t[0]), int(t[2])))
arrow = Literal("->").suppress()
transition = And(OneOrMore(coordinate + arrow) + coordinate)

#POST: check there are exactly 6 distinct x and y coordinates with some tolerance and throw anything else away
def filterCircles(circles,image):
  #TODO: make proper filtration
  circles = [c for c in circles if c[0] < 510 and c[1] < 650]
  xs = map(lambda c: c[0],circles)
  ys = map(lambda c: c[1],circles)
  #print collections.Counter(map(myround,xs))
  return [c for c in circles if c[0] < 510 and c[1] < 650]
  
def foo(c):
  c[0] = myround(c[0])
  c[1] = myround(c[1])
  return c

class Dot:
  
  Purple = numpy.array([157,90,183])
  Yellow = numpy.array([231,221,37])
  Red = numpy.array([235,93,70])
  Green = numpy.array([138,233,145])
  Blue = numpy.array([138,189,255])



  def __init__(self,x,y,extX,extY,col):
    self.x = x
    self.y = y
    self.externX = extX
    self.externY = extY
    self._col = determineColour(col)

  def getColour(self): return self._col

  def __repr__(self):
    return "x: {} y: {} maps to {}, {} \n".format(self.x,self.y,self.externX,self.externY)

CONST_RANGE = 10
def determineColour(col):
  if numpy.linalg.norm(numpy.array(col) - Dot.Green) < CONST_RANGE: return 'G'
  elif numpy.linalg.norm(numpy.array(col) - Dot.Purple) < CONST_RANGE: return 'P'
  elif numpy.linalg.norm(numpy.array(col) - Dot.Yellow) < CONST_RANGE: return 'Y'
  elif numpy.linalg.norm(numpy.array(col) - Dot.Red) < CONST_RANGE: return 'R'
  elif numpy.linalg.norm(numpy.array(col) - Dot.Blue) < CONST_RANGE: return 'B'
  else: raise ValueError("Colour " + str(col) +  " not recognized")
  
  
def rangeEq(a,b):
  return fabs(a -  b) < 5
  
def myround(x, base=10):
  return int(round(x*1.2,-1)/1.2)
def isRightColour(col):
  return numpy.linalg.norm(numpy.array(col) - Dot.Green) < CONST_RANGE or numpy.linalg.norm(numpy.array(col) - Dot.Purple) < CONST_RANGE or numpy.linalg.norm(numpy.array(col) - Dot.Yellow) < CONST_RANGE or numpy.linalg.norm(numpy.array(col) - Dot.Red) < CONST_RANGE or numpy.linalg.norm(numpy.array(col) - Dot.Blue) < CONST_RANGE
