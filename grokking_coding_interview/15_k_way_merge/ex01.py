#!/usr/bin/env python
# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
import heapq

def mergeList( lists ):
   minHeap = []
   mergedList = []

   numElems = 0
   for l in lists:
      numElems += len( l )

   index = 0
   for i in range( len( lists ) ):
      heapq.heappush( minHeap, ( lists[ i ][ index ], i, index + 1 ) )

   while len( mergedList ) < numElems:
      value, lIndex, eIndex = heapq.heappop( minHeap )
      mergedList.append( value )
      if eIndex < len( lists[ lIndex ] ):
         heapq.heappush( minHeap, ( lists[ lIndex ][ eIndex ], lIndex, eIndex + 1 ) )

   return mergedList

testCases = [
      {
         'input' : [ [2, 6, 8], [3, 6, 7], [1, 3, 4] ],
         'output' : [1, 2, 3, 3, 4, 6, 6, 7, 8],
      },
      {
         'input' : [ [5, 8, 9], [1, 7] ],
         'output' : [1, 5, 7, 8, 9],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( mergeList( i ) == o )
