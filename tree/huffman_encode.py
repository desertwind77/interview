#!/usr/bin/env python3

from collections import defaultdict
from huffman_tree import huffmanTree

def getWordFrequency( plainText ):
   wordFrequency = defaultdict( int )
   for s in plainText:
      wordFrequency[ s ] += 1
   return dict( wordFrequency )

def huffmanEncode( plainText ):
   '''
   Encode plainText using Huffman's algorithm
   '''
   wordFrequency = getWordFrequency( plainText )
   huffmanCodeDict = huffmanTree( wordFrequency )

   answer = ''
   for s in plainText:
      answer += huffmanCodeDict[ s ]

   return ( answer, huffmanCodeDict )

def huffmanDecode( plainText, huffmanCodeDict ):
   '''
   Decode plainText using Huffman's algorithm
   '''
   reversehuffmanCodeDict = {}
   for k, v in huffmanCodeDict.items():
      reversehuffmanCodeDict[ v ] = k

   decoded = ''
   while len( plainText ) != 0:
      found = False
      for code, symbol in reversehuffmanCodeDict.items():
         if plainText.startswith( code ):
            decoded += symbol
            size = len( code )
            plainText = plainText[ size: ]
            found = True

      if not found:
         return ''

   return decoded

if __name__ == '__main__':
   testCases = [
         {

            # The input has 47 characters, each of which takes one byte. So the input
            # takes 47 * 8 = 376 bits.
            'plainText' : 'Huffman coding is a data compression algorithm.',
            # The encoded plainText takes 194 bits which is 51.6% of the original
            # plainText.
            'answer' : 194,
         }
   ]

   for test in testCases:
      plainText = test[ 'plainText' ]
      answer = test[ 'answer' ]
      encoded, huffmanCodeDict = huffmanEncode( plainText )
      assert( answer == len( encoded ) )
      assert( plainText == huffmanDecode( encoded, huffmanCodeDict ) )
