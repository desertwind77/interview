#!/usr/bin/env python
#
# Equal Subset Sum Partition (medium)
#
# Given a set of positive numbers, find if we can partition it into two subsets such
# that the sum of elements in both subsets is equal.

def equalSubsetSum_recursive1( arr, index, left, right ):
   # Brute force : unable to find overlapping problems
   # time = O( 2^n )
   # space = O( n ) for stack
   if index == len( arr ):
      # if sum( left ) == sum( right ):
      #    print( left, right )
      return sum( left ) == sum( right )

   tmp = left[:]
   tmp.append( arr[ index ] )
   lResult = equalSubsetSum_recursive1( arr, index + 1, tmp, right[:] )

   tmp = right[:]
   tmp.append( arr[ index ] )
   rResult = equalSubsetSum_recursive1( arr, index + 1, left[:], tmp )

   return lResult or rResult

def equalSubsetSum1( arr ):
   return equalSubsetSum_recursive1( arr, 0, [], [] )

###############################################################

def equalSubsetSum_recursive1_1( arr, index, left, right, dp ):
   # Brute force : unable to find overlapping problems
   # time = O( 2^n )
   # space = O( n ) for stack
   if index == len( arr ):
      return left == right

   a, b = left, right
   if a > b:
      a, b = b, a
   result = dp.get( ( index, a, b ), None )
   if not result:
      lResult = equalSubsetSum_recursive1_1( arr, index + 1,
                                             left + arr[ index ], right, dp )
      rResult = equalSubsetSum_recursive1_1( arr, index + 1,
                                             left, right + arr[ index ], dp )
      result = lResult or rResult
      dp[ ( index, a, b ) ] = result

   return result

def equalSubsetSum1_1( arr ):
   return equalSubsetSum_recursive1_1( arr, 0, 0, 0, {} )

###############################################################
def equalSubsetSum_recursive2( arr, index, total ):
   if total == 0:
      return True
   if index >= len( arr ):
      return False

   result1 = False
   if arr[ index ] <= total:
      result1 = equalSubsetSum_recursive2( arr, index + 1, total - arr[ index ])
   result2 = equalSubsetSum_recursive2( arr, index + 1, total )

   return result1 or result2

def equalSubsetSum2( arr ):
   if not arr:
      return False

   total = sum( arr )
   if total % 2 != 0:
      # Odd numbers
      return False

   # Reduce the problem to check whether the summation of any subsets equals
   # total / 2.
   return equalSubsetSum_recursive2( arr, 0, total / 2 )

###############################################################

def equalSubsetSum_recursive3( arr, index, total, dp ):
   if total == 0:
      return True
   if index >= len( arr ):
      return False

   if dp[ index ][ total ] != -1:
      return dp[ index ][ total ]

   result1 = False
   if arr[ index ] <= total:
      result1 = equalSubsetSum_recursive3( arr, index + 1, total - arr[ index ], dp )
   result2 = equalSubsetSum_recursive3( arr, index + 1, total, dp )

   result = result1 or result2
   dp[ index ][ total ] = result

   return result

def equalSubsetSum3( arr ):
   # Top-down dynamic programming with memorization
   # time = O( N * M ) where N = len( arr ), M = sum( arr )
   # space = O( N * M ) for table + O( N ) for stack
   #       = O( N * M ) asymtopically
   if not arr:
      return False

   total = sum( arr )
   if total % 2 != 0:
      # Odd numbers
      return False

   # Reduce the problem to check whether the summation of any subsets equals
   # total / 2.
   total = int( total / 2 )
   dp = [ [ - 1 for _ in range( total + 1 ) ] for _ in range( len( arr ) ) ]

   return equalSubsetSum_recursive3( arr, 0, total, dp )

def equalSubsetSum4( arr ):
   # Bottom-up dynamic programming
   # time = O( N * M ) where N = len( arr ), M = sum( arr )
   # space = O( N * M )
   #
   #                    summation
   # index  subset      0 1 2 3 4 5
   # 0      {1}         T T F F F F
   # 1      {1,2}       T T T T F F
   # 2      {1,2,3}     T T T T T T
   # 3      {1,2,3,4}   T T T T T T
   s = sum( arr )

   # if 's' is a an odd number, we can't have two subsets with same total
   if s % 2 != 0:
      return False

   # we are trying to find a subset of given numbers that has a total sum of 's/2'.
   s = int( s / 2  )

   n = len( arr )
   dp = [ [ False for _ in range( s + 1 ) ] for _ in range( n ) ]

   # populate the s=0 columns, as we can always for '0' sum with an empty set
   for i in range( 0, n ):
      dp[ i ][ 0 ] = True

   # with only one number, we can form a subset only when the required sum is
   # equal to its value
   for j in range( 1, s + 1 ):
      dp[ 0 ][ j ] = arr[ 0 ] == j

   # process all subsets for all sums
   for i in range( 1, n ):
      for j in range( 1, s + 1 ):
         if dp[ i - 1 ][ j ]:
            # if we can get the sum 'j' without the number at index 'i'
            dp[ i ][ j ] = dp[ i - 1 ][ j ]
         elif j >= arr[ i ]:
            # else if we can find a subset to get the remaining sum
            dp[ i ][ j ] = dp[ i - 1 ][ j - arr[ i ] ]

   return dp[ n - 1 ][ s ]

testCases = [
      {
         'input' : [1, 2, 3, 4],
         'output' : True
      },
      {
         'input' : [1, 1, 3, 4, 7],
         'output' : True,
      },
      {
         'input' : [2, 3, 4, 6],
         'output' : False,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( equalSubsetSum1( i ) == o )
   assert( equalSubsetSum1_1( i ) == o )
   assert( equalSubsetSum2( i ) == o )
   assert( equalSubsetSum3( i ) == o )
   assert( equalSubsetSum4( i ) == o )
