#!/usr/bin/env python
# Given an infinite sorted array (or an array with unknown size), find if a given
# number ‘key’ is present in the array. Write a function to return the index of
# the ‘key’ if it is present in the array, otherwise return -1.
#
# Since it is not possible to define an array with infinite (unknown) size, you
# will be provided with an interface ArrayReader to read elements of the array.
# ArrayReader.get(index) will return the number at index; if the array’s size
# is smaller than the index, it will return Integer.MAX_VALUE.

import math

class ArrayReader:
   def get( arr, index ):
      if index < len( arr ):
         return arr[ index ]
      return math.inf

def predicate( x, key ):
   return x > key

def binarySearch( arr, key ):
   start, end = 0, 1
   cur = ArrayReader.get( arr, end )
   while cur < key:
      step = end - start
      start = end + 1
      end = start + step * 2
      cur = ArrayReader.get( arr, end )

   while start < end:
      mid = start + int( ( end - start + 1 ) / 2 )
      if predicate( ArrayReader.get( arr, mid ), key ):
         end = mid - 1
      else:
         start = mid

   if ArrayReader.get( arr, start ) == key:
      return start
   return -1

testCases = [
      {
         'input' : [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
         'key' : 16,
         'output' : 6,
      },
      {
         'input' : [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
         'key' : 11,
         'output' : -1,
      },
      {
         'input' : [1, 3, 8, 10, 15],
         'key' : 15,
         'output' : 4,
      },
      {
         'input' : [1, 3, 8, 10, 15],
         'key' : 200,
         'output' : -1,
      },
]

for test in testCases:
   i = test[ 'input' ]
   key = test[ 'key' ]
   o = test[ 'output' ]
   assert( binarySearch( i, key ) == o )
