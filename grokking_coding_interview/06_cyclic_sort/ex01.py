#!/usr/bin/env python
# Cyclic Sort (easy)
#
# We are given an array containing n objects. Each object, when created, was assigned
# a unique number from the range 1 to n based on their creation sequence. This means
# that the object with sequence number 3 was created just before the object with
# sequence number 4.
#
# Write a function to sort the objects in-place on their creation sequence number in
# O(n) and without using any extra space. For simplicity, let’s assume we are
# passed an integer array containing only the sequence numbers, though each number is
# actually an object.

def sort( arr ):
   # index : 0 1 2 3 4
   # array : 3 1 5 4 2
   # 0       5 1 3 4 2
   #         2 1 3 4 5
   #         1 2 3 4 5
   for i in range( len( arr ) ):
      while arr[ i ] != i + 1:
         tmp = arr[ i ]
         arr[ i ], arr[ tmp - 1 ] = arr[ tmp - 1 ], arr[ i ]

testCases = [
      {
         'input' : [3, 1, 5, 4, 2],
         'output' : [1, 2, 3, 4, 5],
      },
      {
         'input' : [2, 6, 4, 3, 1, 5],
         'output' : [1, 2, 3, 4, 5, 6],
      },
      {
         'input' : [1, 5, 6, 4, 3, 2],
         'output' : [1, 2, 3, 4, 5, 6],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   sort( i )
   assert( i == o )
