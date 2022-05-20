#!/usr/bin/env python
# Design a class to efficiently find the Kth largest element in a stream of numbers.
#
# The class should have the following two things:
#
# 1. The constructor of the class should accept an integer array containing initial
#    numbers from the stream and an integer ‘K’.
# 2. The class should expose a function add(int num) which will store the given number
#    and return the Kth largest number.

from heapq import *

class KthLargestNumber:
   def __init__( self, arr, k ):
      self.minHeap = []
      self.k = k

      for a in arr:
         heappush( self.minHeap, a )
         if len( self.minHeap ) > k:
            heappop( self.minHeap )

   def add( self, num ):
      heappush( self.minHeap, num )
      if len( self.minHeap ) > k:
         heappop( self.minHeap )

      return self.minHeap[ 0 ]

testCases = [
      {
         'input' : [3, 1, 5, 12, 2, 11],
         'K' : 4,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]

   number = KthLargestNumber( i, k )
   assert( number.add( 6 ) == 5 )
   assert( number.add( 13 ) == 6 )
   assert( number.add( 4 ) == 6 )
