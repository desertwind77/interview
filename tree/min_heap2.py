#!/usr/bin/env python3

from heapq import heappush, heappop, heapify
from math import floor

# heappop  : pop and return the smallest element from the heap
# heappush : push the value item onto the heap, maintaining heap invarient
# heapify  : transform list into heap, in place, in linear time

class MinHeap:
   def __init__( self ):
      self.heap = []

   def parent( self, i ):
      return floor( ( i - 1 ) / 2 )

   def insertKey( self, key ):
      heappush( self.heap, key )

   def decreaseKey( self, index, newVal ):
      self.heap[ index ] = newVal

      while index != 0 and self.heap[ self.parent( index ) ] > self.heap[ index ]:
         self.heap[ index ], self.heap[ self.parent( index ) ] = \
               self.heap[ self.parent( index ) ], self.heap[ index ]

   def extractMin( self ):
      return heappop( self.heap )

   def deleteKey( self, index ):
      self.decreaseKey( index, float( "-inf" ) )
      self.extractMin()

   def getMin( self ):
      return self.heap[ 0 ]

if __name__ == '__main__':
   array = [ 3, 2, 1, 15, 5, 4, 45 ]

   minHeap = MinHeap()
   for a in array:
      minHeap.insertKey( a )
   assert( minHeap.heap == [ 1, 3, 2, 15, 5, 4, 45 ] )

   minHeap.deleteKey( 1 )
   assert( minHeap.heap == [ 1, 5, 2, 15, 45, 4 ] )

   minHeap.decreaseKey( 4, 3 )
   assert( minHeap.heap == [ 1, 3, 2, 15, 5, 4 ] )

   assert( minHeap.extractMin() == 1 )
   assert( minHeap.getMin() == 2 )
   assert( minHeap.heap == [ 2, 3, 4, 15, 5] )
