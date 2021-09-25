#!/usr/bin/env python3
import math
import sys

class MinHeap:
   '''
   Binary min heap
   '''

   def __init__( self ):
      self.heap = []

   def parent( self, index ):
      # Return the index of the parent
      return math.floor( ( index - 1 ) / 2 )

   def left( self, index ):
      # Return the index of the left child
      return 2 * index + 1

   def right( self, index ):
      # Return the index of the right child
      return 2 * index + 2

   def getMin( self ):
      return self.heap[ 0 ]

   def heapify( self, index ):
      size = len( self.heap )
      left = self.left( index )
      right = self.right( index )
      smallest = index

      if left < size and self.heap[ smallest ] > self.heap[ left ]:
         smallest = left
      if right < size and self.heap[ smallest ] > self.heap[ right ]:
         smallest = right
      if smallest != index:
         self.heap[ smallest ], self.heap[ index ] = \
               self.heap[ index ], self.heap[ smallest ]
         self.heapify( smallest )

   def extractMin( self ):
      root = self.heap[ 0 ]
      lastIndex = len( self.heap ) - 1
      self.heap[ 0 ] = self.heap[ lastIndex ]
      self.heap.pop()
      self.heapify( 0 )
      return root

   def decreaseKey( self, index, newVal ):
      self.heap[ index ] = newVal
      self.populateUpward( index )

   def deleteKey( self, index ):
      self.decreaseKey( index, -1 * sys.maxsize - 1 )
      self.extractMin()

   def insertKey( self, key ):
      self.heap.append( key )
      index = len( self.heap ) - 1
      self.populateUpward( index )

   def populateUpward( self, index ):
      curIndex = index
      parentIndex = self.parent( curIndex )
      while curIndex != 0 and self.heap[ curIndex ] < self.heap[ parentIndex ]:
         self.heap[ curIndex ], self.heap[ parentIndex ] = \
            self.heap[ parentIndex], self.heap[ curIndex]
         curIndex = parentIndex
         parentIndex = self.parent( curIndex )

   def print( self ):
      print( self.heap )

if __name__ == '__main__':
   heap = [ 3, 2, 1, 15, 5, 4, 45 ]

   minHeap = MinHeap()
   for a in heap:
      minHeap.insertKey( a )
   assert( minHeap.heap == [ 1, 3, 2, 15, 5, 4, 45 ] )

   minHeap.deleteKey( 1 )
   assert( minHeap.heap == [ 1, 5, 2, 15, 45, 4 ] )

   minHeap.decreaseKey( 4, 3 )
   assert( minHeap.heap == [ 1, 3, 2, 15, 5, 4 ] )

   assert( minHeap.extractMin() == 1 )
   assert( minHeap.getMin() == 2 )
   assert( minHeap.heap == [ 2, 3, 4, 15, 5] )
