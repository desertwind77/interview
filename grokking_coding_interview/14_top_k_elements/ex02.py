#!/usr/bin/env python
# Given an unsorted array of numbers, find Kth smallest number in it.
#
# Please note that it is the Kth smallest number in the sorted order, not the
# Kth distinct element.
#
# Note: For a detailed discussion about different approaches to solve this problem,
# take a look at Kth Smallest Number.

from heapq import *

def findKthSmallestNumber( arr, k ):
   if not arr:
      return None

   maxHeap = []

   for a in arr:
      heappush( maxHeap, -a )
      if len( maxHeap ) > k:
         heappop( maxHeap )

   return -maxHeap[ 0 ]

testCases = [
      {
         'input' : [1, 5, 12, 2, 11, 5],
         'K' : 3,
         'output' : 5,
      },
      {
         'input' : [1, 5, 12, 2, 11, 5],
         'K' : 4,
         'output' : 5,
      },
      {
         'input' : [5, 12, 11, -1, 12],
         'K' : 3,
         'output' : 11,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]
   o = test[ 'output' ]
   assert( findKthSmallestNumber( i, k ) == o )
