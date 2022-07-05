#!/usr/bin/env python
#
# Subset Sum (medium)
#
# Given a set of positive numbers, determine if a subset exists whose sum is equal to
# a given number ‘S’.

def subsetSumRecursive( nums, s, index, dp ):
   if s == 0:
      return True
   if index >= len( nums ):
      return False

   if dp[ index ][ s ] == -1:
      result1 = False
      if nums[ index ] <= s:
         result1 = subsetSumRecursive( nums, s - nums[ index ], index + 1, dp )
      result2 = subsetSumRecursive( nums, s, index + 1, dp )
      dp[ index ][ s ] = result1 or result2

   return dp[ index ][ s ]

def subsetSum( nums, s ):
   # Top-down dynamic programming
   # time = O( N * M ) where N = len( nums ) and M = s
   # space = O( N * M ) for dp + O( N ) for stack
   if not nums:
      return False

   dp = [ [ -1 for _ in range( s + 1 ) ] for _ in range( len( nums ) ) ]
   return subsetSumRecursive( nums, s, 0, dp )

def subsetSum2( nums, s ):
   # Bottom-up dynamic programming
   # time = O( N * M )
   # space = O( N * M )
   #                          summation
   # index  subset            0  1  2  3  4  5  6
   # 0      { 1 }             T  T  F  F  F  F  F
   # 1      { 1, 2 }          T  T  T  T  F  F  F
   # 2      { 1, 2, 3 }       T  T  T  T  T  T  T
   # 3      { 1, 2, 3, 7 }    T  T  T  T  T  T  T
   if not nums:
      return False

   n = len( nums )

   dp = [ [ False for _ in range( s + 1 ) ] for _ in range( n ) ]
   for i in range( n ):
      dp[ i ][ 0 ] = True

   for j in range( 1, s + 1 ):
      dp[ 0 ][ j ] = ( j == nums[ 0 ] )

   for i in range( 1, n ):
      for j in range( 1, s + 1 ):
         if dp[ i - 1 ][ j ]:
            dp[ i ][ j ] = dp[ i - 1 ][ j ]
         elif nums[ i ] <= j:
            dp[ i ][ j ] = dp[ i - 1 ][ j - nums[ i ] ]

   return dp[ n - 1 ][ s ]

def subsetSum3( nums, s ):
   # Bottom-up dynamic programming
   # time = O( N * M )
   # space = O( N )
   if not nums:
      return False

   dp = [ False for _ in range( s + 1 ) ]

   dp[ 0 ] = True
   for i in range( 1, s + 1 ):
      dp[ i ] = ( i == nums[ 0 ] )

   for i in range( 1, len( nums ) ):
      for j in range( s, -1, -1 ):
         if not dp[ j ] and  nums[ i ] <= j:
            dp[ j ] = dp[ j - nums[ i ] ]

   return dp[ s ]

testCases = [
      {
         'input' : [1, 2, 3, 7],
         'S' : 6,
         'output' : True,
      },
      {
         'input' : [1, 2, 7, 1, 5],
         'S' : 10,
         'output' : True,
      },
      {
         'input' : [1, 3, 4, 8],
         'S' : 6,
         'output' : False,
      },
]

for test in testCases:
   i = test[ 'input' ]
   s = test[ 'S' ]
   o = test[ 'output' ]
   assert( subsetSum( i, s ) == o )
   assert( subsetSum2( i, s ) == o )
   assert( subsetSum3( i, s ) == o )
