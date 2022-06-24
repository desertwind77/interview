#!/usr/bin/env python
# Remove Duplicates (easy)
#
# Given an array of sorted numbers, remove all duplicate number instances from it
# in-place, such that each element appears only once. The relative order of the
# elements should be kept the same and you should not use any extra space so that
# that the solution have a space complexity of O(1).
#
# Move all the unique elements at the beginning of the array and after moving return
# the length of the subarray that has no duplicate in it.

def removeDuplicates( arr ):
   #   0  1  2  3  4  5  6
   #   2  3  3  3  6  9  9
   #      FN
   #         FN
   #         N  F
   #         N     F
   #   2  3  6  3  3  9  9
   #            N     F
   #   2  3  6  9  3  3  9
   #               N     F
   #               N        F
   noDup, forward = 1, 1
   while forward < len( arr ):
      if arr[ forward ] == arr[ noDup - 1 ]:
         forward += 1
      else:
         if arr[ forward ] != arr[ noDup ]:
            arr[ noDup ], arr[ forward ] = arr[ forward ], arr[ noDup ]
         noDup += 1
         forward += 1

   return noDup

testCases = [
      {
         'input' : [2, 3, 3, 3, 6, 9, 9],
         'output' : 4,
      },
      {
         'input' : [2, 2, 2, 11],
         'output' : 2,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( o == removeDuplicates( i ) )
