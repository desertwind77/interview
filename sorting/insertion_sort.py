#!/usr/bin/env python3

def insertion_sort( array ):
   # Divide the array into two parts: sorted and unsorted.
   # Initially, only the index 0 is sorted.
   # Gradually include more elements at subsequent indices
   size = len( array )

   for i in range( 1, size ):
      # i represents the unsorted part, starting from 1 to size - 1
      for j in range( 0, i ):
         # j represents the sorted part, starting from 0 to i - 1
         if array[ j ] > array[ i ]:
            # tmp = array[ i ]
            # move elements from array[ j : i - 1 ] to array[ j + 1 : i ]
            # array[ j ] = tmp
            tmp = array[ i ]
            for k in range( i - 1, j - 1, - 1 ):
               array[ k + 1 ] = array[ k ]
            array[ j ] = tmp

   return array

if __name__ == '__main__':
   testCases = [
         [ 12, 11, 13, 5, 6, 7 ],
         [ 518, 446, 909, 464, 212, 735, 681, 738, 344, 546, 150, 516, 642,
           190, 797, 753, 732, 529, 576, 396, 376, 606, 614, 662, 777, 678, 248,
           133, 384, 11, 456 ],
   ]

   for test in testCases:
      assert( sorted( test ) == insertion_sort( test.copy() ) )

