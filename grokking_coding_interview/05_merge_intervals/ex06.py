#!/usr/bin/env python
#
# Maximum CPU Load (hard)
#
# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load
# when it is running. Our goal is to find the maximum CPU load at any time if all the
# jobs are running on the same machine.
from heapq import *

class Job:
   def __init__( self, start, end, load ):
      self.start = start
      self.end = end
      self.load = load

   def __repr__( self ):
      return "[" + str( self.start ) + ", " + \
            str( self.end ) + ", " + \
            str( self.load ) + "]"

   def __lt__( self, other ):
      return self.start <= other.start

def maxLoad( jobs ):
   jobs = [ Job( j[ 0 ], j[ 1 ], j[ 2 ] ) for j in jobs ]
   jobs.sort( key=lambda x: x.start )
   minHeap = []
   maxLoad = 0
   curLoad = 0

   for j in jobs:
      while minHeap and minHeap[ 0 ].end <= j.start:
         top = heappop( minHeap )
         curLoad -= top.load
      heappush( minHeap, j )
      curLoad += j.load

      if curLoad > maxLoad:
         maxLoad = curLoad

   return maxLoad

testCases = [
      {
         'jobs' : [[1,4,3], [2,5,4], [7,9,6]],
         'output' : 7,
      },
      {
         'jobs' : [[6,7,10], [2,4,11], [8,12,15]],
         'output' : 15,
      },
      {
         'jobs' : [[1,4,2], [2,4,1], [3,6,5]],
         'output' : 8,
      },
]

for test in testCases:
   j = test[ 'jobs' ]
   o = test[ 'output' ]
   assert( maxLoad( j ) == o )
