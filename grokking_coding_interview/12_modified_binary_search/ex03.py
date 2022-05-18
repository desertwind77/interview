#!/usr/bin/env python
# Given an array of lowercase letters sorted in ascending order, find the smallest
# letter in the given array greater than a given ‘key’.
#
# Assume the given array is a circular list, which means that the last letter is
# assumed to be connected with the first letter. This also means that the smallest
# letter in the given array is greater than the last letter of the array and is
# also the first letter of the array.
#
# Write a function to return the next letter of the given ‘key’.
#
# a c (f) h, key = f
# F F  F  T
#
# (a) c f h, key = b
#  F  T T T
#
# a c f (h), key = m
# F F F  F
#
# a c f (h), key = h
# F F F  F
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

   if start == len( arr ) - 1:
      return arr[ 0 ]
   return arr[ start + 1 ]

testCases = [
      {
         'input' : ['a', 'c', 'f', 'h'],
         'key' : 'f',
         'output' : 'h',
      },
      {
         'input' : ['a', 'c', 'f', 'h'],
         'key' : 'b',
         'output' : 'c',
      },
      {
         'input' : ['a', 'c', 'f', 'h'],
         'key' : 'm',
         'output' : 'a',
      },
      {
         'input' : ['a', 'c', 'f', 'h'],
         'key' : 'h',
         'output' : 'a',
      },
]

for test in testCases:
   i = test[ 'input' ]
   key = test[ 'key' ]
   o = test[ 'output' ]
   assert( binarySearch( i, key ) == o )
