schools = [
  [5, 73],
  [10, 70],
  [10, 98],
  [105, 160],
  [120, 186],
  [90, 195],
  [13, 73],
  [482, 262],
  [351, 600],
  [12, 52],
  [61, 82],
  [151, 478],
  [121, 362],
  [1, 4],
  [1, 9],
  [7, 100],
  [345, 567],
  [12, 170],
  [111, 199],
  [234, 400],
  [132, 443],
  [1, 2],
  [100, 500],
  [351, 463],
  [17, 196]
]

def generateHitList(schools):
  hitList = {}
  for i in range(len(schools)):
    for j in range(schools[i][0], schools[i][1]):
      if not j in hitList:
        hitList[j] = [i]
      else: 
        hitList[j].append(i)
  return hitList

def removeHitListDuplicates(hitList):
  seen = []
  newHitList = {}
  for key in hitList:
    if hitList[key] not in seen:
      newHitList[key] = hitList[key]
      seen.append(hitList[key])
  return newHitList

def getMaxLength(hitList):
  maxLength = 0
  for key in hitList:
    if len(hitList[key]) > maxLength:
      maxLength = len(hitList[key])
  return maxLength

def getTimes(hitList):
  times = []
  schoolsCovered = set()
  sortedHitList = sorted(hitList.items(), key = lambda x: len(x[1]), reverse = True)
  for value in sortedHitList:
    if len(set(value[1]) - schoolsCovered) > 0:
      schoolsCovered.update(value[1])
      times.append(value[0])
  return times

def main(schools):
  hitList = generateHitList(schools)
  revisedHitList = removeHitListDuplicates(hitList)
  times = getTimes(revisedHitList)
  print(times)

main(schools)

'''
Generated Times: 
[151, 17, 61, 351, 7, 1]
'''