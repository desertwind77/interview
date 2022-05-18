#!/usr/bin/env python
# Given an array of numbers sorted in an ascending order,
# find the ceiling of a given number ‘key’. The ceiling
# of the ‘key’ will be the smallest element in the given
# array greater than or equal to the ‘key’.
#
# Write a function to return the index of the ceiling of
# the ‘key’. If there isn’t any ceiling return -1.

# Case 1
# 4 (6) 10, key = 6
# F  F  T
#
# Case 2
# 1 3 8 10 (15), key = 12
# F F F F   T
#
# Case 3
# 4 6 10, key = 17
# F F F
#
# Case 4
# (4) 6 10, key = -1
#  T  T T
def predicate( x, key ):
   return x > key

def binarySearch( arr, key ):
   start, end = 0, len( arr ) - 1

   while start < end:
      mid = start + int( ( end - start + 1 ) / 2 )
      if predicate( arr[ mid ], key ):
         end = mid - 1
      else:
         start = mid

   if arr[ start ] == key:             # case 1
      return start
   elif arr[ start ] > key:            # case 4
      return start
   elif start < len( arr ) - 1 and \
         arr[ start + 1 ] > key:       # case 2
      return start + 1
   # case 3
   return -1

testCases = [
      {
         'input' : [4, 6, 10],
         'key' :  6,
         'output' : 1,
      },
      {
         'input' : [1, 3, 8, 10, 15],
         'key' :  12,
         'output' : 4,
      },
      {
         'input' : [4, 6, 10],
         'key' :  17,
         'output' : -1,
      },
      {
         'input' : [4, 6, 10],
         'key' :  -1,
         'output' : 0,
      },
]

for test in testCases:
   i = test[ 'input' ]
   key = test[ 'key' ]
   o = test[ 'output' ]
   assert( binarySearch( i, key ) == o )
