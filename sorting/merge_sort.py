#!/usr/bin/env python3
import math

def merge( array, left, right ):
   i = j = k = 0 
   while i < len( array ):
      if not ( j < len( left ) and k < len( right ) ):
         break
      if left[ j ] <= right[ k ]:
         array[ i ] = left[ j ]
         j += 1
      else:
         array[ i ] = right[ k ]
         k += 1
      i += 1

   while i < len( array ):
      if j < len( left ):
         array[ i ] = left[ j ]
         j += 1
      elif k < len( right ):
         array[ i ] = right[ k ]
         k += 1
      i += 1

def merge_sort( array ):
   size = len( array )
   if size <= 1:
      return array

   mid = math.ceil( ( size - 1 ) / 2 )
   left = merge_sort( array[ 0 : mid ] )
   right = merge_sort( array[ mid : ] )
   merge( array, left, right )

   return array

if __name__ == '__main__':
   testCases = [
         [ 12, 11, 13, 5, 6, 7 ],
         [ 518, 446, 909, 464, 212, 735, 681, 738, 344, 546, 150, 516, 642,
           190, 797, 753, 732, 529, 576, 396, 376, 606, 614, 662, 777, 678, 248,
           133, 384, 11, 456 ],
   ]

   for test in testCases:
      assert( sorted( test ) == merge_sort( test.copy() ) )
