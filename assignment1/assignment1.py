prices = [
    23, 42, 53, 62, 13, 34, 23, 13, 6, 3, 
    1, 4, 64, 64, 34, 34, 67, 83, 23, 23,
    42, 83, 24, 24, 73, 82, 73, 72, 56, 93,
    23, 4, 7, 9, 13, 42, 34, 82, 52, 83,
    14, 64, 94, 23, 82, 24, 62, 14, 24, 29
]

def minPSoFar(a, i, minP):
    if i + 1 < len(a) - 1:
        if a[i] < minP:
            return minPSoFar(a, i + 1, a[i])
        else: 
            return minPSoFar(a, i + 1, minP)
    return minP

minPSoFarResult = minPSoFar(prices, 0, prices[0])

def maxProfitSoFar(a, i, maxP):
    currentProfit = a[i] - minPSoFarResult
    if i + 1 >= len(a):
        return maxP
    if currentProfit > maxP:
        return maxProfitSoFar(a, i + 1, currentProfit)
    else: 
        return maxProfitSoFar(a, i + 1, maxP)

maxProfitSoFarResult = maxProfitSoFar(prices, 0, 0)

print('MinPriceSoFar', minPSoFarResult)
print('MaxProfitSoFar', maxProfitSoFarResult)