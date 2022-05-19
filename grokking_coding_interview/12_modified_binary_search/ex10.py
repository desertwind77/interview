#!/usr/bin/env python
# Given an array of numbers which is sorted in ascending order and
# is rotated ‘k’ times around a pivot, find ‘k’.
#
# You can assume that the array does not have any duplicates.

def predicate( arr, i ):
   # decreasing
   if i == 0:
      return arr[ i ] > arr[ i + 1 ]
   else:
      return arr[ i ] < arr[ i - 1 ]

def findMax( arr ):
   start, end = 0, len( arr ) - 1

   while start < end:
      mid = start + int( ( end - start + 1 ) / 2 )
      if predicate( arr, mid ):
         end = mid - 1
      else:
         start = mid
   return start

def find( arr ):
   maxIndex = findMax( arr )
   if maxIndex == len( arr ) - 1:
      return 0
   else:
      return maxIndex + 1

testCases = [
      {
         'input' : [10, 15, 1, 3, 8],
         'output' : 2,
      },
      {
         'input' : [4, 5, 7, 9, 10, -1, 2],
         'output' : 5,
      },
      {
         'input' : [1, 3, 8, 10],
         'output' : 0,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( find( i ) == o )
