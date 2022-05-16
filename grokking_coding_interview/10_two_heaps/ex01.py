#!/usr/bin/env python
# Design a class to calculate the median of a number stream. The class should have
# the following two methods:
#
# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
#
# If the count of numbers inserted in the class is even, the median will be the
# average of the middle two numbers.

from heapq import *

class Mediam:
   def __init__( self ):
      self.maxHeap = []
      self.minHeap = []

   def insertNum( self, n ):
      if not self.maxHeap or -n >= self.maxHeap[ 0 ]:
         heappush( self.maxHeap, -1 * n )
      else:
         heappush( self.minHeap, n )

      if len( self.maxHeap ) - len( self.minHeap ) > 1:
         top = -1 * heappop( self.maxHeap )
         heappush( self.minHeap, top )
      elif len( self.maxHeap ) < len( self.minHeap ):
         top = heappop( self.minHeap )
         heappush( self.maxHeap, -1 * top )
      print( self.maxHeap, self.minHeap )

   def findMedian( self ):
      if not self.maxHeap:
         return None
      elif len( self.maxHeap ) == len( self.minHeap ):
         topL = -1 * self.maxHeap[ 0 ]
         topR = self.minHeap[ 0 ]
         return ( topL + topR ) * 1.0 / 2
      return self.maxHeap[ 0 ] * -1

test = Mediam()
print( test.findMedian() )

test.insertNum( 3 )
test.insertNum( 1 )
print( test.findMedian() )

test.insertNum( 5 )
print( test.findMedian() )

test.insertNum( 4 )
print( test.findMedian() )

test.insertNum( 7 )
print( test.findMedian() )

test.insertNum( 9 )
print( test.findMedian() )
