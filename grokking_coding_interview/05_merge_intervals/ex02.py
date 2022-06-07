#!/usr/bin/env python
# Insert Interval (medium)
#
# Given a list of non-overlapping intervals sorted by their start time, insert a
# given interval at the correct position and merge all necessary intervals to produce
# a list that has only mutually exclusive intervals.

class Interval:
   def __init__( self, start, end ):
      self.start = start
      self.end = end

   def __repr__( self ):
      return "[" + str( self.start ) + ", " + str( self.end ) + "]"

def merge( old, new ):
   def isOverlapped( a, b ):
      if a.start > b.start:
         a, b = b, a

      # a.start is less than b.start
      if b.start >= a.start and b.start <= a.end:
         return True

      return False

   old = [ Interval( i[ 0 ], i[ 1 ] ) for i in old ]
   old.sort( key=lambda x: x.start )
   new = Interval( new[ 0 ], new[ 1 ] )

   mergedList = []

   for i in range( len( old ) ):
      cur = old[ i ]
      if cur.end < new.start:
         # Skipping all non-overlapping intervals at the beginning of the list
         mergedList.append( cur )
      else:
         if isOverlapped( cur, new ):
            new = Interval( min( cur.start, new.start ), max( cur.end, new.end ) )
         else:
            mergedList += old[ i: ]
            break
   mergedList.append( new )

   mergedList.sort( key=lambda x: x.start )
   mergedList = [ [ i.start, i.end ] for i in mergedList ]

   return mergedList

testCases = [
      {
         'old' : [[1,3], [5,7], [8,12]],
         'new' : [4,6],
         'output' : [[1,3], [4,7], [8,12]],
      },
      {
         'old' : [[1,3], [5,7], [8,12]],
         'new' : [4,10],
         'output' : [[1,3], [4,12]],

      },
      {
         'old' : [[2,3],[5,7]],
         'new' : [1,4],
         'output' : [[1,4], [5,7]],
      },
]

for test in testCases:
   old = test[ 'old' ]
   new = test[ 'new' ]
   o = test[ 'output' ]
   result = merge( old, new )
   assert( o == result )
