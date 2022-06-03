#!/usr/bin/env python
#
# Find the Corrupt Pair (easy)
#
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to
# ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a
# data error, one of the numbers got duplicated which also resulted in one number
# going missing. Find both these numbers.

def sort( arr ):
   size = len( arr )

   for i in range( size ):
      while arr[ i ] != i + 1 and arr[ arr[ i ] - 1 ] != arr[ i ]:
         tmp = arr[ i ]
         arr[ i ], arr[ tmp - 1 ] = arr[ tmp - 1 ], arr[ i ]

   for i in range( size ):
      if arr[ i ] != i + 1:
         return [ arr[ i ], i + 1 ]

   return [ -1, -1 ]

testCases = [
      {
         'input' : [3, 1, 2, 5, 2],
         'output' : [2, 4],
      },
      {
         'input' : [3, 1, 2, 3, 6, 4],
         'output' : [3, 5],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   print( sort( i ) )
