#!/usr/bin/env python
# Given a sorted array of numbers, find if a given number ‘key’ is present in
# the array. Though we know that the array is sorted, we don’t know if it’s sorted in
# ascending or descending order. You should assume that the array can have
# duplicates.
#
# Write a function to return the index of the ‘key’ if it is present in the array,
# otherwise return -1.

def predicate( x, key, ascending ):
   if ascending:
      return x > key
   return x < key

# index : 0 1 2 3 4 5 6
# array : 1 2 3 4 5 6 7
# pred  : F F F F F T T
# key : 5
#         s     m     e
#               s   m e
#               s me
#                 se
#
# index : 0 1 2 3 4 5 6
# array : 1 2 3 4 5 6 7
# pred  : F F F F F F F
# key : 11
#         s     m     e
#               s   m e
#                   s e
#                     se
#
# index : 0 1 2 3 4 5 6
# array : 1 2 3 4 5 6 7
# pred  : T T T T T T T
# key : -1
#         s     m     e
#         s m e
#         se
def binarySearch( arr, key ):
   start, end = 0, len( arr ) - 1
   ascending = arr[ start ] <= arr[ end ]

   while start < end:
      mid = start + int( ( end - start + 1 ) / 2 )
      if predicate( arr[ mid ], key, ascending ):
         end = mid - 1
      else:
         start = mid

   if arr[ start ] == key:
      return start

   return -1

testCases = [
      {
         'input' : [ 4, 6, 10 ],
         'key' : 10,
         'output' : 2,
      },
      {
         'input' : [1, 2, 3, 4, 5, 6, 7],
         'key' : -1,
         'output' : -1,
      },
      {
         'input' : [1, 2, 3, 4, 5, 6, 7],
         'key' : 11,
         'output' : -1,
      },
      {
         'input' : [1, 2, 3, 4, 5, 6, 7],
         'key' : 5,
         'output' : 4,
      },
      {
         'input' : [ 10, 6, 4 ],
         'key' : 10,
         'output' : 0 ,
      },
      {
         'input' : [ 10, 6, 4 ],
         'key' : 4,
         'output' : 2 ,
      },
]

for test in testCases:
   arr = test[ 'input' ]
   key = test[ 'key' ]
   output = test[ 'output' ]
   assert( binarySearch( arr, key ) == output )
