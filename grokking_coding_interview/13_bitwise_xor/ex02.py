#!/usr/bin/env python
# In a non-empty array of numbers, every number
# appears exactly twice except two numbers that
# appear only once. Find the two numbers that
# appear only once.
import math

def allOneBits( num ):
   count = 0
   while num != 0:
      num = num >> 1
      count += 1

   return int( math.pow( 2, count ) - 1 )

def rightMostSetBit1( num ):
   num2 = num - 1
   allOne = allOneBits( num )
   return num2 ^ allOne

def rightMostSetBit2( num ):
   rightMostSetBit = 1
   while rightMostSetBit & num == 0:
      rightMostSetBit = rightMostSetBit << 1
   return rightMostSetBit

def twoNumbers( arr ):
   allXor = 0
   for i in arr:
      allXor ^= i

   #rightMostSetBit = rightMostSetBit1( allXor )
   rightMostSetBit = rightMostSetBit2( allXor )

   oneBit = allXor & rightMostSetBit

   oneHalf = zeroHalf = 0
   for i in arr:
      if i & oneBit:
         oneHalf ^= i
      else:
         zeroHalf ^= i

   return sorted( [ zeroHalf, oneHalf ] )

testCases = [
      { 'input' : [1, 4, 2, 1, 3, 5, 6, 2, 3, 5],
        'output' : [ 4, 6 ] },
      { 'input' : [ 2, 1, 3, 2 ],
        'output' : [ 1, 3 ] },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( twoNumbers( i ) == o )
