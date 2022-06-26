#!/usr/bin/env python
#
# Longest Substring with K Distinct Characters (medium)
#
# Given a string, find the length of the longest substring in it with no more than K
# distinct characters.
#
# You can assume that K is less than or equal to the length of the given string.

from collections import defaultdict

def longest( arr, unique ):
   count = defaultdict( int )
   start = 0
   maxLen = 0

   for i in range( len( arr ) ):
      count[ arr[ i ] ] += 1

      while start <= i and len( count.keys() ) > unique:
         count[ arr[ start ] ] -= 1
         if count[ arr[ start ] ] == 0:
            del count[ arr[ start ] ]
         start += 1

      maxLen = max( maxLen, i - start + 1 )

   return maxLen

testCases = [
      # index  : 0  1  2  3  4  5
      # array  : a  r  a  a  c  i, k = 2
      # start  : 0  0  0  0  2  4
      # len    : 1  2  3  4  3  2
      # unique : a1 a1 a2 a3 a2 c1
      #             r1 r1 r1 c1 i1
      {
         'input' : "araaci",
         'K' : 2,
         'output' : 4,
      },
      {
         'input' : "araaci",
         'K' : 1,
         'output' : 2,
      },
      {
         'input' : "cbbebi",
         'K' : 3,
         'output' : 5,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]
   o = test[ 'output' ]
   assert( longest( i, k ) == o )
