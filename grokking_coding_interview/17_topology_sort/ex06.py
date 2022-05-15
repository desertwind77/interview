#!/usr/bin/env python
# We are given an undirected graph that has characteristics
# of a k-ary tree. In such a graph, we can choose any node
# as the root to make a k-ary tree. The root (or the tree)
# with the minimum height will be called Minimum Height Tree
# (MHT). There can be multiple MHTs for a graph. In this problem,
# we need to find all those roots which give us MHTs.
# Write a method to find all MHTs of the given graph and
# return a list of their roots.
from collections import deque

def findTrees( vertices, edges ):
   if vertices <= 0:
      return []
   elif vertices == 1:
      # When there is only one node, its inDegree is 0. The algorithm
      # cannot handle this. So we need to handle it here.
      return [ 0 ]

   inDegree = { i: 0 for i in range( vertices ) }
   graph = { i: [] for i in range( vertices ) }
   for edge in edges:
      m, n = edge[ 0 ], edge[ 1 ]
      inDegree[ m ] += 1
      inDegree[ n ] += 1
      graph[ m ].append( n )
      graph[ n ].append( m )

   leaves = deque( [ n for n, v in inDegree.items() if v == 1 ] )

   numNodes = vertices
   while numNodes > 2:
      numLeaves = len( leaves )
      numNodes -= numLeaves

      for _ in range( numLeaves ):
         u = leaves.popleft()
         inDegree[ u ] -= 1
         for v in graph[ u ]:
            inDegree[ v ] -= 1
            if inDegree[ v ] == 1:
               leaves.append( v )

   return list( leaves )

testCases = [
      { "vertices" : 5,
        "edges" : [ [ 0, 1 ], [ 1, 2 ], [ 1, 3 ], [ 2, 4 ] ],
        "output" : [ 1, 2 ], },
      { "vertices" : 4,
        "edges" : [ [ 0, 1 ], [ 0, 2 ], [ 2, 3 ] ],
        "output" : [ 0, 2 ], },
      { "vertices" : 4,
        "edges" : [ [ 0, 1 ], [ 1, 2 ], [ 1, 3 ] ],
        "output" : [ 1 ], },
]

for test in testCases:
   v = test[ 'vertices' ]
   e = test[ 'edges' ]
   o = test[ 'output' ]
   assert( findTrees( v, e ) == o )

