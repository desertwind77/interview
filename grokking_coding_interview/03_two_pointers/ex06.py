#!/usr/bin/env python
# Triplets with Smaller Sum (medium)
#
# Given an array arr of unsorted numbers and a target sum, count all triplets in it
# such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different
# indices. Write a function to return the count of such triplets.

def tripletSum( arr, target ):
   def twoSum( arr , target ):
      count = 0

      f, b = 0, len( arr ) - 1
      while f < b:
         if arr[ f ] + arr[ b ] < target:
            count += b - f
            f += 1
         else:
            b -= 1

      return count

   arr = sorted( arr )
   count = 0
   for i in range( 0, len( arr ) - 2 ):
      count += twoSum( arr[ i + 1: ], target - arr[ i ] )

   return count

testCases = [
      {
         'input' : [-1, 0, 2, 3],
         'target' : 3,
         'output' : 2,
      },
      {
         'input' : [-1, 4, 2, 1, 3],
         'target' : 5,
         'output' : 4,
      },
]

for test in testCases:
   i = test[ 'input' ]
   t = test[ 'target' ]
   o = test[ 'output' ]
   assert( o == tripletSum( i, t ) )
