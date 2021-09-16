#!/usr/bin/env python3
from collections import defaultdict

def optimized_matrix_multiplication( input ):
   length = len( input )
   cost = defaultdict( int )
   paren = defaultdict( str )
   result = {}
   for i in range( 0, length ):
      r = length - i - 1
      c = i
      result[ ( r, c ) ] = input[ i ]
      paren[ ( r, c ) ] = str( input[ i ] )

   for i in range( 1, length ):
      for j in range( length - i, 0, -1 ):
         # i     j
         # 1     4, 3, 2, 1      ( 4, 1 ), ( 3, 2 ), ( 2, 3 ), ( 1, 4 )
         # 2     3, 2, 1         ( 4, 2 ), ( 3, 3 ), ( 2, 4 )
         # 3     2, 1            ( 4, 3 ), ( 3, 4 )
         # 4     1               ( 4, 4 )
         r = i + j - 1
         c = length - j

         if ( cost[ ( r - 1, c ) ] == 0 ) and ( cost[ ( r, c - 1 ) ] == 0 ):
            ( x, y ) = result[ ( r - 1, c ) ]
            ( _, z ) = result[ ( r, c - 1 ) ]
            cost[ ( r, c ) ] = ( x * y * z )
            result[ ( r, c ) ] = ( x, z )
            paren[ ( r, c ) ] = \
                  "( %s * %s )" % ( paren[ ( r, c - 1 ) ], paren[ ( r - 1, c ) ] )
         else:
            ( x, y ) = result[ ( r - 1, c ) ]
            ( _, z ) = result[ ( length - c - 1, c ) ]
            ucost = cost[ ( r - 1, c ) ] + ( x * y * z )

            ( x, y ) = result[ ( r, c - 1 ) ]
            ( _, z ) = result[ ( r, length - r - 1 ) ]
            lcost = cost[ ( r, c - 1 ) ] + ( x * y * z )

            cost[ ( r, c ) ] = min( ucost, lcost )
            result[ ( r, c ) ] = ( x, z )
            if ucost < lcost:
               paren[ ( r, c ) ] = "( %s * %s )" % \
                     ( paren[ r, length - r - 1 ], paren[ ( r - 1, c ) ] )
            else:
               paren[ ( r, c ) ] = "( %s * %s )" % \
                     ( paren[ ( r, c - 1 ) ], paren[ length - c - 1, c ] )
   print( paren[ ( length - 1, length -1 ) ] )
   return cost[ ( length - 1, length - 1 ) ]

input = [ ( 10, 5 ), ( 5, 3 ), ( 3, 2 ), ( 2, 9 ), ( 9, 3 ) ]
res = optimized_matrix_multiplication( input )
print( 'cost of matrix multiplication = %d' % ( res ) )
