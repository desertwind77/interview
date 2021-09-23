#!/usr/bin/env python3

from collections import defaultdict
from huffman_tree import huffmanTree

def getWordFrequency( string ):
   freq = defaultdict( int )
   for s in string:
      freq[ s ] += 1
   return dict( freq )

def huffmanEncode( string ):
   '''
   Encode string using Huffman's algorithm
   '''
   freq = getWordFrequency( string )
   coding = huffmanTree( freq )

   answer = ''
   for s in string:
      answer += coding[ s ]

   return ( answer, coding )

def huffmanDecode( string, coding ):
   '''
   Decode string using Huffman's algorithm
   '''
   reverseCoding = {}
   for k, v in coding.items():
      reverseCoding[ v ] = k

   decoded = ''
   while len( string ) != 0:
      found = False
      for code, symbol in reverseCoding.items():
         if string.startswith( code ):
            decoded += symbol
            size = len( code )
            string = string[ size: ]
            found = True

      if not found:
         return ''

   return decoded

if __name__ == '__main__':
   testCases = [
         {

            # The input has 47 characters, each of which takes one byte. So the input
            # takes 47 * 8 = 376 bits.
            'string' : 'Huffman coding is a data compression algorithm.',
            # The encoded string takes 194 bits which is 51.6% of the original
            # string.
            'answer' : 194,
         }
   ]

   for test in testCases:
      string = test[ 'string' ]
      answer = test[ 'answer' ]
      encoded, coding = huffmanEncode( string )
      assert( answer == len( encoded ) )
      assert( string == huffmanDecode( encoded, coding ) )
