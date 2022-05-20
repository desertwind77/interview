#!/usr/bin/env python
# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers
# to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily
# present in the array.

from heapq import *

def findKClosestNumbers( arr, k, x ):
   maxHeap = []

   for a in arr:
      heappush( maxHeap, ( -abs( x - a ), a ) )
      if len( maxHeap ) > k:
         heappop( maxHeap )

   return sorted( [ i[ 1 ] for i in maxHeap ] )

testCases = [
      {
         'input' : [5, 6, 7, 8, 9],
         'K' : 3,
         'X': 7,
         'output' : [6, 7, 8],
      },
      {
         'input' : [2, 4, 5, 6, 9],
         'K' : 3,
         'X': 6,
         'output' : [4, 5, 6],
      },
      {
         'input' : [2, 4, 5, 6, 9],
         'K' : 3,
         'X': 10,
         'output' : [5, 6, 9],
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]
   x = test[ 'X' ]
   o = test[ 'output' ]
   assert( findKClosestNumbers( i, k, x ) == o )
