#!/usr/bin/env python
# Minimum Meeting Rooms (hard)
#
# Given a list of intervals representing the start and end time of ‘N’ meetings, find
# the minimum number of rooms required to hold all the meetings.

from collections import deque

class Interval:
   def __init__( self, start, end ):
      self.start = start
      self.end = end

   def __repr__( self ):
      return "[" + str( self.start ) + ", " + str( self.end ) + "]"

def isOverlapping( a, b ):
   if a.start > b.start:
      a, b = b, a
   return b.start < a.end

def minMeetingRooms( meetings ):
   if not meetings:
      return 0

   meetings = [ Interval( m[ 0 ], m[ 1 ] ) for m in meetings ]
   meetings.sort( key=lambda x: x.start )
   meetings = deque( meetings )

   rooms = [ [ meetings.popleft() ] ]
   while meetings:
      cur = meetings.popleft()

      scheduled = False
      for i in range( len( rooms ) ):
         curRoom = rooms[ i ]
         if not isOverlapping( curRoom[ -1 ], cur ):
            curRoom.append( cur )
            scheduled = True

      if not scheduled:
         rooms.append( [ cur ] )

   return len( rooms )

testCases = [
      {
         'meetings' : [[1,4], [2,5], [7,9]],
         'output' : 2,
      },
      {
         'meetings' : [[6,7], [2,4], [8,12]],
         'output' : 1,
      },
      {
         'meetings' : [[1,4], [2,3], [3,6]],
         'output' : 2,
      },
      {
         'meetings' : [[4,5], [2,3], [2,4], [3,5]],
         'output' : 2,
      },
]

for test in testCases:
   m = test[ 'meetings' ]
   o = test[ 'output' ]
   assert( minMeetingRooms( m ) == o )
