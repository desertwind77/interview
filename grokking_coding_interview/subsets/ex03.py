#!/usr/bin/env python
# Given a set of distinct numbers, find all of its permutation1.
#
# Permutation is defined as the re-arranging of the elements of
# the set. For example, {1, 2, 3} has the following six permutation1:
#
# {1, 2, 3}
# {1, 3, 2}
# {2, 1, 3}
# {2, 3, 1}
# {3, 1, 2}
# {3, 2, 1}
# If a set has ‘n’ distinct elements it will have n!n! permutation1.

def permutations1( arr ):
   result = [ [] ]

   for a in arr:
      cur = []
      for r in result:
         for i in range( len( r ) + 1 ):
            tmp = r[:]
            tmp.insert( i, a )
            cur.append( tmp )
      result = cur

   return sorted( result )

def permutations2( arr ):
   result = []
   queue = [ ( [], arr[:] ) ]

   while queue:
      prefix, input = queue.pop( 0 )
      if not input:
         result.append( prefix )
      else:
         for i in range( len( input ) ):
            curPrefix = prefix[:]
            curPrefix.append( input[ i ] )
            curInput = input[:]
            curInput.pop( i )
            queue.append( ( curPrefix, curInput ) )

   return sorted( result )

from collections import deque

def permutations3( nums ):
   numsLength = len( nums )
   result = []
   permutations = deque()
   permutations.append( [] )

   for currentNumber in nums:
      # we will take all existing permutations and add the
      # current number to create new permutations
      n = len( permutations )
      for _ in range( n ):
         oldPermutation = permutations.popleft()
         # create a new permutation by adding the current number
         # at every position
         for j in range( len( oldPermutation ) + 1 ):
            newPermutation = list( oldPermutation )
            newPermutation.insert( j, currentNumber )

            if len( newPermutation ) == numsLength:
               result.append( newPermutation )
            else:
               permutations.append( newPermutation )

   return sorted( result )

def doPermutation( nums, index, curPermutation, result ):
   if index == len( nums ):
      result.append( curPermutation )
   else:
      for i in range( len( curPermutation ) + 1 ):
         newPermutation = list( curPermutation )
         newPermutation.insert( i, nums[ index ] )
         doPermutation( nums, index + 1, newPermutation, result )

def permutationRecursive( nums ):
   result = []
   doPermutation( nums, 0, [], result )
   return result

testCases = [
      {
         'input' : [ 1, 2, 3 ],
         'output' : [ [ 1, 2, 3 ], [ 1, 3, 2 ], [ 2, 1, 3 ], [2, 3, 1 ],
                      [ 3, 1, 2 ], [ 3, 2, 1 ] ]
      }
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( permutations1( i ) == o )
   assert( permutations2( i ) == o )
   assert( permutations3( i ) == o )
   assert( sorted( permutationRecursive( i ) ) )
