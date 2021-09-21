#!/usr/bin/env python3

def selection_sort( array ):
   size = len( array )

   for i in range( 0, size - 1):
      minIndex = i
      for j in range( i + 1, size ):
         # For each i, select the smallest element between the index
         # i and ( size - 1 ) and put it at the index i.
         if array[ j ] < array[ minIndex ]:
            minIndex = j
      if minIndex != i:
         array[ i ], array[ minIndex ] = array[ minIndex ], array[ i ]

   return array

if __name__ == '__main__':
   testCases = [
         [ 12, 11, 13, 5, 6, 7 ],
         [ 518, 446, 909, 464, 212, 735, 681, 738, 344, 546, 150, 516, 642,
           190, 797, 753, 732, 529, 576, 396, 376, 606, 614, 662, 777, 678, 248,
           133, 384, 11, 456 ],
   ]

   for test in testCases:
      assert( sorted( test ) == selection_sort( test.copy() ) )
