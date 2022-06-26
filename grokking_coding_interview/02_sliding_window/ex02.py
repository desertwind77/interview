#!/usr/bin/env python
#
# Smallest Subarray with a Greater Sum (easy)
#
# Given an array of positive numbers and a positive number ‘S,’ find the length of
# the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return
# 0 if no such subarray exists.

def smallSubarray( arr, target ):
   start = end = 0
   total = 0
   size = len( arr )
   maxLen = size

   while end < size:
      total += arr[ end ]

      while start <= end and total >= target:
         maxLen = min( maxLen, end - start + 1 )
         total -= arr[ start ]
         start += 1

      end += 1

   return maxLen

testCases = [
      # index :  0 1 2 3 4  5
      # array :  2 1 5 2 3  2, target = 7
      #
      # start  end   total    maxLen
      # 0      0     2
      # 0      1     3
      # 0      2     8        3
      # 1      2     6        3
      # 1      3     8        3
      # 2      3     7        2
      # 2      4     10       2
      # 3      4     5        2
      # 3      5     7        2
      {
         'input' : [2, 1, 5, 2, 3, 2],
         'S' : 7,
         'output' : 2,
      },
      # index : 0 1 2 3 4
      # array : 2 1 5 2 8, target = 7
      #
      #
      # start  end   total    maxLen
      # 0      0     2
      # 0      1     3
      # 0      2     8        3
      # 1      2     6
      # 1      3     8        3
      # 2      3     7        2
      # 3      3     2        2
      # 3      4     10       2
      # 4      4     8        1
      {
         'input' : [2, 1, 5, 2, 8],
         'S' : 7,
         'output' : 1,
      },
      {
         'input' : [3, 4, 1, 1, 6],
         'S' : 8,
         'output' : 3,
      },
]

for test in testCases:
   i = test[ 'input' ]
   s = test[ 'S' ]
   o = test[ 'output' ]
   assert( smallSubarray( i, s ) == o )
