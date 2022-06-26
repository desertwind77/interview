#!/usr/bin/env python
#
# Longest Substring with Distinct Characters (hard)
#
# Given a string, find the length of the longest substring, which has all distinct
# characters.

from collections import deque

def longestSubstring( arr ):
   start = maxLen = 0
   chars = deque()

   for i in range( len( arr ) ):
      cur = arr[ i ]

      while chars and cur in chars:
         start += 1
         chars.popleft()

      chars.append( cur )
      maxLen = max( maxLen, i - start + 1 )

   return maxLen

testCases = [
      # index : 0  1  2  3  4  5  6
      # input : a  a  b  c  c  b  b
      # start : 0  1  1  1  4  4  6
      # set   : a  a  a  a  c  b  b
      #               b  b     c
      #                  c
      {
         'input' : "aabccbb",
         'output' : 3
      },
      {
         'input' : "abbbb",
         'output' : 2
      },
      {
         'input' : "abccde",
         'output' : 3
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   print( longestSubstring( i ) )
