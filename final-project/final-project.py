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
    expectedSum = 0

    if left > right: 
      # player 2 will pick left
      if (right + leftNext) > (left + rightNext):
        None
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

  '''
  print(A)
  print(B)
  print(C)
  '''

  '''
  def lcs(X, Y, m, n):
    if m == 0 or n == 0:
      return 0
    elif X[m - 1] == Y[n - 1]:
      return 1 + lcs(X, Y, m-1, n-1)
    else: 
      return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))
  '''

  print(lcs(A, B))
  print(lcs(A, C))
  print(lcs(B, C))
  
problem1()
