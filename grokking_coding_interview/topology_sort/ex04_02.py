#!/usr/bin/env python
# There is a dictionary containing words from an alien language for which we
# don’t know the ordering of the alphabets. Write a method to find the correct
# order of the alphabets in the alien language. It is given that the input is a
# valid dictionary and there exists an ordering among its alphabets.
from collections import deque

def dictionary( words ):
   if not words:
      return ''

   sortedOrder = []
   inDegree = {}
   graph = {}
   for word in words:
      for c in word:
         inDegree[ c ] = 0
         graph[ c ] = []

   for i in range( 0, len( words ) - 1 ):
      w1, w2 = words[ i ], words[ i + 1 ]
      for j in range( 0, min( len( w1 ), len( w2 ) ) ):
         parent, child = w1[ j ], w2[ j ]
         if parent != child:
            graph[ parent ].append( child )
            inDegree[ child ] += 1
            break

   sources = deque( [ x for x, v in inDegree.items() if v == 0 ] )

   while sources:
      vertex = sources.popleft()
      sortedOrder.append( vertex )
      for c in graph[ vertex ]:
         inDegree[ c ] -= 1
         if inDegree[ c ] == 0:
            sources.append( c )

   # if sortedOrder doesn't contain all characters, there is a cyclic
   # dependency between characters, therefore, we'll not be able to
   # find the correct ordering of characters
   if len( sortedOrder ) != len( inDegree ):
      return ""

   return ''.join( sortedOrder )

testCases = [
      { 'words' : [ "ba", "bc", "ac", "cab" ],
        'output' : 'bac' },
      { 'words' : [ "cab", "aaa", "aab" ],
        'output' : 'cab' },
      { 'words' : [ "ywx", "wz", "xww", "xz", "zyy", "zwz" ],
        'output' : 'ywxz' },
]

for test in testCases:
   w = test[ 'words' ]
   o = test[ 'output' ]
   assert( dictionary( w ) == o )
