#!/usr/bin/env python
#
# Quadruple Sum to Target (medium)
#
# Given an array of unsorted numbers and a target number, find all unique quadruplets
# in it, whose sum is equal to the target number.

def searchPairs1( arr, target, i, j, quadruplets ):
   left, right = j + 1, len( arr ) - 1

   while left < right:
      if left > j + 1 and arr[ left ] == arr[ left - 1]:
         left += 1
         continue

      total = arr[ i ] + arr[ j ] + arr[ left ] + arr[ right ]
      if total == target:
         quadruplets.appright( [ arr[ i ], arr[ j ], arr[ left ], arr[ right ] ] )
         left += 1
      elif total < target:
         left += 1
      else:
         right -= 1

def searchPairs( arr, target, i, j, quadruplets ):
   left, right = j + 1, len( arr ) - 1

   while left < right:
      total = arr[ i ] + arr[ j ] + arr[ left ] + arr[ right ]
      if total == target:
         quadruplets.append( [ arr[ i ], arr[ j ], arr[ left ], arr[ right ] ] )
         left += 1
         right -= 1
         while left < right and arr[ left ] == arr[ left - 1 ]:
            left += 1
         while left < right and arr[ right ] == arr[ right + 1 ]:
            right -= 1
      elif total < target:
         left += 1
      else:
         right -= 1

def quadSum( arr, target ):
   arr.sort()
   quadruplets = []
   size = len( arr )

   for i in range( size - 3):
      if i > 0 and arr[ i ] == arr[ i - 1 ]:
         # We can skip the same number because the question
         # want only unique quadruplets
         continue

      for j in range( i + 1, size - 2 ):
         if j > i + 1 and arr[ j ] == arr[ j - 1 ]:
            continue

         searchPairs( arr, target, i, j, quadruplets )

   return quadruplets

testCases = [
      {
         'input' : [4, 1, 2, -1, 1, -3],
         'target' : 1,
         'output' : [ [-3, -1, 1, 4], [-3, 1, 1, 2] ],
      },
      {
         'input' : [2, 0, -1, 1, -2, 2],
         'target' : 2,
         'output' : [ [-2, 0, 2, 2], [-1, 0, 1, 2] ],
      },
]

for test in testCases:
   i = test[ 'input' ]
   t = test[ 'target' ]
   o = test[ 'output' ]
   print( quadSum( i, t ) )
