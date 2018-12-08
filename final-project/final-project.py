'''
David Skrenta
CSCI 3104 Algorithms
Final Project
'''

import random

def lcs(x, y):
  '''
  Finds the largest common subsequence in strings x and y
  '''

  # Get lengths of input strings
  len_x = len(x)
  len_y = len(y)

  # Create 2D array for storing subproblem values
  l = [[None] * (len_y + 1) for i in range(len_x + 1)]

  # Fill in 2D array in bottom up pattern
  for i in range(len_x + 1):
    for j in range(len_y + 1):
        if i == 0 or j == 0:
          l[i][j] = 0
        elif x[i - 1] == y[j - 1]:
          l[i][j] = l[i - 1][j - 1] + 1
        else: 
          l[i][j] = max(l[i - 1][j], l[i][j - 1])

  # Last value of 2D array contains lcs
  return l[len_x][len_y]

def problem1():
  '''
  Opens the three unknown species files
  Performs lcs comparisons on each file
  Presents results
  '''

  # Open files
  a_file = open('sequence_A.fa', 'r')
  b_file = open('sequence_B.fa', 'r')
  c_file = open('sequence_C.fa', 'r')

  # Read file data
  A = a_file.read()
  B = b_file.read()
  C = c_file.read()

  # Close files
  a_file.close()
  b_file.close()
  c_file.close()

  # Trim > and remove new lines
  A = ''.join(A.split()).replace('>', '')
  B = ''.join(B.split()).replace('>', '')
  C = ''.join(C.split()).replace('>', '')

  # Display lcs results
  print('(A, B):', str(lcs(A, B))) # 2017
  print('(A, C):', str(lcs(A, C))) # 1985
  print('(B, C):', str(lcs(B, C))) # 2434

  # B and C are human (Homo Sapiens), A is soybean (Glycine Max) because b and c have the longest common substring

def problem3():
  '''
  Contains greedy and player1 strategy functions
  Contains main Pandas Peril game loop which calls both functions
  Presents results
  '''

  def greedy(cards):
    left = cards[0]
    right = cards[len(cards) - 1]

    # Pick either left or right card depending on which is larger
    if left >= right:
      return cards.pop(0) 
    else:
      return cards.pop()

  def player1(cards):
    left = cards[0]
    right = cards[len(cards) - 1]
    nextLeft = 0
    nextRight = 0

    # Safely set next left if exists
    try: 
      nextLeft = cards[1]
    except: 
      None
    
    # Safely set next right if exists
    try: 
      nextRight = cards[len(cards) - 2]
    except: 
      None

    if left >= right:
      # Player 2 will pick left
      # Check if next move will be greater than left + greedy next right
      if (right + nextLeft) > (left + nextRight):
        return cards.pop()
      else: 
        return cards.pop(0)
    else:
      # Player 2 will pick right
      # Check if next move will be greather than right + greedy next left
      if (right + nextLeft) < (left + nextRight):
        return cards.pop(0)
      else: 
        return cards.pop()

  def main():
    cards = []
    # Inserts random numbers between 1 and 25 to cards
    for x in range(0, 10):
      cards.append(random.randint(1, 25))
    initialCards = cards.copy()
    player1_sum = 0
    player2_sum = 0

    # Main game loop which simulates turns
    # Terminates when cards contains no more cards
    while len(cards) > 0:
      player1_sum += player1(cards)
      player2_sum += greedy(cards) 

    # Output results
    print('Cards', initialCards)
    print('Player 1:', str(player1_sum))
    print('Player 2:', str(player2_sum))
  
  main()

def convex_hull(points):
  '''
  Generates the convex hull of set of given input points organized in a list of tuples: [(x, y)...]
  Implements the monotone chain algorithm: O(n log n) complexity
  Returns the list of points included in the convex_hull in the same format as the input points
  '''

  # Sorts the points and removes any duplicates
  points = sorted(set(points))

  # Make sure points contains more than 1 point
  if len(points) <= 1:
    return points

  # Computes the cross product for the vector inputs x, y, z
  def cross_product(x, y, z):
    return (y[0] - x[0]) * (z[1] - x[1]) - (y[1] - x[1]) * (z[0] - x[0])

  # Generates lower section of the convex hull 
  lower = []
  for p in points:
    while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)

  # Generates the upper section of the convex hull
  upper = []
  for p in reversed(points):
    while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
      upper.pop()
    upper.append(p)
 
  # Combines the upper and lower sections of the convex hull together to form the final convex hull
  # Last point is removed because it is also contained in the beginning
  return lower[:-1] + upper[:-1]

def randCoords(n):
  '''
  Generates random coordinates given a value n which specifies the number of coordinates to return
  Coordinates are [(x, y)] with a max value of 100 and a min value of 0 
  '''

  # Generates a new random (x, y) pair within 0 - 100 for each x and y
  def newPoint():
    return (random.uniform(0, 100), random.uniform(0, 100))

  points = []

  # Appends random points to points list
  for x in range(1, n):
    points.append(newPoint())

  return points

def problem4():
  '''
  Gets the random points from randCoords
  Generates the convex hull from convex_hull
  Builds the bounding box coordinates given max_x, max_y, min_x, and min_y
  '''

  # Gets random coordinates 
  points = randCoords(50)

  # Builds convex hull from random coordinates
  convex_hull_points = convex_hull(points)

  # Calculates max_x, max_y, min_x, min_y
  max_x = max(convex_hull_points, key=lambda x: x[0])[0]
  max_y = max(convex_hull_points, key=lambda x: x[1])[1]
  min_x = min(convex_hull_points, key=lambda x: x[0])[0]
  min_y = min(convex_hull_points, key=lambda x: x[1])[1]

  # Builds bounding box with max values obtained above
  r_coords = [
    (min_x, max_y),
    (min_x, min_y),
    (max_x, max_y),
    (max_x, min_y)
  ]

  print(points)
  print(r_coords)

print('Problem 1:')
problem1()
print('Problem 3:')
problem3()
print('Problem 4:')
problem4()