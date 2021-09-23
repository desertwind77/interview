#!/usr/bin/env python3
import math
import sys

class MinHeap:
   '''
   Binary min heap
   '''

   def __init__( self ):
      self.array = []

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
      return self.array[ 0 ]

   def heapify( self, index ):
      size = len( self.array )
      left = self.left( index )
      right = self.right( index )
      smallest = index

      if left < size and self.array[ smallest ] > self.array[ left ]:
         smallest = left
      if right < size and self.array[ smallest ] > self.array[ right ]:
         smallest = right
      if smallest != index:
         self.array[ smallest ], self.array[ index ] = \
               self.array[ index ], self.array[ smallest ]
         self.heapify( smallest )

   def extractMin( self ):
      root = self.array[ 0 ]
      lastIndex = len( self.array ) - 1
      self.array[ 0 ] = self.array[ lastIndex ]
      self.array.pop()
      self.heapify( 0 )
      return root

   def decreaseKey( self, index, newVal ):
      self.array[ index ] = newVal
      self.populateUpward( index )

   def deleteKey( self, index ):
      self.decreaseKey( index, -1 * sys.maxsize - 1 )
      self.extractMin()

   def insertKey( self, key ):
      self.array.append( key )
      index = len( self.array ) - 1
      self.populateUpward( index )

   def populateUpward( self, index ):
      curIndex = index
      parentIndex = self.parent( curIndex )
      while curIndex != 0 and self.array[ curIndex ] < self.array[ parentIndex ]:
         self.array[ curIndex ], self.array[ parentIndex ] = \
            self.array[ parentIndex], self.array[ curIndex]
         curIndex = parentIndex
         parentIndex = self.parent( curIndex )

   def print( self ):
      print( self.array )

if __name__ == '__main__':
   array = [ 3, 2, 1, 15, 5, 4, 45 ]

   minHeap = MinHeap()
   for a in array:
      minHeap.insertKey( a )
   assert( minHeap.array == [ 1, 3, 2, 15, 5, 4, 45 ] )

   minHeap.deleteKey( 1 )
   assert( minHeap.array == [ 1, 5, 2, 15, 45, 4 ] )

   minHeap.decreaseKey( 4, 3 )
   assert( minHeap.array == [ 1, 3, 2, 15, 5, 4 ] )

   assert( minHeap.extractMin() == 1 )
   assert( minHeap.getMin() == 2 )
   assert( minHeap.array == [ 2, 3, 4, 15, 5] )
