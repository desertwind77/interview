#!/usr/bin/env python
#
# Find all Duplicate Numbers (easy)
#
# We are given an unsorted array containing n numbers taken from the range 1 to n.
# The array has some numbers appearing twice, find all these duplicate numbers using
# constant space.

def sort( arr ):
   size = len( arr )

   # index : 0 1 2 3 4
   # array : 3 4 4 5 5
   # 0       4 4 3 5 5
   #         5 4 3 4 5
   # 1       5 4 3 4 5
   # 2       5 4 3 4 5
   # 3       5 4 3 4 5
   # 4       5 4 3 4 5
   for i in range( size ):
      while arr[ i ] != i + 1 and arr[ arr[ i ] - 1 ] != arr[ i ]:
         tmp = arr[ i ]
         arr[ i ], arr[ tmp - 1 ] = arr[ tmp - 1 ], arr[ i ]

   result = []
   for i in range( size ):
      if arr [ i ] != i + 1:
         result.append( arr[ i ] )
   return result

testCases = [
      {
         'input' : [3, 4, 4, 5, 5],
         'output' : [4, 5],
      },
      {
         'input' : [5, 4, 7, 2, 3, 5, 3],
         'output' : [3, 5],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( sorted( sort( i ) ) == o )
