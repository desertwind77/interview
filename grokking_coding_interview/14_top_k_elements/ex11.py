#!/usr/bin/env python
# Given a string, find if its letters can be rearranged in such a way that no two
# same characters come next to each other.

from collections import defaultdict
from heapq import *

def arrange( arr ):
   hashMap = defaultdict( int )
   for a in arr:
      hashMap[ a ] += 1

   maxHeap = []
   for ch, freq in hashMap.items():
      heappush( maxHeap, ( -freq, ch ) )

   result = ''
   while maxHeap:
      freq, ch = heappop( maxHeap )
      if len( result ) > 0 and result[ -1 ] == ch:
         return ''
      result += ch

      freq += 1
      if freq < 0:
         heappush( maxHeap, ( freq, ch ) )

   return result

testCases = [
      {
         'input' : "aappp",
         'output' : "papap",
      },
      {
         'input' : "Programming",
         'output' : [ "rgmrgmPiano", "gmringmrPoa", "gmrPagimnor" ],
      },
      {
         'input' : "aapa",
         'output' : "",
      },
]

for test in testCases:
   i = test[ 'input' ]
   print( arrange( i ) )
