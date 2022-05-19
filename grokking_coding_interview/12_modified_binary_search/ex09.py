#!/usr/bin/env python
# Given an array of numbers which is sorted in ascending order and also rotated
# by some arbitrary number, find if a given ‘key’ is present in it.
#
# Write a function to return the index of the ‘key’ in the rotated array. If
# the ‘key’ is not present, return -1. You can assume that the given array
# does not have any duplicates.

# We can do the same thing as ex08.py

testCases = [
      {
         'input' : [10, 15, 1, 3, 8],
         'key' : 15,
         'output' : 1,
      },
      {
         'input' : [4, 5, 7, 9, 10, -1, 2],
         'key' : 10,
         'output' : 4,
      },
]

for test in testCases:
   i = test[ 'input' ]
   key = test[ 'key' ]
   o = test[ 'output' ]
