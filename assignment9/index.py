EDIT_COSTS = {
  'indel': 1,
  'swap': 5,
  'sub': 3,
  'no-op': 0
}

def alignStrings(s1, s2):
  len1 = len(s1)
  len2 = len(s2)
  table = [None] * (len2 + 1)
  for i in range(len2 + 1):
    table[i] = [0] * (len1 + 1)
  for i in range(1, len2 + 1):
    table[i][0] = i
  for i in range(1, len1 + 1):  
    table[0][i] = i
  for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
      if s1[j - 1] == s2[i - 1]:
        d = 0
      else: 
        d = 1
      table[i][j] = min((table[i - 1][j - 1] + d) * EDIT_COSTS['sub'], (table[i - 1][j] + 1) * EDIT_COSTS['indel'], (table[i][j - 1] + 1) * EDIT_COSTS['indel'])
  return table

def extractAlignment(s1, s2, table):
  a = [None] * len(table)
  prev = None
  for i in range(0, len(table)):
    if prev: 
      diff = min(table[i]) - prev
      if diff == 0:
        a[i] = '#'
      elif diff == 1: 
        a[i] = 'indel'
      elif diff == 3:
        a[i] = 'sub'
    elif min(table[i]) == 0: 
      a[i] = '#'
    prev = min(table[i])
  return a

def commonSubstrings(x, l, a, y):
  substrs = [''] * len(x)
  newSubstr = False
  currentIndex = 0
  for i in range(0, len(x)):
    if x[i] == y[i]:
      if newSubstr:
        newSubstr = False
        currentIndex += 1
      substrs[currentIndex] += x[i]
    else:
      newSubstr = True
  finalSubstrs = []
  for j in range(0, len(substrs)):
    if len(substrs[j]) > 0 and len(substrs[j]) >= l:
      finalSubstrs.append(substrs[j])
  return finalSubstrs

def main():
  matrix = alignStrings('sunday', 'saturday')
  a = extractAlignment('sunday', 'saturday', matrix)
  substrs = commonSubstrings('i like dogs and other stuff', 3, a, 'i like cats and other stuff')
  print(matrix)
  print(a)
  print(substrs)

main()