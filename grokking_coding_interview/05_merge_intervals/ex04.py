#!/usr/bin/env python
# Conflicting Appointments (medium)
#
# Given an array of intervals representing ‘N’ appointments, find out if a person can
# attend all the appointments.

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

def canAttend( apps ):
   if len( apps ) < 2:
      return True

   apps = [ Interval( i[ 0 ], i[ 1 ] ) for i in apps ]
   apps.sort( key=lambda x: x.start )

   prev = apps[ 0 ]
   for i in range( 1, len( apps ) ):
      cur = apps[ i ]
      if isOverlapping( prev, cur ):
         return False
      prev = cur

   return True

testCases = [
      {
         'appointments' : [[1,4], [2,5], [7,9]],
         'output' : False,
      },
      {
         'appointments' : [[6,7], [2,4], [8,12]],
         'output' : True,
      },
      {
         'appointments' : [[4,5], [2,3], [3,6]],
         'output' : False,
      },
]

for test in testCases:
   a = test[ 'appointments' ]
   o = test[ 'output' ]
   assert( canAttend( a ) == o )
