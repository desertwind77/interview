#!/usr/bin/env python
# Given a string and a number ‘K’, find if the string can be rearranged such that the
# same characters are at least ‘K’ distance apart from each other.

from collections import defaultdict, deque
from heapq import *

def arrange1( arr, k ):
   # 'input' : "Programming",
   # g:2,r:2,m:2,p:1,o:1,a:1,i:1,n:1   ''       []
   # g:2,r:2,m:2,p:1,o:1,a:1,i:1,n:1   'g'      [None,g:1]     r:2,m:2,p:1,o:1,a:1,i:1,n:1
   # r:2,m:2,p:1,o:1,a:1,i:1,n:1       'gr'     [g:1,r:1]      m:2,p:1,o:1,a:1,i:1,n:1
   # m:2,p:1,o:1,a:1,i:1,n:1           'grm'    [r:1,m:1]      g:1,p:1,o:1,a:1,i:1,n:1
   # g:1,p:1,o:1,a:1,i:1,n:1           'grmg'   [m:1]          r:1,p:1,o:1,a:1,i:1,n:1
   # r:1,p:1,o:1,a:1,i:1,n:1           'grmgr'  []             m:1,p:1,o:1,a:1,i:1,n:1
   # ..
   hashMap = defaultdict( int )
   for a in arr:
      hashMap[ a ] += 1

   maxHeap = []
   for ch, freq in hashMap.items():
      heappush( maxHeap, ( -freq, ch ) )

   queue = deque()
   result = []
   while maxHeap:
      freq, ch = heappop( maxHeap )
      result.append( ch )

      if queue:
         top = queue.popleft()
         if top:
            prevCh, prevFreq = top
            heappush( maxHeap, ( -prevFreq, prevCh ) )

      freq = -freq
      freq -= 1
      if freq > 0:
         curLen = len( queue )
         for _ in range( k - curLen - 2 ):
            queue.append( None )
         queue.append( ( ch, freq ) )

   return ''.join( result ) if len( result ) == len( arr ) else ''

def arrange2( arr, k ):
   hashMap = defaultdict( int )
   for a in arr:
      hashMap[ a ] += 1

   maxHeap = []
   for ch, freq in hashMap.items():
      heappush( maxHeap, ( -freq, ch ) )

   queue = deque()
   result = []
   while maxHeap:
      negFreq, ch = heappop( maxHeap )
      if negFreq < 0:
         result.append( ch )
         queue.append( ( negFreq + 1, ch ) )

      # k = 2
      # m:-2,p:-2    m     p:-2     [m:-1]          p:-2
      # p:-2         mp    {}       [m:-1,p:-1]     m:-1
      # m:-1         mpm   {}       [p:-1,m:0]      p:-1
      # p:-1         mpmp  {}       [m:0,p:0]       {}
      if len( queue ) == k:
         prevNegFreq, prevCh = queue.popleft()
         heappush( maxHeap, ( prevNegFreq, prevCh ) )

   return ''.join( result ) if len( result ) == len( arr ) else ''

testCases = [
      {
         'input' : "mmpp",
         'K' : 2,
         'output' : [ "mpmp", "pmpm" ]
      },
      {
         'input' : "Programming",
         'K' : 3,
         'output' : [ "rgmPrgmiano", "gmringmrPoa", "gmrPagimnor" ] # and a few more
      },
      {
         'input' : "aab",
         'K' : 2,
         'output' : "aba",
      },
      {
         'input' : "aappa",
         'K' : 3,
         'output' : "",
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]
   o = test[ 'output' ]
   print( arrange1( i, k ) )
   print( arrange2( i, k ) )
