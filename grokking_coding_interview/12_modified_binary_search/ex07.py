#!/usr/bin/env python
# Find the maximum value in a given Bitonic array. An array is considered
# bitonic if it is monotonically increasing and then monotonically decreasing.
# Monotonically increasing or decreasing means that for any index i in
# the array arr[i] != arr[i+1].

# 1 3 8 12  4 2
# F F F (F) T T
#  8  7 6 5 4 3
# (T) T T T T T
# 1 2 3 4 5  6
# F F F F F (F)
def predicate( arr, i ):
   # decreasing
   if i == 0:
      return arr[ i ] > arr[ i + 1]
   elif i < len( arr ):
      return arr[ i ] < arr[ i - 1 ]

def binarySearch( arr ):
   start, end = 0, len( arr ) - 1

   while start < end:
      mid = start + int( ( end - start + 1 ) / 2 )
      if predicate( arr, mid ):
         end = mid - 1
      else:
         start = mid

   return arr[ start ]

testCases = [
      {
         'input' : [1, 3, 8, 12, 4, 2],
         'output' : 12,
      },
      {
         'input' : [3, 8, 3, 1],
         'output' : 8,
      },
      {
         'input' : [1, 3, 8, 12],
         'output' : 12,
      },
      {
         'input' : [10, 9, 8],
         'output' : 10,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( binarySearch( i ) == o )
