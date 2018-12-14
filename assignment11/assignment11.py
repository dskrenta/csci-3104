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

def a(names):
  h1Dict = {}
  h2Dict = {}

  def addToDict(data, value):
    if value in data:
      data[value] += 1
    else:
      data[value] = 1

  for name in names:
    addToDict(h1Dict, h1(name, 5701))
    addToDict(h2Dict, h2(name, 5701))
  
  return h1Dict, h2Dict

def b(data):
  return False

def main():
  file = open('dist.all.last.txt', 'r')
  names = list(map(lambda x: x.split('\t')[0].lower(), file.readlines()))
  random.shuffle(names)
  selectedNames = names[:len(names) // 2]
  # print(selectedNames, len(names), len(selectedNames))
  result = a(selectedNames)
  print(result)

main()

# print(h1('stuff'), h2('stuff'))