#!/usr/bin/env python
# Triplet Sum to Zero (medium)
#
# Given an array of unsorted numbers, find all unique triplets in it that add up to
# zero.

def tripletSumToZero( arr ):
   def twoSum( arr, target ):
      result = []
      f, b = 0, len( arr ) - 1
      while f < b:
         if f > 0 and arr[ f ] == arr[ f - 1 ]:
            f += 1
            continue

         if arr[ f ] + arr[ b ] == target:
            result.append( [ arr[ f ], arr[ b ] ] )
            f += 1
         elif arr[ f ] + arr[ b ] < target:
            f += 1
         else:
            b -= 1
      return result

   result = []
   size = len( arr )
   arr = sorted( arr )
   # -3 -2 -1  0  1  1  2
   for i in range( 0, size - 2 ):
      if i > 0 and arr[ i ] == arr[ i - 1 ]:
         continue

      first = [ arr[ i ] ]
      target = -arr[ i ]
      rest = twoSum( arr[ i+1: ], target )
      if rest:
         for i in rest:
            result.append( first + i )

   return result


testCases = [
      {
         'input' : [-3, 0, 1, 2, -1, 1, -2],
         'output' : [ [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1], ]
      },
      {
         'input' : [-5, 2, -1, -2, 3],
         'output' : [[-5, 2, 3], [-2, -1, 3]],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( o == tripletSumToZero( i ) )
