#!/usr/bin/env python3
# Triplet Sum Close to Target (medium)
#
# Given an array of unsorted numbers and a target number, find a triplet in the array
# whose sum is as close to the target number as possible, return the sum of the
# triplet. If there are more than one such triplet, return the sum of the triplet
# with the smallest sum.

def tripletSum( arr, target ):
   def twoSum( arr, target ):
      f, b = 0, len( arr ) - 1

      result = None
      while f < b:
         total = arr[ f ] + arr[ b ]

         if result is None or abs( target - total ) < abs( target - result ):
            result = total

         if total == target:
            break
         elif total < target:
            f += 1
         else:
            b -= 1

      return result

   arr = sorted( arr )

   closest = None
   for i in range( 0, len( arr ) - 2 ):
      search = twoSum( arr[ i + 1 : ], target - arr[ i ] )
      total = arr[ i ] + search

      if closest is None or abs( target - total ) < abs( target - closest ):
         closest = total

   return closest

testCases = [
      {
         'input' : [-2, 0, 1, 2],
         'target' : 2,
         'output' : 1,
      },
      {
         'input' : [-3, -1, 1, 2],
         'target' : 1,
         'output' : 0,
      },
      {
         'input' : [1, 0, 1, 1],
         'target' : 100,
         'output' : 3,
      },
]

for test in testCases:
   i = test[ 'input' ]
   t = test[ 'target' ]
   o = test[ 'output' ]
   assert( o == tripletSum( i, t ) )
