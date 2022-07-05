#!/usr/bin/env python
#
# Target Sum (hard)
#
# You are given a set of positive numbers and a target sum ‘S’. Each number should be
# assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols
# to make the sum of the numbers equal to the target ‘S’.

def targetSum( arr, s ):
   n = len( arr )
   t = sum( arr )
   target = int( ( s + t ) / 2 )

   dp = [ [ 0 for _ in range( target + 1 ) ] for _ in range( n ) ]

   for i in range( n ):
      dp[ i ][ 0 ] = 1
   dp[ 0 ][ arr[ 0 ] ] = 1

   for i in range( 1, n ):
      for j in range( 1, target + 1 ):
         dp[ i ][ j ] = dp[ i - 1 ][ j ]
         if arr[ i ] <= j:
            dp[ i ][ j ] += dp[ i - 1 ][ j - arr[ i ] ]

   return dp[ n - 1 ][ target ]

def targetSum2( arr, s ):
   n = len( arr )
   t = sum( arr )
   target = int( ( s + t ) / 2 )

   dp = [ 0 for _ in range( target + 1 ) ]
   dp[ 0 ] = dp[ arr[ 0 ] ] = 1

   for i in range( 1, n ):
      for j in range( target, 0, -1 ):
         if arr[ i ] <= j:
            dp[ j ] = dp[ j ] + dp[ j - arr[ i ] ]

   return dp[ target ]

testCases = [
      {
         'input' : [1, 1, 2, 3],
         'S' : 1,
         'output' : 3,
      },
      {
         'input' : [1, 2, 7, 1],
         'S' : 9,
         'output' : 2,
      },
]

for test in testCases:
   i = test[ 'input' ]
   s = test[ 'S' ]
   o = test[ 'output' ]
   assert( targetSum( i, s ) == o )
   assert( targetSum2( i, s ) == o )
