#!/usr/bin/env python
#
# Subarrays with Product Less than a Target (medium)
#
# Given an array with positive numbers and a positive target number, find all of its
# contiguous subarrays whose product is less than the target number.

from functools import reduce
from collections import deque

def find_subarrays(arr, target):
   result = []
   product = 1
   left = 0
   for right in range(len(arr)):
      product *= arr[right]
      while (product >= target and left < len(arr)):
         product /= arr[left]
         left += 1

      # since the product of all numbers from left to right is less than the target 
      # therefore, all subarrays from left to right will have a product less than the 
      # target too; to avoid duplicates, we will start with a subarray containing only 
      # arr[right] and then extend it
      temp_list = deque()
      for i in range(right, left-1, -1):
         temp_list.appendleft(arr[i])
         result.append(list(temp_list))
      print( result )

   return result

def product( arr, target ):
   result = []

   for i in range( len( arr ) ):
      cur = arr[ i ]
      if cur < target:
         result.append( [ cur ] )

         j = i + 1
         while j < len( arr ):
            product = reduce( lambda x, y: x * y, arr[ i : j + 1 ] , 1 )
            if product < target:
               result.append( arr[ i : j + 1 ] )
            else:
               break
            j += 1

   return result

testCases = [
      {
         'input' : [2, 5, 3, 10],
         'target' : 30,
         'output' : [ [2], [5], [2, 5], [3], [5, 3], [10] ],
      },
      {
         'input' : [8, 2, 6, 5],
         'target' : 50,
         'output' : [ [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] ],
      },
      {
         'input' : [2, 5, 3, 10],
         'target' : 3000,
         'output' : [ [2], [2, 5], [2, 5, 3], [2, 5, 3, 10], [5],
                      [5, 3], [5, 3, 10], [3], [3, 10], [10] ],

      },
]

for test in testCases:
   i = test[ 'input' ]
   t = test[ 'target' ]
   o = sorted( test[ 'output' ] )
   assert( sorted( product( i, t ) ) == o )
   print( find_subarrays( i, t ) )
