#!/usr/bin/env python
# Given a sequence originalSeq and an array of sequences,
# write a method to find if originalSeq can be uniquely
# reconstructed from the array of sequences.
#
# Unique reconstruction means that we need to find if
# originalSeq is the only sequence such that all
# sequences in the array are subsequences of it.
from collections import deque

def canConstruct( originalSeq, seqs ):
   if not originalSeq:
      return False

   sortedOrder = []
   inDegree = {}
   graph = {}
   for seq in seqs:
      for n in seq:
         inDegree[ n ] = 0
         graph[ n ] = []

   for seq in seqs:
      for i in range( 0, len( seq ) - 1 ):
         u = seq[ i ]
         v = seq[ i + 1 ]
         inDegree[ v ] += 1
         graph[ u ].append( v )

   # Rule #1 : if we don't have ordering rules for all
   # the numbers we'll not able to uniquely construct
   # the sequence
   if len( inDegree ) != len( originalSeq ):
      return False

   sources = deque( [ x for x, v in inDegree.items() if v == 0 ] )

   while sources:
      # Rule #2 : more than one sources mean, there is
      # more than one way to reconstruct the sequence
      if len( sources ) > 1:
         return False

      # Rule #3 : the next source(or number) is different
      # from the original sequence
      if originalSeq[ len( sortedOrder ) ] != sources[ 0 ]:
         return False

      vertex = sources.popleft()
      sortedOrder.append( vertex )
      for c in graph[ vertex ]:
         inDegree[ c ] -= 1
         if inDegree[ c ] == 0:
            sources.append( c )

   # Rule #4 : if sortedOrder's size is not equal to original
   # sequence's size, there is no unique way to construct
   return len( sortedOrder ) == len( originalSeq )

testCases = [
      { "originalSeq" : [1, 2, 3, 4],
        "seqs" : [ [1, 2], [2, 3], [3, 4] ],
        "answer" : True, },
      { "originalSeq" : [1, 2, 3, 4],
        "seqs" : [ [1, 2], [2, 3], [2, 4] ],
        "answer" : False, },
      { "originalSeq" : [3, 1, 4, 2, 5],
        "seqs" : [ [3, 1, 5], [1, 4, 2, 5] ],
        "answer" : True, },
]

for test in testCases:
   o = test[ 'originalSeq' ]
   s = test[ 'seqs' ]
   a = test[ 'answer' ]
   assert( canConstruct( o, s ) == a )

