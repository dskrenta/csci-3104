import random

def indexOfLetter(x):
  letters = [
    'a', 'b', 'c', 'd', 'e', 
    'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 
    'z'
  ]
  return letters.index(x) + 1

def h1(x, l):
  xList = list(x)
  return sum(map(lambda x: indexOfLetter(x), xList)) % l

def h2(x, l):
  rand = random.randint(0, l - 1)
  xList = list(x)
  return sum(map(lambda x: indexOfLetter(x) * rand, xList)) % l

def a(names, l):
  h1Dict = {}
  h2Dict = {}

  def addToDict(data, value):
    if value in data:
      data[value] += 1
    else:
      data[value] = 1

  for name in names:
    addToDict(h1Dict, h1(name, l))
    addToDict(h2Dict, h2(name, l))
  
  return h1Dict, h2Dict

def ascii_histogram(data):
  for key,val in data.items():
    print('{k} {a}'.format(k = key, a= '*' * int(val)))

def b(data):
  print('H1 Histogram:')
  ascii_histogram(data[0])
  print('H2 Histogram:')
  ascii_histogram(data[1])

def getLongestChain(data):
  h1Max = max(data[0].items(), key = lambda x: x[1])[1]
  h2Max = max(data[1].items(), key = lambda x: x[1])[1]

  return h1Max, h2Max

def d1(names):
  print('Names length, (h1 collisions, h2 collisions)')

  firstNames = names[:len(names) // 8]
  firstNamesLen = len(firstNames)
  data = a(firstNames, 5701)
  print(firstNamesLen, getLongestChain(data))

  secondNames = names[:len(names) // 4]
  secondNamesLen = len(secondNames)
  data = a(secondNames, 5701)
  print(secondNamesLen, getLongestChain(data))

  thirdNames = names[:len(names) // 2]
  thirdNamesLen = len(thirdNames)
  data = a(thirdNames, 5701)
  print(thirdNamesLen, getLongestChain(data))

  print('The length of the longest chain increases when the number of names increases')


def getCollisions(data):
  h1Collisions = 0
  h2Collisions = 0

  for item in data[0].items():
    if item[1] > 1:
      h1Collisions += item[1]

  for item in data[1].items():
    if item[1] > 1:
      h2Collisions += item[1]
  
  return h1Collisions, h2Collisions

def d2(names):
  primes = [5701, 7927, 8831, 9733]

  res = list(map(lambda prime: getCollisions(a(names, prime)), primes))
  print('(h1 collisions, h2 collisions)')
  print(res)
  print('Collisions decrease when the number of buckets increase')

def main():
  file = open('dist.all.last.txt', 'r')
  names = list(map(lambda x: x.split('\t')[0].lower(), file.readlines()))
  random.shuffle(names)
  selectedNames = names[:len(names) // 2]
  result = a(selectedNames, 5701)
  b(result)
  d1(names)
  d2(selectedNames)

main()

