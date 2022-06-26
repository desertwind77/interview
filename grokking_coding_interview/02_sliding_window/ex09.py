#!/usr/bin/env python
#
# String Anagrams (hard)
#
# Given a string and a pattern, find all anagrams of the pattern in the given string.
#
# Every anagram is a permutation of a string. As we know, when we are not allowed to
# repeat characters while finding permutations of a string, we get N!N! permutations
# (or anagrams) of a string having NN characters. For example, here are the six
# anagrams of the string “abc”:
#
# abc
# acb
# bac
# bca
# cab
# cba
#
# Write a function to return a list of starting indices of the anagrams of the
# pattern in the given string.

from collections import defaultdict

def anagrams( arr, pattern ):
   # Sliding Windows
   # n = len( arr ) and m = len( pattern )
   # time = O( n + m )
   # space = O( m ) for hashmap
   charFreq = defaultdict( int )
   for ch in pattern:
      charFreq[ ch ] += 1

   result = []
   windowStart, matched = 0, 0
   for windowEnd in range( len( arr ) ):
      rightChar = arr[ windowEnd ]
      if rightChar in charFreq:
         charFreq[ rightChar ] -= 1
         if charFreq[ rightChar ] == 0:
            matched += 1

      if matched == len( charFreq ):
         result.append( windowStart )

      if windowEnd >= len( pattern ) - 1:
         leftChar = arr[ windowStart ]
         windowStart += 1
         if leftChar in charFreq:
            if charFreq[ leftChar ] == 0:
               matched -= 1
            charFreq[ leftChar ] += 1

   return result

testCases = [
      # index       :    | 0  | 1   | 2  | 3
      # input       :    | p  | p   | q  | p
      # windowStart : 0  | 0  | 0   | 1  | 2
      # charFreq    : p1 | p0 | p-1 | p0 | p0
      #               q1 | q1 | q1  | q0 | q0
      # match       : 0  | 0  | 0   | 2  | 2
      # result      :    |    |     | 1  | 12
      #
      # windowStart : 0  | 0  | 1   | 2  | 3
      # charFreq    : p1 | p0 | p0  | p1 | p0
      #               q1 | q1 | q1  | q0 | q1
      # match       : 0  | 0  | 1   | 1  | 1
      {
         'input' : "ppqp",
         'pattern' : "pq",
         'output' : [1, 2],
      },
      {
         'input' : "abbcabc",
         'pattern' : "abc",
         'output' : [2, 3, 4],
      },
]

for test in testCases:
   i = test[ 'input' ]
   p = test[ 'pattern' ]
   o = test[ 'output' ]
   assert( anagrams( i, p ) == o )
