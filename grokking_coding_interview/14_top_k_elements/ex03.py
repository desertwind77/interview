#!/usr/bin/env python
# Given an array of points in a 2D plane, find ‘K’ closest points to the origin.

import math
from heapq import *

def findKthSmallest( points, k ):
   maxHeap = []

   for p in points:
      distance = math.sqrt( p[ 0 ] * p[ 0 ] + p[ 1 ] * p[ 1 ] )
      heappush( maxHeap, ( -distance, p ) )
      if len( maxHeap ) > k:
         heappop( maxHeap )

   return [ p for _, p in maxHeap ]

testCases = [
      {
         'points' : [[1,2],[1,3]],
         'K' : 1,
         'output' : [[1,2]],
      },
      {
         'points' : [[1, 3], [3, 4], [2, -1]],
         'K' : 2,
         'output' : [[1, 3], [2, -1]],
      },
]

for test in testCases:
   p = test[ 'points' ]
   k = test[ 'K' ]
   o = test[ 'output' ]
   assert( findKthSmallest( p, k ) == o )
