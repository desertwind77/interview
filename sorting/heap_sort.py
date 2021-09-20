#!/usr/bin/env python3
import math

def maxHeapify( array, cur, size  ):
   left = 2 * cur + 1
   right = 2 * cur + 2

   largest = cur
   if left < size and array[ cur ] < array[ left ]:
      largest = left
   if right < size and array[ largest ] < array[ right ]:
      largest = right

   if largest != cur:
      array[ cur ], array[ largest ] = array[ largest ], array[ cur ]
      maxHeapify( array, largest, size )

def buildMaxHeap( array ):
   size = len( array )
   for i in range( math.ceil( size / 2 ) - 1, -1, -1 ):
      maxHeapify( array, i, size )

def heap_sort( array ):
   # Build a max heap. Note that a heap is not a sorted array
   buildMaxHeap( array )

   size = len( array )
   for i in range( size - 1, 0, -1 ):
      # The root of the max heap is the largest element in the array.
      # Keep placing it toward the end of the array.
      array[ 0 ], array[ i ] = array[ i ], array[ 0 ]
      maxHeapify( array, 0, i )

   # Though heap sort is an in-place sort, we still return the sorted array
   # so that the API is compatible with other sorting algorithm.
   return array

if __name__ == '__main__':
   testCases = [
         [ 12, 11, 13, 5, 6, 7 ],
         [ 518, 446, 909, 464, 212, 735, 681, 738, 344, 546, 150, 516, 642,
           190, 797, 753, 732, 529, 576, 396, 376, 606, 614, 662, 777, 678, 248,
           133, 384, 11, 456 ],
   ]

   for test in testCases:
      assert( sorted( test ) == heap_sort( test.copy() ) )
