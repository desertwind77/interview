#!/usr/bin/env python
# You are given a list of tasks that need to be run, in any order, on a server. Each
# task will take one CPU interval to execute but once a task has finished, it has a
# cooling period during which it can’t be run again. If the cooling period for all
# tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server
# needs to finish all tasks.
#
# If at any time the server can’t execute any task then it must stay idle.

from collections import defaultdict, deque
from heapq import *

def schedule( arr, k ):
   hashMap = defaultdict( int )
   for a in arr:
      hashMap[ a ] += 1

   maxHeap = []
   for ch, freq in hashMap.items():
      heappush( maxHeap, ( -freq, ch ) )

   queue = deque()
   cpu = 0
   sch = ''
   while maxHeap or queue:
      ch, freq = None, 0
      if maxHeap:
         freq, ch = heappop( maxHeap )
         cpu += 1
         sch += ch

      if queue:
         top = queue.popleft()
         if top:
            prevCh, prevFreq = top
            heappush( maxHeap, ( -prevFreq, prevCh ) )
         elif not ch:
            cpu += 1
            sch += 'N'

      if ch:
         freq = -freq
         freq -= 1
         if freq > 0:
            for _ in range( k - len( queue ) - 2 ):
               queue.append( None )
            queue.append( ( ch, freq ) )
   print( sch )

   return cpu

testCases = [
      # a -> c -> b -> a -> c -> idle -> a
      # a:3,c:2,b:1     a        [None,a:2]        c:2,b:1
      # c:2,b:1         ac       [a:2,c:1]         b:1
      # b:1             acb      [c:1]             a:2
      # a:2             acba     [N,a:1]           c:1
      # c:1             acbacN   [a:1]
      # {}              acbacN   []                a:1
      # a:1             acbacNa  []                {}
      {
         'input' : [ 'a', 'a', 'a', 'b', 'c', 'c' ],
         'K' : 2,
         'output' : 7,
      },
      # a -> b -> idle -> idle -> a
      {
         'input' : [ 'a', 'b', 'a' ],
         'K' : 3,
         'output' : 5,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]
   o = test[ 'output' ]
   print( schedule( i, k ) )
