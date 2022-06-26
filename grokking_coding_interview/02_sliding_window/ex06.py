#!/usr/bin/env python
#
# Longest Substring with Same Letters after Replacement (hard)
#
# Given a string with lowercase letters only, if you are allowed to replace no more
# than ‘k’ letters with any letter, find the length of the longest substring having
# the same letters after replacement.

from collections import defaultdict

def longestSubstring( arr, k ):
   charFreq = defaultdict( int )
   windowStart = maxRepeatCharCount = maxLength = 0

   for windowEnd in range( len( arr ) ):
      rightChar = arr[ windowEnd ]
      charFreq[ rightChar ] += 1
      maxRepeatCharCount = max( maxRepeatCharCount, charFreq[ rightChar ] )

      if windowEnd - windowStart + 1 - maxRepeatCharCount > k:
         leftChar = arr[ windowStart ]
         charFreq[ leftChar ] -= 1
         windowStart += 1

      maxLength = max( maxLength, windowEnd - windowStart + 1 )

   return maxLength

testCases = [
      # index              : 0  1  2  3  4  5  6
      # input              : a  a  b  c  c  b  b
      # charFreq           : a1 a2 a2 a2 a2 a1 b3
      #                            b1 b1 b1 b2 c2
      #                               c1 c2 c2
      # maxRepeatCharCount : 1  2  2  2  2  2  3
      # windowStart        : 0  0  0  0  1  2  2
      # charFreq           : a1 a2 a2 a2 a1 b2
      #                            b1 b1 b1 c2
      #                               c1 c2
      {
         'input' : "aabccbb",
         'k' : 2,
         'output' : 5,
      },
      {
         'input' : "abbcb",
         'k' : 1,
         'output' : 4,
      },
      {
         'input' : "abccde",
         'k' : 1,
         'output' : 3,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'k' ]
   print( longestSubstring( i, k ) )
