#!/usr/bin/env python3
#
# Create and print a huffman tree using a greedy algorithm
# https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

class Node:
   def __init__( self, symbol, freq, left=None, right=None ):
      self.symbol = symbol
      self.freq = freq
      self.left = left
      self.right = right
      self.huffCode = ''   # either 0 or 1

   def __repr__( self ):
      return "(%s,%s)" % ( self.symbol, self.freq )

   def __str__( self ):
      return "(%s,%s)" % ( self.symbol, self.freq )

def createHuffmanCoding( root, prefix='', coding={} ):
   curPrefix = prefix + root.huffCode
   if root.symbol != '':
      # Leaf nodes
      coding[ root.symbol ] = curPrefix
   else:
      # Internal ndoes
      if root.left:
         createHuffmanCoding( root.left, curPrefix, coding=coding )
      if root.right:
         createHuffmanCoding( root.right, curPrefix, coding=coding )

def createHuffmanTree( freq ):
   if isinstance( freq, list ):
      nodeList = [ Node( c, f ) for ( c, f ) in freq ]
   elif isinstance( freq, dict ):
      nodeList = [ Node( k, v ) for ( k, v ) in freq.items() ]
   else:
      return None

   while len( nodeList ) != 0:
      nodeList = sorted( nodeList, key=lambda n: n.freq )

      left = nodeList.pop( 0 )
      if len( nodeList ) == 0:
         # This is the last node in nodeList. So it is the root.
         return left
      else:
         # Before popping left, there were at least 2 nodes in nodeList. So create an
         # internal node that groups left and right nodes.
         right = nodeList.pop( 0 )
         left.huffCode = '0'
         right.huffCode = '1'
         nodeList.append( Node( '', left.freq + right.freq, left, right ) )

def huffmanTree( freq ):
   root = createHuffmanTree( freq )
   coding = {}
   createHuffmanCoding( root, coding=coding )
   return coding

if __name__ == '__main__':
   testCases = [
         {
            'frequency' : [ ( 'a', 5 ), ( 'b', 9 ), ( 'c', 12 ), ( 'd', 13 ),
                            ( 'e', 16 ), ( 'f', 45 ) ],
            'answer'    : { 'f': '0',
                            'c': '100',
                            'd': '101',
                            'a': '1100',
                            'b': '1101',
                            'e': '111' },
         },
   ]

   for test in testCases:
      freq = test[ 'frequency' ]
      answer = test[ 'answer' ]
      assert( answer == huffmanTree( freq ) )
