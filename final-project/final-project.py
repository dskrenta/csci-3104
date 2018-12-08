from random import uniform

def pandasPeril():
  cards = [5, 10, 15, 5, 10, 20, 4, 1]
  dynamicExpectedSum = 0

  def greedy(cards):
    left = cards[0]
    right = cards[len(cards) - 1]

    if left >= right:
      cards.pop(0) 
    else:
      cards.pop()

  def dynamic(cards):
    left = cards[0]
    right = cards[len(cards) - 1]
    leftNext = 0
    rightNext = 0

    if left > right: 
      # player 2 will pick left
      if (right + leftNext) > (left + rightNext):
        cards.pop()
      else: 
        cards.pop(0)
      None
    elif left < right: 
      # player 2 will pick right
      None
    else:
      # player 2 will pick left or right
      None

  def main():
    while len(cards) > 0:
      dynamic(cards)
      greedy(cards) 
  
  main()

def lcs(x, y):
  m = len(x)
  n = len(y)

  l = [[None] * (n + 1) for i in range(m + 1)]

  for i in range(m + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
          l[i][j] = 0
        elif x[i - 1] == y[j - 1]:
          l[i][j] = l[i - 1][j - 1] + 1
        else: 
          l[i][j] = max(l[i - 1][j], l[i][j - 1])
  return l[m][n]

def problem1():
  a_file = open('sequence_A.fa', 'r')
  b_file = open('sequence_B.fa', 'r')
  c_file = open('sequence_C.fa', 'r')

  A = a_file.read()
  B = b_file.read()
  C = c_file.read()

  a_file.close()
  b_file.close()
  c_file.close()

  A = ''.join(A.split()).replace('>', '')
  B = ''.join(B.split()).replace('>', '')
  C = ''.join(C.split()).replace('>', '')

  print(lcs(A, B)) # 2017
  print(lcs(A, C)) # 1985
  print(lcs(B, C)) # 2434

  # B and C are human (Homo Sapiens), A is soybean (Glycine Max) because b and c have the longest common substring

# problem1()

def convex_hull(points):
  """Computes the convex hull of a set of 2D points.

  Input: an iterable sequence of (x, y) pairs representing the points.
  Output: a list of vertices of the convex hull in counter-clockwise order,
    starting from the vertex with the lexicographically smallest coordinates.
  Implements Andrew's monotone chain algorithm. O(n log n) complexity.
  """

  # Sort the points lexicographically (tuples are compared lexicographically).
  # Remove duplicates to detect the case we have just one unique point.
  points = sorted(set(points))

  # Boring case: no points or a single point, possibly repeated multiple times.
  if len(points) <= 1:
    return points

  # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
  # Returns a positive value, if OAB makes a counter-clockwise turn,
  # negative for clockwise turn, and zero if the points are collinear.
  def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

  # Build lower hull 
  lower = []
  for p in points:
    while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)

  # Build upper hull
  upper = []
  for p in reversed(points):
    while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
      upper.pop()
    upper.append(p)

  # Concatenation of the lower and upper hulls gives the convex hull.
  # Last point of each list is omitted because it is repeated at the beginning of the other list. 
  return lower[:-1] + upper[:-1]

def randCoords(n):
  def newPoint():
    return (uniform(0, 100), uniform(0, 100))

  points = []

  for x in range(1, n):
    points.append(newPoint())

  return points

def problem4():
  points = randCoords(50)
  convex_hull_points = convex_hull(points)

  max_x = max(convex_hull_points, key=lambda x: x[0])[0]
  max_y = max(convex_hull_points, key=lambda x: x[1])[1]
  min_x = min(convex_hull_points, key=lambda x: x[0])[0]
  min_y = min(convex_hull_points, key=lambda x: x[1])[1]

  r_coords = [
    (min_x, max_y),
    (min_x, min_y),
    (max_x, max_y),
    (max_x, min_y)
  ]

  print(points)
  print(r_coords)

problem4()