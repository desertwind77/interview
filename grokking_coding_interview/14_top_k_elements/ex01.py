#!/usr/bin/env python
# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
#
# Note: For a detailed discussion about different approaches to solve this problem,
# take a look at Kth Smallest Number.

from heapq import *

def findKthLargest( arr, k ):
   minHeap = []

   for a in arr:
      heappush( minHeap, a )
      if len( minHeap ) > k:
         heappop( minHeap )

   return [ i for i in minHeap ]

testCases = [
      {
         'input' : [3, 1, 5, 12, 2, 11],
         'K' : 3,
         'output' : [5, 12, 11],
      },
      {
         'input' : [5, 12, 11, -1, 12],
         'K' : 3,
         'output' : [12, 11, 12],
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]
   o = sorted( test[ 'output' ] )
   print( sorted( findKthLargest( i, k ) ) )
