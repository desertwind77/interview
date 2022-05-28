#!/usr/bin/env python
# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the
# array such that we are left with maximum distinct numbers.

from collections import defaultdict
from heapq import *

def remove( arr, k ):
   hashMap = defaultdict( int )
   for a in arr:
      hashMap[ a ] += 1

   maxHeap = []
   for val, freq in hashMap.items():
      heappush( maxHeap, ( -freq, val ) )

   for _ in range( k ):
      freq, val = heappop( maxHeap )
      if freq < -1:
         freq += 1
         if freq > 0:
            heappush( maxHeap, ( freq, val ) )

   return len( maxHeap )

testCases = [
      {
         'input' : [7, 3, 5, 8, 5, 3, 3],
         'K' : 2,
         'output' : 3,
      },
      {
         'input' : [3, 5, 12, 11, 12],
         'K' : 3,
         'output' : 2,
      },
      {
         'input' : [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5],
         'K' : 2,
         'output' : 3,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]
   o = test[ 'output' ]
   print( remove( i, k ) )
