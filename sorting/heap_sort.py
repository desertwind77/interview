#!/usr/bin/env python3
import math
# We need to use math.ceil because in python3, 3/2 is 1.5 and int( 1.5 ) is 1.

def heapify( array, cur, size, ascending ):
   def compare( a, b, ascending ):
      if ascending:
         return a <= b
      return a > b

   left = 2 * cur + 1
   right = 2 * cur + 2

   largest = cur
   if left < size and compare( array[ cur ], array[ left ], ascending ):
      largest = left
   if right < size and compare( array[ largest ], array[ right ], ascending ):
      largest = right

   if largest != cur:
      array[ cur ], array[ largest ] = array[ largest ], array[ cur ]
      heapify( array, largest, size, ascending )

def buildHeap( array, ascending ):
   size = len( array )
   for i in range( math.ceil( size / 2 ) - 1, -1, -1 ):
      heapify( array, i, size, ascending )

def heap_sort( array, ascending=True ):
   # For sorting in ascending order, we need to build a max heap.
   # For sorting in descending order, we need to build a min heap.
   # Note that a heap is not a sorted array
   buildHeap( array, ascending )

   size = len( array )
   for i in range( size - 1, 0, -1 ):
      # The root of the max heap is the largest element in the array.
      # Keep placing it toward the end of the array.
      array[ 0 ], array[ i ] = array[ i ], array[ 0 ]
      heapify( array, 0, i, ascending )

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
      assert( sorted(test)[::-1] == heap_sort( test.copy(), ascending=False ) )
