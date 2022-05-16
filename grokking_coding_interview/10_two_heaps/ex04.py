#!/usr/bin/env python
# Given an array of intervals, find the next interval of each interval. In a list of
# intervals, for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’
# greater than or equal to the ‘end’ of ‘i’.
#
# Write a function to return an array containing indices of the next interval of each
# input interval. If there is no next interval of a given interval, return -1. It is
# given that none of the intervals have the same start point.

from heapq import *

def nextIntervals( intervals ):
   maxHeapStart = []
   maxHeapEnd = []
   result = [ -1 ] * len( intervals )

   for i in range( len( intervals ) ):
      heappush( maxHeapStart, ( -intervals[ i ][ 0 ], i ) )
      heappush( maxHeapEnd, ( -intervals[ i ][ 1 ], i ) )

   while maxHeapEnd:
      end, index = heappop( maxHeapEnd )

      if -end > -maxHeapStart[ 0 ][ 0 ]:
         continue

      tmp = []
      while maxHeapStart and -maxHeapStart[ 0 ][ 0] >= -end:
         top = heappop( maxHeapStart )
         tmp.append( top )

      if tmp:
         _, nIndex = tmp[ -1 ]
         result[ index ] = nIndex

      for t in tmp:
         heappush( maxHeapStart, t )

   return result

class Interval:
   def __init__( self, start, end ):
      self.start = start
      self.end = end

def nextIntervals2( intervals ):
   n = len( intervals )
   maxStartHeap, maxEndHeap = [], []

   result = [ -1 for _ in range( n ) ]
   for i in range( n ):
      heappush( maxStartHeap, ( -intervals[ i ].start, i ) )
      heappush( maxEndHeap, ( -intervals[ i ].end, i ) )

   for _ in range( n ):
      topEnd, endIndex = heappop( maxEndHeap )
      if -maxStartHeap[ 0 ][ 0 ] >= -topEnd:
         topStart, startIndex = heappop( maxStartHeap )
         while maxStartHeap and -maxStartHeap[ 0 ][ 0 ] >= -topEnd:
            topStart, startIndex = heappop( maxStartHeap )

         result[ endIndex ] = startIndex

         heappush( maxStartHeap, ( topStart, startIndex ) )

   return result

testCases = [
      {
         'intervals' : [ [ 2, 3 ], [ 3, 4 ], [ 5, 6 ] ],
         'output' : [ 1, 2, -1 ],
      },
      {
         'intervals' : [ [ 3, 4 ], [ 1, 5 ], [ 4, 6 ] ],
         'output' : [ 2, -1, -1 ],
      }
]

for test in testCases:
   i = test[ 'intervals' ]
   o = test[ 'output' ]
   assert( nextIntervals( i ) == o )
   intervals = [ Interval( x[ 0 ], x[ 1 ] ) for x in i ]
   assert( nextIntervals2( intervals ) == o )
