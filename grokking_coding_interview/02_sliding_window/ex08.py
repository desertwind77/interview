#!/usr/bin/env python
#
# Permutation in a String (hard)
#
# Given a string and a pattern, find out if the string contains any permutation of
# the pattern.
#
# Permutation is defined as the re-arranging of the characters of the string. For
# example, “abc” has the following six permutations:
#
# abc
# acb
# bac
# bca
# cab
# cba
#
# If a string has ‘n’ distinct characters, it will have n! permutations.

def containPattern1( arr, pattern ):
   # Brute force : O( n ^ 2 )
   contain = []
   curPattern = list( pattern )

   for i in range( len( arr ) ):
      cur = arr[ i ]
      if cur in curPattern:
         contain.append( cur )
         curPattern.remove( cur )
         if not curPattern:
            return True
      else:
         contain = []
         curPattern = list( pattern )

   return False

from collections import defaultdict

def containPattern2( arr, pattern ):
   # Sliding Windows
   # n = len( arr ) and m = len( pattern )
   # time = O( n + m )
   # space = O( m ) for hashmap
   windowStart, matched = 0, 0
   charFreq = defaultdict( int )

   for ch in pattern:
      charFreq[ ch ] += 1

   for windowEnd in range( len( arr ) ):
      rightChar = arr[ windowEnd ]
      if rightChar in charFreq:
         charFreq[ rightChar ] -= 1
         if charFreq[ rightChar ] == 0:
            matched += 1

      if matched == len( charFreq ):
         return True

      if windowEnd >= len( pattern ) - 1:
         leftChar = arr[ windowStart ]
         windowStart += 1
         if leftChar in charFreq:
            if charFreq[ leftChar ] == 0:
               matched -= 1
            charFreq[ leftChar ] += 1

   return False

testCases = [
      # Brute force:
      # index : 0 1 2 3 4 5 6
      # input : o i d b c a f
      # start : 0 1 2 3 3 3
      # hash  :       b b b
      #                 c c
      #                   a
      # Sliding Window:
      # index    :    0  1  2  3  4  5 6
      # input    :    o  i  d  b  c  a f
      # start    : 0
      # match    : 0  0  0  0  1  2  3
      # charFreq : a1 a1 a1 a1 a1 a1 a0
      #            b1 b1 b1 b1 b0 b0 b0
      #            c1 c1 c1 c1 c1 c0 c0
      {
         'input' : "oidbcaf",
         'pattern' : "abc",
         'output' : True,
      },
      {
         'input' : "odicf",
         'pattern' : "dc",
         'output' : False,
      },
      {
         'input' : "bcdxabcdy",
         'pattern' : "bcdyabcdx",
         'output' : True,
      },
      # index    :    0  1   2   3   4
      # input    :    a  a   a   c   b
      # start    : 0  0  0   0   1   2
      # match    : 0  1  1   1   2   3
      # charFreq : a1 a0 a-1 a-1 a0  a0  (at the end of the iteration)
      #                      **  **      (was changed at the end of the iteration)
      #            b1 b1 b1  b1  b1  b0
      #            c1 c1 c1  c1  c0  c0
      {
         'input' : "aaacb",
         'pattern' : "abc",
         'output' : True,
      },
]

for test in testCases:
   i = test[ 'input' ]
   p = test[ 'pattern' ]
   o = test[ 'output' ]
   assert( containPattern1( i, p ) == o )
   assert( containPattern2( i, p ) == o )
