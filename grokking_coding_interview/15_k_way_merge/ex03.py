#!/usr/bin/env python
# Given an N * N matrix where each row and  column is sorted in ascending order, find
# the Kth smallest element in the matrix.
import heapq

def kSmallest( matrix, k ):
   minHeap = []
   clen = len( matrix[ 0 ] )
   count = 0

   for i in range( len( matrix ) ):
      heapq.heappush( minHeap, ( matrix[ i ][ 0 ], i, 1 ) )

   curVal = None
   while count < k:
      value, rIndex, cIndex = heapq.heappop( minHeap )
      curVal = value
      count += 1
      if cIndex < clen:
         heapq.heappush( minHeap, ( matrix[ rIndex ][ cIndex ], rIndex, cIndex + 1 ) )

   return curVal

testCases = [
   {
      'matrix' : [
         [2, 6, 8],
         [3, 7, 10],
         [5, 8, 11]
      ],
      'k' : 5,
      'output' : 7,
   },
]

for test in testCases:
   m = test[ 'matrix' ]
   k = test[ 'k' ]
   o = test[ 'output' ]
   assert( kSmallest( m, k ) == o )
