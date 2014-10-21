import numpy
import cv2
import collections

from operator import itemgetter


class DotsBoard:
  
  def __init__(self, circles, image):
    self._dots = []
    
    if circles is not None:
      map(foo,circles)
#     print image.shape
#     print str([h for h in image[0:900, 0:600] if numpy.array_equal(h ,[255, 255, 255])])
      circles = sorted(circles,key=itemgetter(0))  
      circles = sorted(circles,key=itemgetter(1))
	#print str(circles[0..len(circles)][1]) + "\n"
      circles = filterCircles(circles,image)
#      cv2.imshow('img',image)
#      cv2.waitKey()
      assert len(circles) == 36, "too many circles found: %r \n\n %r" % (len(circles),  str(circles))
      for i in range(0, len(circles)):
        x = circles[i][0]
        y = circles[i][1]
        px = image[y][x][::-1]
        print "x: " + str(x) + " y: " + str(y) + " col: " + determineColour(px) + "\n"
        self._dots.append(Dot(i % 6,  i // 6,x ,y, px ))
		
  def printBoard(self):
    s = ""
    for i in range(0,6):
      for j in range(0,6):
        s += self._dots[j + i*6].getColour() +  " "
      s += "\n"
    return s
  
#POST: check there are exactly 6 distinct x and y coordinates with some tolerance and throw anything else away
def filterCircles(circles,image):
  #TODO: make proper filtration
  circles = [c for c in circles if c[0] < 510 and c[1] < 650]
  xs = map(lambda c: c[0],circles)
  ys = map(lambda c: c[1],circles)
  print collections.Counter(map(myround,xs))
  return [c for c in circles if c[0] < 510 and c[1] < 650]
  
def foo(c):
  c[0] = myround(c[0])
  c[1] = myround(c[1])
  return c

class Dot:
  
  Purple = numpy.array([157,90,183])
  Yellow = numpy.array([231,221,0])
  Red = numpy.array([241,91,59])
  Green = numpy.array([137,237,144])
  Blue = numpy.array([138,189,255])



  def __init__(self,x,y,extX,extY,col):
    self.x = x
    self.y = y
    self.externX = extX
    self.externY = extY
    self._col = determineColour(col)

  def getColour(self): return self._col

CONST_RANGE = 30
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
