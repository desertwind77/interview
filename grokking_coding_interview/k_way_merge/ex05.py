#!/usr/bin/env python
# Given two sorted arrays in descending order, find ‘K’
# pairs with the largest sum where each pair consists of
# numbers from both the arrays.
import heapq

def kLargestPairs( lists, k ):
   minHeap = []

   for i in range( len( lists[ 0 ] ) ):
      for j in range( len( lists[ 1 ] ) ):
         if len( minHeap ) < k:
            heapq.heappush( minHeap, ( lists[ 0 ][ i ] + lists[ 1 ][ j ], lists[ 0 ][ i ], lists[ 1 ][ j ]  ) )
         else:
            if lists[ 0 ][ i ] + lists[ 1 ][ j ] < minHeap[ 0 ][ 0 ]:
               break
            else:
               heapq.heappop( minHeap )
               heapq.heappush( minHeap, ( lists[ 0 ][ i ] + lists[ 1 ][ j ], lists[ 0 ][ i ], lists[ 1 ][ j ]  ) )

   result = []
   for elem in minHeap:
      _, i, j = elem
      result.append( [ i, j ] )

   return result

testCases = [
   {
      'input' : [ [9, 8, 2], [6, 3, 1], ],
      'k' : 3,
      'output' : [ [9, 3], [9, 6], [8, 6] ],
   },
   {
      'input' : [ [ 5, 2, 1 ], [ 2, -1 ] ],
      'k' : 3,
      'output' : [ [5, 2], [5, -1], [2, 2] ],
   },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'k' ]
   o = test[ 'output' ]
   assert( sorted( kLargestPairs( i, k ) ) == sorted( o ) )
