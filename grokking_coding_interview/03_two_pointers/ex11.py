#!/usr/bin/env python
#
# Minimum Window Sort (medium)
#
# Given an array, find the length of the smallest subarray in it which when sorted
# will sort the whole array.

def minWindowSort( arr ):
   left = 0
   while left < len( arr ) - 1 and arr[ left ] <= arr[ left + 1 ]:
      left += 1

   right = len( arr ) - 1
   while right > 0 and arr[ right ] >= arr[ right - 1 ]:
      right -= 1

   if left > right:
      return 0

   minNum = min( arr[ left : right + 1 ] )
   maxNum = max( arr[ left : right + 1 ] )

   start = 0
   while start <= left and arr[ start ] <= minNum:
      start += 1

   end = len( arr ) - 1
   while end >= right and arr[ end ] >= maxNum:
      end -= 1

   return end - start + 1

testCases = [
      {
         # Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole
         # array sorted
         'input' : [1, 2, 5, 3, 7, 10, 9, 12],
         'output' : 5,
      },
      {
         # Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole
         # array sorted
         'input' : [1, 3, 2, 0, -1, 7, 10],
         'output' : 5,
      },
      {
         # Explanation: The array is already sorted
         'input' : [1, 2, 3],
         'output' : 0,
      },
      {
         # Explanation: The whole array needs to be sorted.
         'input' : [3, 2, 1],
         'output' : 3,
      },
      {
         'input' : [1, 2, 5, 3, 2, 7, 10, 9, 12],
         'output' : 6,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( minWindowSort( i ) == o )
