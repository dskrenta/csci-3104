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
        
    elif left < right: 
      # player 2 will pick right
    else:
      # player 2 will pick left or right

  def main():
    while len(cards) > 0:
      dynamic(cards)
      greedy(cards) 
  
  main()

def lcs(X, Y, m, n):
  if m == 0 or n == 0:
    return 0
  elif X[m - 1] == Y[n - 1]:
    return 1 + lcs(X, Y, m-1, n-1)
  else: 
    return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))
