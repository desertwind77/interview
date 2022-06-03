#!/usr/bin/env python
#
# Find the Smallest Missing Positive Number (medium)
#
# Given an unsorted array containing numbers, find the smallest missing positive
# number in it.
#
# Note: Positive numbers start from '1'.

def sort( arr ):
   size = len( arr )
   for i in range( size ):
      while arr[ i ] >= 0 and arr[ i ] != i and arr[ i ] < size and arr[ arr[ i ] ] != arr[ i ]:
         tmp = arr[ i ]
         arr[ i ], arr[ tmp ] = arr[ tmp ], arr[ i ]

   for i in range( 1, size ):
      if arr[ i ] != i:
         return i
   return size

testCases = [
      # index :  0 1 2 3 4
      # array : -3 1 5 4 2
      # 0       -3 1 5 4 2
      # 1       -3 1 5 4 2
      # 2       -3 1 5 4 2
      # 3       -3 1 5 2 4
      #         -3 1 2 5 4
      {
         'input' : [-3, 1, 5, 4, 2],
         'output' : 3,
      },
      # index : 0  1  2 3  4
      # array : 3 -2  0 1  2
      # 0       1 -2  0 3  2
      #        -2  1  0 3  2
      # 1      -2  1  0 3  2
      # 2       0  1 -2 3  2
      # 3       0  1 -2 3  2
      # 4       0  1  2 3 -2
      {
         'input' : [3, -2, 0, 1, 2],
         'output' : 4,
      },
      # index : 0 1 2 3
      # array : 3 2 5 1
      # 0       1 2 5 3
      #         2 1 5 3
      #         5 1 2 3
      # ...
      {
         'input' : [3, 2, 5, 1],
         'output' : 4,
      },
      # index : 0   1   2
      # array : 33  37  5
      # 0       33  37  5
      # 1       33  37  5
      # 2       33  37  5
      {
         'input' : [33, 37, 5],
         'output' : 1,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( sort( i ) == o )
