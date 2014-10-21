import numpy


class DotsBoard:
  
  def __init__(self):
    self._dots = []

  def printBoard(self):
    s = ""
    for i in range(0,6):
      for j in range(0,6):
        s += self._dots[j + i*6].getColour() +  " "
      s += "\n"
    return s


@total_ordering
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

  def __lt__(self, other):
    return self.x < other.x or (self.x == other.x and self.y < other.y)
  def __lt__(self, other):
    return self.x == other.x and self.y == other.y

def determineColour(col):
  if numpy.linalg.norm(numpy.array(col) - Dot.Green) < 6: return 'G'
  elif numpy.linalg.norm(numpy.array(col) - Dot.Purple) < 6: return 'P'
  elif numpy.linalg.norm(numpy.array(col) - Dot.Yellow) < 6: return 'Y'
  elif numpy.linalg.norm(numpy.array(col) - Dot.Red) < 6: return 'R'
  elif numpy.linalg.norm(numpy.array(col) - Dot.Blue) < 6: return 'B'
  else: raise ValueError("Colour " + str(col) +  " not recognized")


