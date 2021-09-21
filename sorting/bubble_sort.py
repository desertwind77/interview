#!/usr/bin/env python3

def bubble_sort( array ):
   size = len( array )

   for i in range( 0, size - 1 ):
      # For each round i, put the largest element at the index ( size - i - 1 )
      for j in range( 0, size - i - 1 ):
         if array[ j ] > array[ j + 1 ]:
            array[ j ], array[ j + 1 ] = array[ j + 1 ], array[ j ]

   return array

if __name__ == '__main__':
   testCases = [
         [ 12, 11, 13, 5, 6, 7 ],
         [ 518, 446, 909, 464, 212, 735, 681, 738, 344, 546, 150, 516, 642,
           190, 797, 753, 732, 529, 576, 396, 376, 606, 614, 662, 777, 678, 248,
           133, 384, 11, 456 ],
   ]

   for test in testCases:
      assert( sorted( test ) == bubble_sort( test.copy() ) )
