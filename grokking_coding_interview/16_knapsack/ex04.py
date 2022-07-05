#!/usr/bin/env python
#
# Minimum Subset Sum Difference (hard)
#
# Given a set of positive numbers, partition the set into two subsets with minimum
# difference between their subset sums.

def minSubsetSumDiffRecursive( arr, index, left, right ):
   # Brute force
   # time = O( 2^n )
   # space = O( n ) for stack
   if index >= len( arr ):
      return abs( left - right )

   lresult = minSubsetSumDiffRecursive( arr, index + 1, left + arr[ index ], right )
   rresult = minSubsetSumDiffRecursive( arr, index + 1, left, right + arr[ index ] )
   return min( lresult, rresult )

def minSubsetSumDiff( arr ):
   return minSubsetSumDiffRecursive( arr, 0, 0, 0 )

#################################################################################

def minSubsetSumDiffRecursive2( arr, index, left, right, dp ):
   # Brute force
   # time = O( N * M ) where N = len( arr ) and M = sum( arr )
   # space = O( N * M ) for dp + O( n ) for stack
   #       = O( N * M )
   if index >= len( arr ):
      return abs( left - right )

   if dp[ index ][ left ] == -1:
      lresult = minSubsetSumDiffRecursive2( arr, index + 1,
            left + arr[ index ], right, dp )
      rresult = minSubsetSumDiffRecursive2( arr, index + 1,
            left, right + arr[ index ], dp )
      result = min( lresult, rresult )
      dp[ index ][ left ] = dp[ index ][ right ] = result

   return dp[ index ][ left ]

def minSubsetSumDiff2( arr ):
   n = len( arr )
   s = sum( arr )
   dp = [ [ -1 for _ in range( s + 1 ) ] for _ in range( n ) ]
   return minSubsetSumDiffRecursive2( arr, 0, 0, 0, dp )

#################################################################################

import math
def minSubsetSumDiff3( arr ):
   n = len( arr )
   s = sum( arr )
   h = int( s / 2 )

   dp = [ [ False for _ in range( h + 1 ) ] for _ in range( n ) ]

   for i in range( n ):
      dp[ i ][ 0 ] = True

   for j in range( 1, h + 1 ):
      dp[ 0 ][ j ] = ( arr[ 0 ] == j )

   for i in range( 1, n ):
      for j in range( 1, h + 1 ):
         if dp[ i - 1 ][ j ]:
            dp[ i ][ j ] = dp[ i - 1 ][ j ]
         elif arr[ i ] <= j:
            dp[ i ][ j ] = dp[ i - 1 ][ j - arr[ i ] ]

   firstSubsetSum = None
   for k in range( h, -1, -1 ):
      if dp[ n - 1 ][ k ]:
         firstSubsetSum = k
         break

   secondSubsetSum = s - firstSubsetSum

   return abs( firstSubsetSum - secondSubsetSum )

#################################################################################

testCases = [
      {
         'input' : [1, 2, 3, 9],
         'output' : 3,
      },
      {
         'input' : [1, 2, 7, 1, 5],
         'output' : 0,
      },
      {
         'input' : [1, 3, 100, 4],
         'output' : 92,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( minSubsetSumDiff( i ) == o )
   assert( minSubsetSumDiff2( i ) == o )
   assert( minSubsetSumDiff3( i ) == o )
