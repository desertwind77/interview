#!/usr/bin/env python
# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized
# sub-arrays (or windows) of the array.
#
# Example 1:
#
# Input: nums=[1, 2, -1, 3, 5], k = 2
# Output: [1.5, 0.5, 1.0, 4.0]
# Explanation: Lets consider all windows of size ‘2’:
#
# [1, 2, -1, 3, 5] -> median is 1.5
# [1, 2, -1, 3, 5] -> median is 0.5
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 4.0
#
# Example 2:
#
# Input: nums=[1, 2, -1, 3, 5], k = 3
# Output: [1.0, 2.0, 3.0]
# Explanation: Lets consider all windows of size ‘3’:
#
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 2.0
# [1, 2, -1, 3, 5] -> median is 3.0

import heapq

class SlidingMedian:
   def __init__( self ):
      self.maxHeap, self.minHeap = [], []

   def findSlidingWindowMedian1( self, nums, k ):
      result = []
      for i in range( len( nums ) ):
         n = nums[ i ]
         if not self.maxHeap or n <= -1 * self.maxHeap[ 0 ]:
            heapq.heappush( self.maxHeap, -1 * n )
         else:
            heapq.heappush( self.minHeap, n )
         self.rebalance()

         totalLen = len( self.maxHeap ) + len( self.minHeap )
         if totalLen < k:
            continue
         elif totalLen > k:
            elem = nums[ i - k ]
            if elem <= -self.maxHeap[ 0 ]:
               self.remove( self.maxHeap, -elem )
            else:
               self.remove( self.minHeap, elem )

         self.rebalance()

         median = None
         if len( self.maxHeap ) == len( self.minHeap ):
            median = ( -self.maxHeap[ 0 ] + self.minHeap[ 0 ] ) / 2.0
         else:
            median = -self.maxHeap[ 0 ] / 1.0
         result.append( median )

      return result

   def findSlidingWindowMedian( self, nums, k ):
      result = []
      for i in range( len( nums ) ):
         n = nums[ i ]
         if not self.maxHeap or n <= -1 * self.maxHeap[ 0 ]:
            heapq.heappush( self.maxHeap, -1 * n )
         else:
            heapq.heappush( self.minHeap, n )
         self.rebalance()

         if len( self.maxHeap ) + len( self.minHeap ) < k:
            continue

         median = None
         if len( self.maxHeap ) == len( self.minHeap ):
            median = ( -self.maxHeap[ 0 ] + self.minHeap[ 0 ] ) / 2.0
         else:
            median = -self.maxHeap[ 0 ] / 1.0
         result.append( median )

         elem = nums[ i - k + 1 ]
         if elem <= -self.maxHeap[ 0 ]:
            self.remove( self.maxHeap, -elem )
         else:
            self.remove( self.minHeap, elem )
         self.rebalance()

      return result

   def remove( self, heap, elem ):
      '''removes an element from the heap keeping the heap property'''
      index = heap.index( elem )

      # move the element to the end and delete it
      heap[ index ] = heap[ -1 ]
      del heap[ -1 ]

      # we can use heapify to readjust the elements but that would be O(N),
      # instead, we will adjust only one element which will O(logN)
      if index < len( heap ):
         heapq._siftup( heap, index )
         heapq._siftdown( heap, 0, index )

   def rebalance( self ):
      if len( self.maxHeap ) - len( self.minHeap ) > 1:
         top = -heapq.heappop( self.maxHeap )
         heapq.heappush( self.minHeap, top )
      elif len( self.minHeap ) > len( self.maxHeap ):
         top = heapq.heappop( self.minHeap )
         heapq.heappush( self.maxHeap, -top )

testCases = [
      {
         'input' : [ 1, 2, -1, 3, 5 ],
         'k' : 2,
         'output' : [1.5, 0.5, 1.0, 4.0],
      },
      {
         'input' : [ 1, 2, -1, 3, 5 ],
         'k' : 3,
         'output' : [1.0, 2.0, 3.0],
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'k' ]
   o = test[ 'output' ]
   median = SlidingMedian()
   assert( median.findSlidingWindowMedian( i, k ) == o )
