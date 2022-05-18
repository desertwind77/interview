#!/usr/bin/env python
# Given an array of numbers sorted in ascending order, find the range of a given
# number ‘key’. The range of the ‘key’ will be the first and last position of the
# ‘key’ in the array.
#
# Write a function to return the range of the ‘key’. If the ‘key’ is not present
# return [-1, -1].

def upper( x, key ):
   return x > key

def lower( x, key ):
   return x == key

def binarySearch( arr, start, end, key, predicate ):
   while start < end:
      mid = start + int( ( end - start + 1 ) / 2 )
      if predicate( arr[ mid ], key ):
         end = mid - 1
      else:
         start = mid

   return start

def findRange( arr, key ):
   # 1 F (F) T T
   # 2 (T) T T T
   # 3 F F F (F)
   upperIndex = binarySearch( arr, 0, len( arr ) - 1, key, upper )
   if upperIndex == 0 and upper( arr[ upperIndex ], key ):     # case 2
      return [ -1, -1 ]
   elif arr[ upperIndex ] != key:                              # case 3
      return [ -1, -1 ]

   # We know that key is in arr[ 0:upperIndex ]
   # 1 F  (F) T T
   # 2 (T) T  T T
   lowerIndex = binarySearch( arr, 0, upperIndex, key, lower )
   if lower( arr[ lowerIndex ], key ):
      return [ lowerIndex, upperIndex ]      # case 2
   return [ lowerIndex + 1, upperIndex ]     # case 1

testCases = [
      {
         'input' : [4, 6, 6, 6, 9],
         'key' : 6,
         'output' : [1, 3],
      },
      {
         'input' : [1, 3, 8, 10, 15],
         'key' : 10,
         'output' : [3, 3],
      },
      {
         'input' : [1, 3, 8, 10, 15],
         'key' : 12,
         'output' : [-1, -1],
      },
]

for test in testCases:
   i = test[ 'input' ]
   key = test[ 'key' ]
   o = test[ 'output' ]
   print( findRange( i, key ) )
