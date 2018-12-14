from random import randint

BUCKETS_COUNT = 100

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

def h1(x):
  xList = list(x)
  return sum(map(lambda x: indexOfLetter(x), xList)) % BUCKETS_COUNT

def h2(x):
  rand = randint(0, BUCKETS_COUNT - 1)
  xList = list(x)
  return sum(map(lambda x: indexOfLetter(x) * rand, xList)) % BUCKETS_COUNT

print(h1('stuff'), h2('stuff'))