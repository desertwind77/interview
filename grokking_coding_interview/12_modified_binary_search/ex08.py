#!/usr/bin/env python
# Given a Bitonic array, find if a given ‘key’ is present in it. An array is
# considered bitonic if it is monotonically increasing and then monotonically
# decreasing. Monotonically increasing or decreasing means that for any index
# i in the array arr[i] != arr[i+1].
#
# Write a function to return the index of the ‘key’. If the 'key' appears more
# than once, return the smaller index. If the ‘key’ is not present, return -1.

def predicateFindMax( arr, i, key=None ):
   '''decreasing'''
   if i == 0:
      return arr[ i ] > arr[ i + 1 ]
   elif i < len( arr ):
      return arr[ i ] < arr[ i - 1 ]

def predicateFindKeyInc( arr, i, key ):
   return arr[ i ] > key

def predicateFindKeyDec( arr, i, key ):
   return arr[ i ] < key

def binarySearch( arr, start, end, predicate, key=None ):
   while start < end:
      mid = start + int( ( end - start + 1 ) / 2 )
      if predicate( arr, mid, key  ):
         end = mid - 1
      else:
         start = mid
   return start

def find( arr, key ):
   size = len( arr )

   maxIndex = binarySearch( arr, 0, size - 1, predicateFindMax )
   if maxIndex == 0:
      index = binarySearch( arr, 0, size - 1, predicateFindKeyDec, key )
      if arr[ index ] == key:
         return index
   elif maxIndex == size - 1:
      index = binarySearch( arr, 0, size - 1, predicateFindKeyInc, key )
      if arr[ index ] == key:
         return index
   else:
      lIndex = binarySearch( arr, 0, maxIndex, predicateFindKeyInc, key )
      if arr[ lIndex ] == key:
         return lIndex

      rIndex = binarySearch( arr, maxIndex, size - 1, predicateFindKeyDec, key )
      if arr[ rIndex ] == key:
         return rIndex

   return -1

testCases = [
      {
         'input' : [1, 3, 8, 4, 3],
         'key' : 4,
         'output' : 3,
      },
      {
         'input' : [3, 8, 3, 1],
         'key' : 8,
         'output' : 1,
      },
      {
         'input' : [1, 3, 8, 12],
         'key' : 12,
         'output' : 3,
      },
      {
         'input' : [10, 9, 8],
         'key' : 10,
         'output' : 0,
      },
]

for test in testCases:
   i = test[ 'input' ]
   key = test[ 'key' ]
   o = test[ 'output' ]
   assert( find( i, key ) == o )
