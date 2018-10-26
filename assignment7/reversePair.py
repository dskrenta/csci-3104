nums = [
  1, 2, 3, 4, 5, 
  6, 7, 8, 9, 10, 
  7, 34, 5, 2, 4, 
  6, 7, 98, 9, 4, 
  2, 2, 32, 4, 5, 
  6, 8, 8, 1, 3,
  3, 7, 2, 45, 2,
  2, 65, 1, 7, 2,
  23, 5, 2, 5, 2,
  21, 5, 1, 45, 1,
  3, 67, 2, 5, 2, 
  2, 6, 2, 4, 6,
  4, 5, 2, 54, 7,
  3, 4, 7, 2, 4, 
  7, 2, 4, 6, 2,
  2, 6, 12, 5, 2,
  6, 2, 4, 1, 4,
  3, 5, 2, 5, 12,
  3, 6, 2, 4, 6,
  3, 54, 6, 2, 5
]

class ReversePairs(object):
  def __init__(self):
      self.count = 0

  def reversePairs(self, arr):
      def mergeSort(arr):
          length = len(arr)
          if length <= 1:                      
              return arr
          else:               
              return merger(mergeSort(arr[:int(length / 2)]), mergeSort(arr[int(length / 2):]))

      def merger(left, right):
          l, r = 0, 0       
          while l < len(left) and r < len(right):
              if left[l] <= 2 * right[r]:
                  l += 1
              else:
                  self.count += len(left) - l
                  r += 1
          return sorted(left + right) 

      mergeSort(arr)
      return self.count
        
rp = ReversePairs()
print(rp.reversePairs(nums))