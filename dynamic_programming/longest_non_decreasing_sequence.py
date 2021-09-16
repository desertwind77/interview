#!/usr/bin/env python3
# Given  a sequence of N numbers,, find the length of the longest non-decreasing
# sequence.

def longestNonDecreasingSequence( seqeunce ):
   size = len( seqeunce )
   count = [ 0 ] * size
   last = [ 0 ] * size

   for i in range( 0, size ):
      if i == 0:
         count[ i ] = 1
         last[ i ] = 0
      elif sequence[ i ] >= seqeunce[ i - 1 ]:
         count[ i ] = count[ i - 1 ] + 1
         last[ i ] = i - 1
      else:
         count[ i ] = count[ i - 1 ]
         last[ i ] = last[ i - 1 ]

   return count[ size - 1 ]

if __name__ == '__main__':
   testcases = [
         {
            'sequence' : [ 1, 2, 3, 9, 8, 7, 4, 9, 8, 4, 5, 6 ],
            'answer' : 7,
         },
   ]

   for test in testcases:
      sequence = test[ 'sequence' ]
      answer = test[ 'answer' ]
      assert( longestNonDecreasingSequence( sequence ) )
