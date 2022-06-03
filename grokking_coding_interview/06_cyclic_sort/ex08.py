#!/usr/bin/env python
#
# Find the First K Missing Positive Numbers (hard)
#
# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’
# missing positive numbers in the array.

def sort( arr, k ):
   size = len( arr )

   for i in range( size ):
      while arr[ i ] > 0 and arr[ i ] < size and \
            arr[ i ] != i and arr[ arr[ i ] ] != arr[ i ]:
         tmp = arr[ i ]
         arr[ i ], arr[ tmp ] = arr[ tmp ], arr[ i ]

   cache = set()
   for i in range( size ):
      if arr[ i ] >= size:
         cache.add( arr[ i ] )

   result = []
   for i in range( 1, size ):
      if arr[ i ] != i:
         result.append( i )

      if len( result ) >= k:
         break

   # 0  1  2  3  4  5
   # 6 -1 -1 -1 -1 -1
   count = size
   while len( result ) < k:
      if count not in cache:
         result.append( count )
      count += 1

   return result

testCases = [
      {
         # index :  0   1  2  3  4
         # array :  3  -1  4  5  5
         # 0        5  -1  4  3  5
         # 1        5  -1  4  3  5
         # 2        5  -1  5  3  4
         'input' : [3, -1, 4, 5, 5],
         'k' : 3,
         'output' : [1, 2, 6],
      },
      {
         'input' : [2, 3, 4],
         'k' : 3,
         'output' : [1, 5, 6],
      },
      {
         'input' : [-2, -3, 4],
         'k' : 2,
         'output' : [1, 2],
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'k' ]
   o = test[ 'output' ]
   assert( sort( i, k ) == o )
