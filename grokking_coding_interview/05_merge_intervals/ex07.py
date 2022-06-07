#!/usr/bin/env python
# Employee Free Time (hard)
#
# For ‘K’ employees, we are given a list of intervals representing each employee’s
# working hours. Our goal is to determine if there is a free interval which is common
# to all employees. You can assume that each list of employee working hours is sorted
# on the start time.

class Interval:
   def __init__( self, start, end ):
      self.start = start
      self.end = end

   def __repr__( self ):
      return "[" + str( self.start ) + ", " + str( self.end ) + "]"

def isOverlapping( a, b ):
   if a.start > b.start:
      a, b = b, a
   return b.start <= a.end

def freeTimes( hours ):
   allHours = []
   for employee in hours:
      allHours += employee

   allHours = [ Interval( a[ 0 ], a[ 1 ] ) for a in allHours ]
   allHours.sort( key=lambda x: x.start )

   merged = []
   prev = allHours[ 0 ]
   for i in range( 1, len( allHours ) ):
      cur = allHours[ i ]
      if isOverlapping( prev, cur ):
         prev = Interval( prev.start, max( prev.end, cur.end ) )
      else:
         merged.append( prev )
         prev = cur
   merged.append( prev )

   prev = merged[ 0 ]
   result = []
   for i in range( 1, len( merged ) ):
      cur = merged[ i ]
      result.append( [ prev.end, cur.start ] )
      prev = cur

   return result

testCases = [
      {
         'hours' : [ [ [1,3], [5,6] ], [ [2,3], [6,8] ] ],
         'output' : [ [3,5] ],
      },
      {
         'hours' : [ [ [1,3], [9,12] ], [ [2,4]], [[6,8] ] ],
         'output' : [ [4,6], [8,9] ],
      },
      {
         'hours' : [ [ [1,3] ], [ [2,4] ], [ [3,5], [7,9] ] ],
         'output' : [ [5,7] ],
      },
]

for test in testCases:
   h = test[ 'hours' ]
   o = test[ 'output' ]
   assert( freeTimes( h ) == o )
