#!/usr/bin/env python
#
# Smallest Window containing Substring (hard)
#
# Given a string and a pattern, find the smallest substring in the given string which
# has all the character occurrences of the given pattern.

def smallestWindow1( arr, pattern ):
   # Brute force:
   # time = O( n * m )
   # space = O( n )
   maxResult = ''
   for start in range( len( arr ) ):
      cur = arr[ start ]
      if cur not in pattern:
         continue

      i = start
      curPattern = list( pattern )
      result = ''
      while i < len( arr ) and curPattern:
         if arr[ i ] in curPattern:
            curPattern.remove( arr[ i ] )
         result += arr[ i ]
         i += 1

      if not curPattern:
         if maxResult == '' or len( maxResult ) > len( result ):
            maxResult = result

   return maxResult

from collections import defaultdict

def smallestWindow2( arr, pattern ):
   charFreq = defaultdict( int )
   for ch in pattern:
      charFreq[ ch ] += 1

   smallest = ''
   windowStart, matched = 0, 0
   for windowEnd in range( len( arr ) ):
      rightChar = arr[ windowEnd ]
      if rightChar in charFreq:
         charFreq[ rightChar ] -= 1
         if charFreq[ rightChar ] >= 0:
            matched += 1

      if matched == len( pattern ):
         while windowStart < windowEnd:
            leftChar = arr[ windowStart ]
            if ( ( leftChar in charFreq ) and ( charFreq[ leftChar ] < 0 ) ) or \
                  ( leftChar not in charFreq ):
               charFreq[ leftChar ] += 1
               windowStart += 1
            else:
               break
         cur = arr[ windowStart : windowEnd + 1 ]
         if not smallest or len( smallest ) > len( cur ):
            smallest = cur

   return smallest

def smallestWindow3( arr, pattern ):
   charFreq = defaultdict( int )
   for ch in pattern:
      charFreq[ ch ] += 1

   windowStart = matched = subStrStart = 0
   minLength = len( arr ) + 1

   for windowEnd in range( len( arr ) ):
      rightChar = arr[ windowEnd ]
      if rightChar in charFreq:
         charFreq[ rightChar ] -= 1
         if charFreq[ rightChar ] >= 0:
            matched += 1

      while matched == len( pattern ):
         if minLength > windowEnd - windowStart + 1:
            minLength = windowEnd - windowStart + 1
            subStrStart = windowStart

         leftChar = arr[ windowStart ]
         windowStart += 1
         if leftChar in charFreq:
            if charFreq[ leftChar ] == 0:
               # Note that we could have redundant matching characters,
               # therefore we'll decrement the matched count only when a
               # useful occurrence of a matched character is going out
               # of the window
               matched -= 1
            charFreq[ leftChar ] += 1

   if minLength > len( arr ):
      return ''

   return arr[ subStrStart : subStrStart + minLength ]

testCases = [
      {
         'input' : "aabdec",
         'pattern' : "abc",
         'output' : "abdec",
      },
      # index       :    | 0  1  2  3  4  5  6  7  8  9  10 11 12  13 14
      # input       :    | a  x  x  a  b  d  e  c  a  y  y  a  b   a  c
      # windowStart : 0  | 0  0  0  0  0  0  0  0  1  3  3  3  4   4
      # charFreq    : a2 | a1 a1 a1 a0 a0 a0 a0 a0 a0 a1 a1 a0 a1  a0
      #               b1 | b1 b1 b1 b1 b0 b0 b0 b0 b0 b0 b0 b0 b-1 b-1
      #               c1 | c1 c1 c1 c1 c1 c1 c1 c0 c0 c0 c0 c0 c0  c0
      # match       : 0  | 1  1  1  2  3  3  3  4  4  3  3  4  3   4
      #
      # subStrStart : 0  | 0  0  0  0  0  0  0  0  3  3  3  4  4   
      # windowStart : 0  | 0  0  0  0  0  0  0  1  3  3  3  4  4   5
      # charFreq    : a2 | a1 a1 a1 a0 a0 a0 a0 a1 a1 a1 a1 a1 a1  a0
      #               b1 | b1 b1 b1 b1 b0 b0 b0 b0 b0 b0 b0 b0 b-1 b0
      #               c1 | c1 c1 c1 c1 c1 c1 c1 c0 c0 c0 c0 c0 c0  c0
      # match       : 0  | 1  1  1  2  3  3  3  3  3  3  3  3  3   4
      {
         'input' : "axxabdecayyabac",
         'pattern' : "abac",
         'output' : "abac",
      },
      {
         'input' : "aabdec",
         'pattern' : "abac",
         'output' : "aabdec",
      },
      {
         'input' : "abdbca",
         'pattern' : "abc",
         'output' : "bca",
      },
      {
         'input' : "adcad",
         'pattern' : "abc",
         'output' : "",
      },
]

for test in testCases:
   i = test[ 'input' ]
   p = test[ 'pattern' ]
   o = test[ 'output' ]
   print( smallestWindow1( i, p ) )
   assert( smallestWindow1( i, p ) == o )
   #assert( smallestWindow2( i, p ) == o )
   assert( smallestWindow3( i, p ) == o )
