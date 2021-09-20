#!/usr/bin/env python3
import math

class Heap:
   # MinHeap
   def __init__( self, arr ):
      self.heap = arr 

   '''
   def parent( self, cur ):
      return ceil( ( cur - 1 ) / 2 )

   def leftChild( self, cur ):
      return 2 * cur + 1

   def rightChild( self, cur ):
      return 2 * cur + 2

   def maxHeapify( self, size, index ):
      pass

   def insert( self, n ):
      self.data.append( n )
      size = len( self.data )

      cur = size - 1
      parent = self.parent( cur )
      while cur != 0:
         if self.data[ cur ] < self.data[ parent ]:
            self.data[ cur ], self.data[ parent ] = \
                  self.data[ parent ], self.data[ cur ]

   def delete( self ):
      pass
   '''

   def buildMaxHeap( self ):
      size = len( self.heap )
      for i in range( math.ceil( size / 2 ) - 1, -1, -1 ):
         self.maxHeapify( i, size )

   def maxHeapify( self, cur, size  ):
      left = 2 * cur + 1
      right = 2 * cur + 2

      largest = cur
      if left < size and self.heap[ cur ] < self.heap[ left ]:
         largest = left
      if right < size and self.heap[ largest ] < self.heap[ right ]:
         largest = right

      if largest != cur:
         self.heap[ cur ], self.heap[ largest ] = \
               self.heap[ largest ], self.heap[ cur ]
         self.maxHeapify( largest, size )

   def sort( self ):
      # Build a max heap
      self.buildMaxHeap()

      size = len( self.heap )
      for i in range( size - 1, 0, -1 ):
         # The root of the max heap is the largest element in the array.
         # Keep placing it toward the end of the array.
         self.heap[ 0 ], self.heap[ i ] = \
               self.heap[ i ], self.heap[ 0 ]
         self.maxHeapify( 0, i )

      return self.heap

if __name__ == '__main__':
   testCases = [
         [ 12, 11, 13, 5, 6, 7 ],
         [ 518, 446, 909, 464, 212, 735, 681, 738, 344, 546, 150, 516, 642,
           190, 797, 753, 732, 529, 576, 396, 376, 606, 614, 662, 777, 678, 248,
           133, 384, 11, 456 ],
   ]

   for test in testCases:
      heap = Heap( test.copy() )
      assert( sorted( test ) == heap.sort() )
