from DotsBoard import Dot
allGreenDots = [
    Dot(1,1,10,10,Dot.Green),
    Dot(2,1,20,10,Dot.Green),
    Dot(3,1,30,10,Dot.Green),
    Dot(4,1,40,10,Dot.Green),
    Dot(5,1,50,10,Dot.Green),
    Dot(6,1,60,10,Dot.Green),
    Dot(1,2,10,20,Dot.Green),
    Dot(2,2,20,20,Dot.Green),
    Dot(3,2,30,20,Dot.Green),
    Dot(4,2,40,20,Dot.Green),
    Dot(5,2,50,20,Dot.Green),
    Dot(6,2,60,20,Dot.Green),
    Dot(1,3,10,30,Dot.Green),
    Dot(2,3,20,30,Dot.Green),
    Dot(3,3,30,30,Dot.Green),
    Dot(4,3,40,30,Dot.Green),
    Dot(5,3,50,30,Dot.Green),
    Dot(6,3,60,30,Dot.Green),
    Dot(1,4,10,40,Dot.Green),
    Dot(2,4,20,40,Dot.Green),
    Dot(3,4,30,40,Dot.Green),
    Dot(4,4,40,40,Dot.Green),
    Dot(5,4,50,40,Dot.Green),
    Dot(6,4,60,40,Dot.Green),
    Dot(1,5,10,50,Dot.Green),
    Dot(2,5,20,50,Dot.Green),
    Dot(3,5,30,50,Dot.Green),
    Dot(4,5,40,50,Dot.Green),
    Dot(5,5,50,50,Dot.Green),
    Dot(6,5,60,50,Dot.Green),
    Dot(1,6,10,60,Dot.Green),
    Dot(2,6,20,60,Dot.Green),
    Dot(3,6,30,60,Dot.Green),
    Dot(4,6,40,60,Dot.Green),
    Dot(5,6,50,60,Dot.Green),
    Dot(6,6,60,60,Dot.Green),
  ]

greenBoard = """G G G G G G 
G G G G G G 
G G G G G G 
G G G G G G 
G G G G G G 
G G G G G G \n"""

sampleBoard1 = [
    Dot(1,1,10,10,Dot.Green),
    Dot(2,1,20,10,Dot.Green),
    Dot(3,1,30,10,Dot.Red),
    Dot(4,1,40,10,Dot.Purple),
    Dot(5,1,50,10,Dot.Green),
    Dot(6,1,60,10,Dot.Blue),
    Dot(1,2,10,20,Dot.Green),
    Dot(2,2,20,20,Dot.Green),
    Dot(3,2,30,20,Dot.Green),
    Dot(4,2,40,20,Dot.Green),
    Dot(5,2,50,20,Dot.Green),
    Dot(6,2,60,20,Dot.Green),
    Dot(1,3,10,30,Dot.Green),
    Dot(2,3,20,30,Dot.Green),
    Dot(3,3,30,30,Dot.Green),
    Dot(4,3,40,30,Dot.Green),
    Dot(5,3,50,30,Dot.Green),
    Dot(6,3,60,30,Dot.Green),
    Dot(1,4,10,40,Dot.Green),
    Dot(2,4,20,40,Dot.Green),
    Dot(3,4,30,40,Dot.Green),
    Dot(4,4,40,40,Dot.Green),
    Dot(5,4,50,40,Dot.Green),
    Dot(6,4,60,40,Dot.Green),
    Dot(1,5,10,50,Dot.Green),
    Dot(2,5,20,50,Dot.Green),
    Dot(3,5,30,50,Dot.Green),
    Dot(4,5,40,50,Dot.Green),
    Dot(5,5,50,50,Dot.Green),
    Dot(6,5,60,50,Dot.Green),
    Dot(1,6,10,60,Dot.Blue),
    Dot(2,6,20,60,Dot.Blue),
    Dot(3,6,30,60,Dot.Blue),
    Dot(4,6,40,60,Dot.Blue),
    Dot(5,6,50,60,Dot.Blue),
    Dot(6,6,60,60,Dot.Blue),
  ]

sampleBoardCommands = "2,6 -> 3,6 -> 4,6 -> 5,6"
sampleBoardCommandsResult = [(20,60),(30,60),(40,60),(50,60)]

boardSample1 = """G G R P G B 
G G G G G G 
G G G G G G 
G G G G G G 
G G G G G G 
B B B B B B \n"""

scrambledSampleBoard1 = [
    Dot(3,6,30,60,Dot.Blue),
    Dot(2,1,20,10,Dot.Green),
    Dot(3,1,30,10,Dot.Red),
    Dot(4,1,40,10,Dot.Purple),
    Dot(5,1,50,10,Dot.Green),
    Dot(6,1,60,10,Dot.Blue),
    Dot(1,2,10,20,Dot.Green),
    Dot(2,2,20,20,Dot.Green),
    Dot(3,4,30,40,Dot.Green),
    Dot(1,5,10,50,Dot.Green),
    Dot(4,2,40,20,Dot.Green),
    Dot(5,2,50,20,Dot.Green),
    Dot(6,2,60,20,Dot.Green),
    Dot(1,3,10,30,Dot.Green),
    Dot(2,3,20,30,Dot.Green),
    Dot(3,3,30,30,Dot.Green),
    Dot(4,3,40,30,Dot.Green),
    Dot(4,6,40,60,Dot.Blue),
    Dot(1,1,10,10,Dot.Green),
    Dot(5,3,50,30,Dot.Green),
    Dot(6,3,60,30,Dot.Green),
    Dot(1,4,10,40,Dot.Green),
    Dot(2,4,20,40,Dot.Green),
    Dot(4,4,40,40,Dot.Green),
    Dot(5,4,50,40,Dot.Green),
    Dot(6,4,60,40,Dot.Green),
    Dot(2,5,20,50,Dot.Green),
    Dot(3,5,30,50,Dot.Green),
    Dot(4,5,40,50,Dot.Green),
    Dot(5,5,50,50,Dot.Green),
    Dot(6,5,60,50,Dot.Green),
    Dot(1,6,10,60,Dot.Blue),
    Dot(2,6,20,60,Dot.Blue),
    Dot(5,6,50,60,Dot.Blue),
    Dot(6,6,60,60,Dot.Blue),
    Dot(3,2,30,20,Dot.Green),
  ]

dotsPNG= """P G B P B G 
R G Y P P Y 
G Y P R P P 
B G Y R R Y 
B P P R P B 
P P G Y B B \n"""

dots1PMG = """B R B P G G 
R B P P B B 
G B G G R G 
R B R G B B 
R R G R R R 
G B B B B R \n"""
