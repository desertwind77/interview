#!/usr/bin/env python
# Given a string, sort it based on the decreasing frequency of its characters.

from collections import defaultdict
from heapq import *

def sort( arr ):
   count = defaultdict( int )
   for a in arr:
      count[ a ] += 1

   maxHeap = []
   for char, freq in count.items():
      heappush( maxHeap, ( -freq, char ) )

   result = ''
   while maxHeap:
      freq, char = heappop( maxHeap )
      for i in range( -freq ):
         result += char

   return result

testCases = [
      {
         'input' : "Programming",
         'output' : "rrggmmPiano",
      },
      {
         'input' : "abcbab",
         'output' : "bbbaac",
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   print( sort( i ) )
