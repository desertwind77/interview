#!/usr/bin/env python
# Pair with Target Sum (easy)
#
# Given an array of sorted numbers and a target sum, find a pair in the array whose
# sum is equal to the given target.
#
# Write a function to return the indices of the two numbers (i.e. the pair) such that
# they add up to the given target.

def pairSum( arr, target ):
   start, end = 0, len( arr ) - 1

   while start < end:
      total = arr[ start ] + arr[ end ]
      if total < target:
         start += 1
      elif total > target:
         end -= 1
      else:
         return [ start, end ]

   return [ -1, -1 ]

testCases = [
      {
         'input' : [1, 2, 3, 4, 6],
         'target' : 6,
         'output' : [1, 3],
      },
      {
         'input' : [2, 5, 9, 11],
         'target' : 11,
         'output' : [0, 2],
      },
]

for test in testCases:
   i = test[ 'input' ]
   t = test[ 'target' ]
   o = test[ 'output' ]
   print( pairSum( i, t ) )

