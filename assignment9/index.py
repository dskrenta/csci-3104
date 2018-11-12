# Given edit costs
EDIT_COSTS = {
  'indel': 1,
  'swap': 5,
  'sub': 3,
  'no-op': 0
}

'''
alignStrings

Fills a matrix with edit distance costs given two strings. The matrix is first created and then populated using temporary values. 
All values are looped over and the min edit distance is determined using the edit costs. The operation with the least cost will 
be entered into the matrix for later use. The matrix allows values to be remembered reducing the amount of computation required.
'''
def alignStrings(s1, s2):
  len1 = len(s1)
  len2 = len(s2)
  table = [None] * (len2 + 1)

  # Populate the matrix
  for i in range(len2 + 1):
    table[i] = [0] * (len1 + 1)
  
  # Add values to the matrix
  for i in range(1, len2 + 1):
    table[i][0] = i
  for i in range(1, len1 + 1):  
    table[0][i] = i
  
  # Populate matrix with edit distance values with dynamic programming
  for i in range(1, len2 + 1):
    for j in range(1, len1 + 1):
      if s1[j - 1] == s2[i - 1]:
        d = 0
      else: 
        d = 1
      # Determine min operation and insert into matrix
      table[i][j] = min((table[i - 1][j - 1] + d) * EDIT_COSTS['sub'], (table[i - 1][j] + 1) * EDIT_COSTS['indel'], (table[i][j - 1] + 1) * EDIT_COSTS['indel'])
  return table

'''
extractAlignment

Returns a list containing the operations used to generate the true edit distance for two input strings. Inputs are string 1, string 2, 
and the edit distance matrix created from alignStrings. Rows will be looped over locating the min operation. That operation is convereted
from its numerical representation to a textual one in order to utlize the operations later. 
'''
def extractAlignment(s1, s2, table):
  a = [None] * len(table)
  prev = None

  # Insert correct operation given min operation for each row of the edit matrix
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

'''
commonSubstrings

Loops over x and y in order to find matching substrings. All substrings are first recorded and then filtered in order to 
comply with the length requirement. I did not recreate the second string from the list containing the operations due to running out of
time. The final filtered substrings are then returned.  
'''
def commonSubstrings(x, l, a, y):
  substrs = [''] * len(x)
  newSubstr = False
  currentIndex = 0
  
  # Each char in x and y are compared for similaries, then added to a substrings list 
  for i in range(0, len(x)):
    if x[i] == y[i]:
      if newSubstr:
        newSubstr = False
        currentIndex += 1
      substrs[currentIndex] += x[i]
    else:
      newSubstr = True
  finalSubstrs = []
  
  # Final substrings are created by filtering substrings given length
  for j in range(0, len(substrs)):
    if len(substrs[j]) > 0 and len(substrs[j]) >= l:
      finalSubstrs.append(substrs[j])
  return finalSubstrs

def partD():
  fileX = open('csci3104_PS9_data_string_x.txt', 'r')
  fileY = open('csci3104_PS9_data_string_y.txt', 'r')
  x = fileX.read()
  y = fileY.read()

  substrs = commonSubstrings(x, 10, [], y)
  print(substrs)

# Main execution
def main():
  matrix = alignStrings('sunday', 'saturday')
  a = extractAlignment('sunday', 'saturday', matrix)
  substrs = commonSubstrings('i like dogs and other stuff', 3, a, 'i like cats and other stuff')
  print(matrix)
  print(a)
  print(substrs)
  partD()

main()

'''
a) Done

b) 
  commonSubstrings: O(n) 
  alignStrings: O(n^2) 
  extractAlignment: O(n)
  O(n^2)

c) 

d) 
'''