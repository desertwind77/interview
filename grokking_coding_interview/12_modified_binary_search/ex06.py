#!/usr/bin/env python
# Given an array of numbers sorted in ascending order, find the element in the
# array that has the minimum difference with the given ‘key’.

def predicate( x, key ):
   return x - key > 0

def binarySearch( arr, key ):
   start, end = 0, len( arr ) - 1

   while start < end:
      mid = start + int( ( end - start + 1 ) / 2 )
      if predicate( arr[ mid ], key ):
         end = mid - 1
      else:
         start = mid

   # 1 F F (F) T T
   # 2 F F F F (F)
   # 3 (T) T T T T
   if predicate( arr[ start ], key ):     # case 3
      return arr[ start ]
   elif start == len( arr ) - 1:          # case 2
      return arr[ start ]
   else:                                  # case 1
      if key - arr[ start ] > arr[ start + 1 ] - key:
         return arr[ start + 1 ]
      else:
         return arr[ start ]

testCases = [
      {
         'input' : [4, 6, 10],
         'key' : 7,
         'output' : 6,
      },
      {
         'input' : [4, 6, 10],
         'key' : 4,
         'output' : 4,
      },
      {
         'input' : [1, 3, 8, 10, 15],
         'key' : 12,
         'output' : 10,
      },
      {
         'input' : [4, 6, 10],
         'key' : 17,
         'output' : 10,
      },
]

for test in testCases:
   i = test[ 'input' ]
   key = test[ 'key' ]
   o = test[ 'output' ]
   print( binarySearch( i, key ) )
