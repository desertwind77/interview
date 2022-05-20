#!/usr/bin/env python
# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big
# rope with minimum cost. The cost of connecting two ropes is equal to the sum of
# their lengths.

from heapq import *

def connect( arr ):
   minHeap = []

   for a in arr:
      heappush( minHeap, a )

   cost = 0
   while len( minHeap ) > 1:
      first = heappop( minHeap )
      second = heappop( minHeap )
      length = first + second
      cost += length

      heappush( minHeap, length )

   return cost

testCases = [
      {
         'input' : [1, 3, 11, 5],
         'output' : 33,
      },
      {
         'input' : [3, 4, 5, 6],
         'output' : 36,
      },
      {
         'input' : [1, 3, 11, 5, 2],
         'output' : 42,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( connect( i ) == o )
