#!/usr/bin/env python
#
# Find the Duplicate Number (easy)
#
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to
# ‘n’. The array has only one duplicate but it can be repeated multiple times. Find
# that duplicate number without using any extra space. You are, however, allowed to
# modify the input array.

def sort( arr ):
   size = len( arr )

   # index : 0 1 2 3 4
   # array : 1 4 4 3 2
   # 0       1 4 4 3 2
   # 1       1 3 4 4 2
   #         1 4 3 4 2
   # 2       1 4 3 4 2
   # 3       1 4 3 4 2
   # 4       1 2 3 4 4
   for i in range( size ):
      while arr[ i ] != i + 1 and arr[ arr[ i ] - 1 ] != arr[ i ]:
         tmp = arr[ i ]
         arr[ i ], arr[ tmp - 1 ] = arr[ tmp - 1 ], arr[ i ]

   for i in range( size ):
      if arr[ i ] != i + 1:
         return arr[ i ]

testCases = [
      {
         'input' : [1, 4, 4, 3, 2],
         'output' : 4,
      },
      {
         'input' : [2, 1, 3, 3, 5, 4],
         'output' : 3,
      },
      {
         'input' : [2, 4, 1, 4, 4],
         'output' : 4,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   print( sort( i ) )
