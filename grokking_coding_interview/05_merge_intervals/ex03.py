#!/usr/bin/env python
# Intervals Intersection (medium)
#
# Given two lists of intervals, find the intersection of these two lists. Each list
# consists of disjoint intervals sorted on their start time.

class Interval:
   def __init__( self, start, end ):
      self.start = start
      self.end = end

   def __repr__( self ):
      return "[" + str( self.start ) + ", " + str( self.end ) + "]"

def isOverlapped( a, b ):
   if a.start > b.start:
      a, b = b, a
   # a.start <= b.start
   return b.start <= a.end

def intersect( a, b ):
   if not isOverlapped( a, b ):
      return None
   return Interval( max( a.start, b.start ), min( a.end, b.end ) )

def findIntersects( arr1, arr2 ):
   arr1 = [ Interval( i[ 0 ], i[ 1 ] ) for i in arr1 ]
   arr2 = [ Interval( i[ 0 ], i[ 1 ] ) for i in arr2 ]
   arr1.sort( key=lambda x: x.start )
   arr2.sort( key=lambda x: x.start )

   result = []
   i1 = i2 = 0
   while i1 < len( arr1 ) and i2 < len( arr2 ):
      a1, a2 = arr1[ i1 ], arr2[ i2 ]
      if isOverlapped( a1, a2 ):
         result.append( intersect( a1, a2 ) )

      if a1.end == a2.end:
         i1 += 1
         i2 += 1
      elif a1.end < a2.end:
         i1 += 1
      else:
         i2 += 1

   result = [ [ i.start, i.end ] for i in result ]
   return result

testCases = [
      {
         'arr1' : [[1, 3], [5, 6], [7, 9]],
         'arr2' : [[2, 3], [5, 7]],
         'output' : [ [2, 3], [5, 6], [7, 7] ],
      },
      {
         'arr1' : [[1, 3], [5, 7], [9, 12]],
         'arr2' : [[5, 10]],
         'output' : [ [5, 7], [9, 10] ],
      },
]

for test in testCases:
   a1 = test[ 'arr1' ]
   a2 = test[ 'arr2' ]
   o = test[ 'output' ]
   assert( findIntersects( a1, a2 ) == o )
