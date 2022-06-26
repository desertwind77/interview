#!/usr/bin/env python
#
# Longest Subarray with Ones after Replacement (hard)
#
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’
# 0s with 1s, find the length of the longest contiguous subarray having all 1s.

def longest( arr, k ):
   windowStart = maxLength = oneCount = 0
   for windowEnd in range( len( arr ) ):
      if arr[ windowEnd ] == 1:
         oneCount += 1

      if windowEnd - windowStart + 1 - oneCount > k:
         if arr[ windowStart ] == 1:
            oneCount -= 1
         windowStart += 1

      maxLength = max( maxLength, windowEnd - windowStart + 1 )

   return maxLength

testCases = [
      # index       : 0 1 2 3 4 5 6 7 8 9 10
      # input       : 0 1 1 0 0 0 1 1 0 1 1
      # windowStart : 0 0 0 0 0 1 2 3 4 5 5
      # oneCount    : 0 1 2 2 2 2 2 2 2 3 4
      #
      # windowStart : 0 0 0 0 1 2 3 4 5 5 5
      # oneCount    : 0 1 2 2 2 1 1 2 2 3 4
      # maxLength   : 1 2 3 4 4 4 4 4 4 5 6
      {
         'input' : [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
         'k' : 2,
         'output' : 6,
      },
      {
         'input' : [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
         'k' : 3,
         'output' : 9,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'k' ]
   o = test[ 'output' ]
   assert( longest( i, k ) == o )
