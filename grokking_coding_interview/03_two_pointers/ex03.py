#!/usr/bin/env python
# Squaring a Sorted Array (easy)
#
# Given a sorted array, create a new array containing squares of all the numbers of
# the input array in the sorted order.

def squareSort( arr ):
   #  0  1  2  3  4       0  1  2  3  4
   # -2 -1  0  2  3       0  0  0  0  0
   #  F           B                   C
   # -2 -1  0  2  4       0  0  0  0  9
   #  F        B                   C
   # -2 -1  0  2  3       0  0  0  4  9
   #  F     B                   C
   # -2 -1  0  2  3       0  0  4  4  9
   #     F  B                C
   # -2 -1  0  2  3       0  1  4  4  9
   #        FB            C
   # -2 -1  0  2  3       0  1  4  4  9
   #        B  F          C
   size = len( arr )
   result = [ None ] * size

   front, back, cur = 0, size - 1, size - 1
   while front <= back:
      if arr[ front ] * arr[ front ] < arr[ back ] * arr[ back ]:
         result[ cur ] = arr[ back ] * arr[ back ]
         back -= 1
      else:
         result[ cur ] = arr[ front ] * arr[ front ]
         front += 1
      cur -= 1
   return result

testCases = [
      {
         'input' : [-2, -1, 0, 2, 3],
         'output' : [0, 1, 4, 4, 9],
      },
      {
         'input' : [-3, -1, 0, 1, 2],
         'output' : [0, 1, 1, 4, 9],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( o == squareSort( i ) )
