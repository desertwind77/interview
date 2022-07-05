#!/usr/bin/env python
#
# Count of Subset Sum (hard)
#
# Given a set of positive numbers, find the total number of subsets whose sum is
# equal to a given number ‘S’.

def countSubsets( arr, s ):
   n = len( arr )

   dp = [ [ 0 for _ in range( s + 1 ) ] for _ in range( n ) ]

   for i in range( n ):
      dp[ i ][ 0 ] = 1
   dp[ 0 ][ arr[ 0 ] ] = 1

   for i in range( 1, n ):
      for j in range( 1, s + 1 ):
         dp[ i ][ j ] = dp[ i - 1 ][ j ] + dp[ i - 1 ][ j - arr[ i ] ]

   return dp[ n - 1 ][ s ]

testCases = [
      {
         'input' : [1, 1, 2, 3],
         'S' : 4,
         'output' : 3,
      },
      {
         'input' : [1, 2, 7, 1, 5],
         'S' : 9,
         'output' : 3,
      },
]

for test in testCases:
   i = test[ 'input' ]
   s = test[ 'S' ]
   o = test[ 'output' ]
   assert( countSubsets( i, s ) == o )
