#!/usr/bin/env python
# Given a string, find all of its permutations preserving
# the character sequence but changing case.

def stringPermutations( arr ):
   results = [ arr ]

   for i in range( len( arr ) ):
      curList = []
      for result in results:
         if result[ i ].isalpha():
            # This works
            #tmp = result[ 0:i ] + result[ i ].upper() + result[ i + 1: ]

            # sting in python is immutable. We can't do str[ i ] = str[ i ].upper().
            # We can work around by convert from string to list and do the
            # conversion.
            tmp = list( result )
            tmp[ i ] = tmp[ i ].swapcase()
            curList.append( ''.join( tmp ) )
      results += curList

   return results

def doRecursive( arr, index, curPermutation, result ):
   def upper( arr, i ):
      tmp = list( arr )
      tmp[ i ] = tmp[ i ].upper()
      return ''.join( tmp )

   if index == len( arr ):
      result.append( curPermutation )
   else:
      doRecursive( arr, index + 1, curPermutation, result )
      if arr[ index ].isalpha():
         doRecursive( arr, index + 1, upper( curPermutation, index ), result )

def recursive( arr ):
   result = []
   doRecursive( arr, 0, arr, result )
   return result

testCases = [
      {
         'input' : "ad52",
         'output' : [ "ad52", "Ad52", "aD52", "AD52" ],
      },
      {
         'input' : "ab7c",
         'output' : [ "ab7c", "Ab7c", "aB7c", "AB7c",
                      "ab7C", "Ab7C", "aB7C", "AB7C" ],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( sorted( stringPermutations( i ) ) == sorted( o ) )
   assert( sorted( recursive( i ) ) == sorted( o ) )
