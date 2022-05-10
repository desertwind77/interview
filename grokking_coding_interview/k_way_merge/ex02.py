#!/usr/bin/env python
# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
import heapq

def kSmallest( lists, k ):
   minHeap = []
   count = 0

   numElems = 0
   for l in lists:
      numElems += len( l )

   for i in range( len( lists ) ):
      heapq.heappush( minHeap, ( lists[ i ][ 0 ], i, 1 ) )

   curVal = None
   while count < k:
      value, lIndex, eIndex = heapq.heappop( minHeap )
      curVal = value
      count += 1
      if eIndex < len( lists[ lIndex ] ):
         heapq.heappush( minHeap, ( lists[ lIndex ][ eIndex ], lIndex, eIndex + 1 ) )

   return curVal

testCases = [
      {
         'input' : [ [2, 6, 8], [3, 6, 7], [1, 3, 4] ],
         'k' : 5,
         'output' : 4,
      },
      {
         'input' : [ [5, 8, 9], [1, 7], ],
         'k' : 3,
         'output' : 7,
      }
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'k' ]
   o = test[ 'output' ]
   assert( kSmallest( i, k ) == o )
