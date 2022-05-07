#!/usr/bin/env python
# Given a binary matrix representing an image, we want
# to flip the image horizontally, then invert it.
#
# To flip an image horizontally means that each row of
# the image is reversed. For example, flipping [0, 1, 1]
# horizontally results in [1, 1, 0].
#
# To invert an image means that each 0 is replaced by 1,
# and each 1 is replaced by 0. For example, inverting
# [1, 1, 0] results in [0, 0, 1].

def flipAndInvertMatrix( matrix ):
   for row in matrix:
      col = len( row )
      # Note : need to use ( col + 1 ) / 2
      for i in range( int( ( col + 1 )/ 2 ) ):
         row[ i ], row[ col - i - 1 ] = row[ col - i - 1 ] ^ 1, row[ i ] ^ 1
   return matrix

testCases = [
      {
         'input' : [
            [1,0,1],
            [1,1,1],
            [0,1,1]
         ],
         'output' : [
            [0,1,0],
            [0,0,0],
            [0,0,1]
         ]
      },
      {
         'input' : [
            [1,1,0,0],
            [1,0,0,1],
            [0,1,1,1],
            [1,0,1,0]
         ],
         'output' : [
            [1,1,0,0],
            [0,1,1,0],
            [0,0,0,1],
            [1,0,1,0]
         ]
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( flipAndInvertMatrix( i ) == o )

