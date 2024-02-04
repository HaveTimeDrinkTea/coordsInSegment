# Create dictionary of the coordinates
pointsDictAll = {
   "CoordNum1" : {
      "x" : 28, 
      "y" : 42,
      "direction": "North"},
   "CoordNum2" : {
      "x" : 27, 
      "y" : 46,
      "direction": "East"},
   "CoordNum3" : {
      "x" : 16, 
      "y" : 22,
      "direction": "South"},
   "CoordNum4" : {
      "x" : 40, 
      "y" : 50,
      "direction": "West"},
   "CoordNum5" : {
      "x" : 8, 
      "y" : 6,
      "direction": "North"},
   "CoordNum6" : {
      "x" : 6, 
      "y" : 19,
      "direction": "East"},
   "CoordNum7" : {
      "x" : 28, 
      "y" : 5,
      "direction": "South"},
   "CoordNum8" : {
      "x" : 39, 
      "y" : 36,
      "direction": "West"},
   "CoordNum9" : {
      "x" : 12, 
      "y" : 34,
      "direction": "North"},
   "CoordNum10" : {
      "x" : 36, 
      "y" : 20,
      "direction": "East"},
   "CoordNum11" : {
      "x" : 22, 
      "y" : 47,
      "direction": "South"},
   "CoordNum12" : {
      "x" : 33, 
      "y" : 19,
      "direction": "West"},
   "CoordNum13" : {
      "x" : 41, 
      "y" : 18,
      "direction": "North"},
   "CoordNum14" : {
      "x" : 41, 
      "y" : 34,
      "direction": "East"},
   "CoordNum15" : {
      "x" : 14, 
      "y" : 29,
      "direction": "South"},
   "CoordNum16" : {
      "x" : 6, 
      "y" : 49,
      "direction": "West"},
   "CoordNum17" : {
      "x" : 46, 
      "y" : 50,
      "direction": "North"},
   "CoordNum18" : {
      "x" : 17, 
      "y" : 40,
      "direction": "East"},
   "CoordNum19" : {
      "x" : 28, 
      "y" : 26,
      "direction": "South"},
   "CoordNum20" : {
      "x" : 2, 
      "y" : 12,
      "direction": "West"},
   }

print("================================================================")
print("================================================================")

# Request User Input

originNum = str(input("Please input a point number: --> "))
arcDegree = int(input("Please input the degree of the arc: --> "))
arcRadius = int(input("Please input the radius of the arc: --> "))

pooCordNum = "CoordNum" + originNum
pooX = pointsDictAll[pooCordNum]["x"]
pooY = pointsDictAll[pooCordNum]["y"]
pooDir = pointsDictAll[pooCordNum]["direction"]

print("")
print(f"You have chosen Point of Origin {originNum} with arc degree of {arcDegree} and arc radius of {arcRadius}")
print(f"This point is located at ({pooX},{pooY}) and points towards {pooDir}.")


# Compute the hypotenuse between the all other points vs POO

pointsDictTmp = pointsDictAll

pointsDictTmp.pop(pooCordNum)

# pointsDictTarget = {}

pointsDictTarget = pointsDictTmp


# Import math Library
import math

for i in pointsDictTmp.copy():
   tpoCordNum = i
   tpoX = pointsDictTmp[i]["x"]
   tpoY = pointsDictTmp[i]["y"]

   xDist = tpoX - pooX
   yDist = tpoY - pooY

   if xDist != 0:
      dist = round(math.sqrt(xDist**2 + yDist**2),2)
      angleThetaDegree = round((math.atan(yDist/xDist)/math.pi)*180,1)
   else:
      dist = yDist   
      angleThetaDegree = 0

   
   
   print(f"Target {tpoCordNum} vs origin {pooCordNum} has a distance of {dist} and the radius is {arcRadius} with degree of {angleThetaDegree}.")


   if abs(dist) > arcRadius:
      del pointsDictTmp[tpoCordNum]
      print(f"Target {tpoCordNum} has been eliminated as dist > arcRadius!")
   elif pooDir == "North" and yDist > 0:    
      if (angleThetaDegree >= 0) and (90 - angleThetaDegree <= (arcDegree*0.5)):
         print(f"Target {tpoCordNum} is in the same North direction and in the view of {pooCordNum}") 
      elif (angleThetaDegree <= 0) and (270 - angleThetaDegree >= (360-(arcDegree*0.5))):
         print(f"Target {tpoCordNum} is in the same North direction and in the view of {pooCordNum}") 
      else:
         print(f"Target {tpoCordNum} is not in the view of {pooCordNum} at all and it has been eliminated.") 
         del pointsDictTmp[tpoCordNum]
   elif pooDir == "South" and yDist < 0:
      if (angleThetaDegree >= 0) and (180 - angleThetaDegree <= (180 - (arcDegree*0.5))):
         print(f"Target {tpoCordNum} is in the same South direction and in the view of {pooCordNum}") 
      elif (angleThetaDegree <= 0) and (180 - angleThetaDegree >= (180 + (arcDegree*0.5))):
         print(f"Target {tpoCordNum} is in the same South direction and in the view of {pooCordNum}") 
      else:
         print(f"Target {tpoCordNum} is not in the view of {pooCordNum} at all and it has been eliminated.") 
         del pointsDictTmp[tpoCordNum]
   elif pooDir == "East" and xDist > 0:   
      if (angleThetaDegree >= 0) and (90 - angleThetaDegree >= (90 - (arcDegree*0.5))):
         print(f"Target {tpoCordNum} is in the same East direction and in the view of {pooCordNum}") 
      elif (angleThetaDegree <= 0) and (90 - angleThetaDegree <= (90 + (arcDegree*0.5))):
         print(f"Target {tpoCordNum} is in the same East direction and in the view of {pooCordNum}") 
      else:
         print(f"Target {tpoCordNum} is not in the view of {pooCordNum} at all and it has been eliminated.") 
         del pointsDictTmp[tpoCordNum]
   elif pooDir == "West" and xDist < 0:   
      if (angleThetaDegree >= 0) and (270 - angleThetaDegree >= (270 - (arcDegree*0.5))):
         print(f"Target {tpoCordNum} is in the same West direction and in the view of {pooCordNum}") 
      elif (angleThetaDegree <= 0) and (270 - angleThetaDegree <= (270 + (arcDegree*0.5))):
         print(f"Target {tpoCordNum} is in the same West direction and in the view of {pooCordNum}") 
      else:
         print(f"Target {tpoCordNum} is is not in the view of {pooCordNum} at all and has been eliminated.") 
         del pointsDictTmp[tpoCordNum]
   else:
      del pointsDictTmp[tpoCordNum]
      print(f"Target {tpoCordNum} is has been eliminated because it is not even in same direction as {pooCordNum}!")
   print("")   

print("")
print("****************************************************************")
print("****************************************************************")
print("")
if not pointsDictTmp:
   print(f"It appears that Origin {pooCordNum} cannot see  any other coordinates within an arc of {arcDegree} degrees and a distance of {arcRadius}:")
else:
   print(f"The following array contains the coordinate(s) that Origin {pooCordNum} can see in an arc of {arcDegree} degrees and a distance of {arcRadius}")
   print(pointsDictTmp)

print("")
print("================================================================")
print("================================================================")
