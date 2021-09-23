#!/usr/bin/env python3

from collections import defaultdict
from huffman_tree import huffmanTree

def getWordFrequency( string ):
   freq = defaultdict( int )
   for s in string:
      freq[ s ] += 1
   return dict( freq )

def huffmanEncode( string ):
   freq = getWordFrequency( string )
   coding = huffmanTree( freq )

   answer = ''
   for s in string:
      answer += coding[ s ]
   return answer

if __name__ == '__main__':
   testCases = [
         {

            # The input has 47 characters, each of which takes one byte. So the input
            # takes 47 * 8 = 376 bits.
            'string' : 'Huffman coding is a data compression algorithm.',
            # The encoded string takes 194 bits.
            'answer' : 194,
         }
   ]

   for test in testCases:
      string = test[ 'string' ]
      answer = test[ 'answer' ]
      assert( answer == len( huffmanEncode( string ) ) )
