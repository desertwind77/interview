#!/usr/bin/env python
# Given an array, find the sum of all numbers between the K1’th and K2’th smallest
# elements of that array.

from heapq import *

def sumBetween( arr, k1, k2 ):
   if k1 > k2:
      k1, k2 = k2, k1
   k1 = k1 + 1
   k2 = k2 - 1

   maxHeap = []

   for n in arr:
      heappush( maxHeap, -n )
      if len( maxHeap ) > k2:
         heappop( maxHeap )

   total = 0
   for _ in range( k2 - k1 + 1 ):
      top = maxHeap[ 0 ]
      heappop( maxHeap )
      total += -top

   return total

testCases = [
      {
         'input' : [1, 3, 12, 5, 15, 11],
         'K1' : 3,
         'K2' : 6,
         'output' : 23,
      },
      {
         'input' : [3, 5, 8, 7],
         'K1' : 1,
         'K2' : 4,
         'output' : 12,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k1 = test[ 'K1' ]
   k2 = test[ 'K2' ]
   o = test[ 'output' ]
   assert( sumBetween( i, k1, k2 ) == o )
