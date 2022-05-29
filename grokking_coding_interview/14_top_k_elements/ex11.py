#!/usr/bin/env python
# Given a string, find if its letters can be rearranged in such a way that no two
# same characters come next to each other.

from collections import defaultdict
from heapq import *

def arrangeNotWorking( arr ):
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

      # This is incorrect cause the same character may be next
      # to each other
      freq += 1
      if freq < 0:
         heappush( maxHeap, ( freq, ch ) )

   return result

def arrange( arr ):
   hashMap = defaultdict( int )
   for a in arr:
      hashMap[ a ] += 1

   maxHeap = []
   for ch, freq in hashMap.items():
      heappush( maxHeap, ( -freq, ch ) )

   # maxHeap   result   prevChar,prevFreq
   # a:3,p:1   ''
   # p:1       a        (a,2)
   # a:2       ap
   # {}        apa      (a,1)
   result = ''
   prevChar, prevFreq = None, 0
   while maxHeap:
      freq, ch = heappop( maxHeap )
      freq = -freq

      if prevChar and prevFreq > 0:
         heappush( maxHeap, ( -prevFreq, prevChar ) )

      result += ch

      prevChar = ch
      prevFreq = freq - 1

   return result if len( result ) == len( arr ) else ''

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
