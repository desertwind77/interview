#!/usr/bin/env python
# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers
# in it.

from collections import defaultdict
from heapq import *

def topKFrequency( arr, k ):
   count = defaultdict( int )

   for a in arr:
      count[ a ] += 1

   minHeap = []
   for char, freq in count.items():
      heappush( minHeap, ( freq, char ) )
      if len( minHeap ) > k:
         heappop( minHeap )

   return [ i[ 1 ] for i in minHeap ]

testCases = [
      {
         'input' : [1, 3, 5, 12, 11, 12, 11],
         'K' : 2,
         'output' : [12, 11],
      },
      {
         'input' : [5, 12, 11, 3, 11],
         'K' : 2,
         'output' : [ [11, 5], [11, 12], [11, 3] ],
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]
   o = test[ 'output' ]
   print( topKFrequency( i, k ) )
