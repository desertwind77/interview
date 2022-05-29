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
   # k:3
   # i   maxHeap     cpu   queue       maxHeap
   # 0   a:-2,b:-1   a     [a:-1]      b:-1
   # 1   b:-1        ab    [a:-1]      {}
   # 2   {}          abI   [a:-1]      {}
   # 3   {}          abII  [a:-1]      {}
   # 0   a:-1        abIIa []          {}
   # 1   {}          abIIa []
   while maxHeap:
      for _ in range( k + 1 ):
         if maxHeap:
            # running a task
            negFreq, ch = heappop( maxHeap )
            if negFreq < 0:
               cpu += 1

            negFreq += 1
            if negFreq < 0:
               queue.append( ( negFreq, ch ) )
         elif queue:
            cpu += 1

      while queue:
         negFreq, ch = queue.popleft()
         if negFreq < 0:
            heappush( maxHeap, ( negFreq, ch ) )

   return cpu

testCases = [
      # a -> c -> b -> a -> c -> idle -> a
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
