#!/usr/bin/env python3
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.

def threeSum1( nums ):
   # time = O( n^3 )
   size = len( nums )
   result = []
   for i in range( size - 2 ):
      first = nums[ i ]
      for j in range( i + 1, size - 1 ):
         second = nums[ j ]
         third = 0 - first - second
         if third in nums[ j+1: ]:
            curTuple = sorted( [ first, second, third ] )
            if curTuple not in result:
               result.append( curTuple )
   return sorted( result )

def threeSum2( nums):
   # time = O( n^2 )
   # space = O( n ) or O( lg n ) depending on the sorting algorithm
   def twoSum( nums, first, result ):
      size = len( nums )

      left = first + 1
      right = size - 1
      while left < size - 1 and left < right:
         total = nums[ first ] + nums[ left ] + nums[ right ]

         if total == 0:
            curTuple = [ nums[ first ], nums[ left ], nums[ right ] ]
            curTuple = sorted( curTuple )
            if curTuple not in result:
                result.append( curTuple )
            left += 1
            # We can move right because left moved
            right -= 1

            while left < right and nums[ left ] == nums[ left - 1 ]:
               left += 1
         elif total < 0:
            left += 1
         else:
            right -= 1

   nums = sorted( nums )
   size = len( nums )
   result = []

   for i in range( size - 2 ):
      if i == 0 or nums[ i ] != nums[ i - 1 ]:
         twoSum( nums, i, result )
   return sorted( result )

def threeSum3( nums):
   # time = O( n^2 )
   # space = O( n ) or O( lg n ) depending on the sorting algorithm
   def twoSum( nums, i, result ):
      seen = set()
      j = i + 1

      while j < len( nums ):
         third = 0 - nums[ i ] - nums[ j ]
         if third in seen:
            result.append( sorted( [ nums[ i ], nums[ j ], third ] ) )
         seen.add( nums[ j ] )
         j += 1

   nums = sorted( nums )
   size = len( nums )
   result = []

   for i in range( size - 2 ):
      # -1 -1 0 1 1
      # The first tuple is [ -1, 0, 1 ]
      # So we can skip the next -1 in this loop because it will give the same tuple.
      if i == 0 or nums[ i ] != nums[ i - 1 ]:
         twoSum( nums, i, result )
   return sorted( result )

def threeSum4( nums ):
   # time = O(n^2)
   # space = O(n) for hashset/hashmap
   res, dups = set(), set()
   seen = {}

   for i, val1 in enumerate( nums ):
      # Use another hashset dups to skip duplicates in the outer loop.
      if val1 not in dups:
         dups.add( val1 )
         for j, val2 in enumerate( nums[ i+1: ] ):
            complement = -val1 - val2

            if complement in seen and seen[ complement ] == i:
               res.add( tuple( sorted( ( val1, val2, complement ) ) ) )
            # Instead of re-populating a hashset every time in the inner loop, we can
            # use a hashmap and populate it once. Values in the hashmap will indicate
            # whether we have encountered that element in the current iteration. When
            # we process nums[j] in the inner loop, we set its hashmap value to i.
            # This indicates that we can now use nums[j] as a complement for nums[i].
            seen[ val2 ] = i

   # The following will not work.
   # -2 1 3 4 5
   #  i j
   # first = -2, second = 1, complement = 2 - 1 = 1
   # because 1 is in cache. we will add ( -2, 1, 1 ) to result. But this is not
   # correct.
   #
   # def threeSum(self, nums):
   #    result = []
   #
   #    cache = {}
   #    for n in nums:
   #       cache[ n ] = True
   #
   #    for i in range( len( nums ) ):
   #       if i == 0 or nums[ i ] != nums[ i + 1 ]:
   #          j = i + 1
   #          while j < len( nums ):
   #             complement = -nums[i] - nums[j]
   #             if complement in cache:
   #                result.append( [ nums[i], num[j], complement ] )
   #   return result

   result = []
   for i in res:
      cur = sorted( list( i ) )
      result.append( cur )

   return sorted( result )

testCases = [
      {
         'input' : [-1,0,1,2,-1,-4],
         'output' : [[-1,-1,2],[-1,0,1]],
      },
      {
         'input' : [],
         'output' : [],
      },
      {
         'input' : [0],
         'output' : [],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = sorted( test[ 'output' ] )
   assert( threeSum1( i ) == o )
   assert( threeSum2( i ) == o )
   assert( threeSum3( i ) == o )
   assert( threeSum4( i ) == o )
