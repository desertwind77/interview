#!/usr/bin/env python
# Every non-negative integer N has a binary
# representation, for example, 8 can be represented
# as “1000” in binary and 7 as “0111” in binary.
#
# The complement of a binary representation is the
# number in binary that we get when we change every
# 1 to a 0 and every 0 to a 1. For example, the binary
# complement of “1010” is “0101”.
#
# For a given positive number N in base-10, return the
# complement of its binary representation as a base-10 integer.
import math

def allOneBits( num ):
   count = 0
   while num != 0:
      num = num >> 1
      count += 1

   return int( math.pow( 2, count ) - 1 )

def complement( num ):
   return num ^ allOneBits( num )

testCases = [
      { 'input' : 8,
        'output' : 7 },
      { 'input' : 10,
        'output' : 5 },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( complement( i ) == o )

