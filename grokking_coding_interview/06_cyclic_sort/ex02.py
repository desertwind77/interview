#!/usr/bin/env python
#
# Find the Missing Number (easy)
#
# We are given an array containing n distinct numbers taken from the range 0 to n.
# Since the array has only n numbers out of the total n+1 numbers, find the missing
# number.

def sort( arr ):
   # index : 0 1 2 3
   # array : 4 0 3 1
   # 0       4 0 3 1
   # 1       0 4 3 1
   # 2       0 4 1 3
   #         0 1 4 3
   size = len( arr )
   for i in range( size ):
      while i < size and arr[ i ] < size and arr[ i ] != i:
         tmp = arr[ i ]
         arr[ i ], arr[ tmp ] = arr[ tmp ], arr[ i ]

   for i in range( size ):
      if arr[ i ] != i:
         return i
   return size

testCases = [
      {
         'input' : [2, 0, 3, 1],
         'output' : 4,
      },
      {
         'input' : [4, 0, 3, 1],
         'output' : 2,
      },
      {
         'input' : [8, 3, 5, 2, 4, 6, 0, 1],
         'output' : 7,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( sort( i ) == o )
