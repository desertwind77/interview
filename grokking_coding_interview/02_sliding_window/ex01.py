#!/usr/bin/env python
#
# Maximum Sum Subarray of Size K (easy)
#
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum
# of any contiguous subarray of size ‘k’.

def maxSumSubarray( arr, k ):
   # index  : 0 1 2 3 4 5
   # array  : 2 1 5 1 3 2,  k = 3
   # sum    : 2 3 8 7 9 6
   # maxSum : 2 3 8 8 9 9
   total = maxTotal = 0
   for i in range( len( arr ) ):
      total += arr[ i ]
      if i >= k:
         total -= arr[ i - k ]
      maxTotal = max( total, maxTotal )

   return maxTotal

testCases = [
      {
         'input' : [2, 1, 5, 1, 3, 2],
         'k' : 3,
         'output' : 9,
      },
      {
         'input' : [2, 3, 4, 1, 5],
         'k' : 2,
         'output' : 7,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'k' ]
   o = test[ 'output' ]
   assert( maxSumSubarray( i, k ) == o )
