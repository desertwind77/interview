#!/usr/bin/env python
# Merge Intervals (medium)
#
# Given a list of intervals, merge all the overlapping intervals to produce a list
# that has only mutually exclusive intervals.

class Interval:
   def __init__( self, start, end ):
      self.start = start
      self.end = end
   def __repr__( self ):
      return "[" + str( self.start ) + ", " + str( self.end ) + "]"

def merge( intervals ):
   if len( intervals ) < 2:
      return intervals

   intervals = [ Interval( i[ 0 ], i[ 1 ] ) for i in intervals ]

   intervals.sort( key=lambda x : x. start )

   merged = []
   prev = intervals[ 0 ]
   for i in range( 1, len( intervals ) ):
      cur = intervals[ i ]

      if cur.start < prev.end:
         prev = Interval( prev.start, max( prev.end, cur.end ) )
      else:
         merged.append( prev )
         prev = cur
   merged.append ( prev )

   return merged

testCases = [
      {
         'intervals' : [[1,4], [2,5], [7,9]],
         'output' : [[1,5], [7,9]],
      },
      {
         'intervals' : [[6,7], [2,4], [5,9]],
         'output' : [[2,4], [5,9]],
      },
      {
         'intervals' : [[1,4], [2,6], [3,5]],
         'output' : [[1,6]],
      },
]

for test in testCases:
   i = test[ 'intervals' ]
   o = test[ 'output' ]
   print( merge( i ) )
