#!/usr/bin/env python3

def partition( array, start, end ):
   if start == end:
      return start

   pivot = array[ end ]

   pi = start
   for i in range( start, end ):
      if array[ i ] < pivot:
         array[ i ], array[ pi ] = array[ pi ], array[ i ]
         pi += 1
   array[ pi ], array[ end ] = array[ end ], array[ pi ]
   return pi

def quick_sort( array, start=None, end=None ):
   start = 0 if start == None else start
   end = len( array ) - 1 if end == None else end

   if start >= end:
      return

   pi = partition( array, start, end )
   quick_sort( array, start, pi - 1 )
   quick_sort( array, pi + 1, end )

   return array

if __name__ == '__main__':
   testCases = [
         [ 12, 11, 13, 5, 6, 7 ],
         [ 518, 446, 909, 464, 212, 735, 681, 738, 344, 546, 150, 516, 642,
           190, 797, 753, 732, 529, 576, 396, 376, 606, 614, 662, 777, 678, 248,
           133, 384, 11, 456 ],
   ]

   for test in testCases:
      assert( sorted( test ) == quick_sort( test.copy() ) )

