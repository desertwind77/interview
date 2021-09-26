#!/usr/bin/env python3

# https://structy.net/problems/undirected-path
# Write a function, undirectedPath, that takes in an array of edges for an undirected
# graph and two nodes (nodeA, nodeB). The function should return a boolean indicating
# whether or not there exists a path between nodeA and nodeB.

from collections import defaultdict
from has_path import hasPath

def undirectedPath( edges, nodeA, nodeB ):
   graph = defaultdict( list ) 
   for e in edges:
      node1 = e[ 0 ]
      node2 = e[ 1 ]
      graph[ node1 ].append( node2 )
      graph[ node2 ].append( node1 )

   return hasPath( graph, nodeA, nodeB )

if __name__ == '__main__':
   testCases = [
         {
            'edges' : [ [ 'i', 'j' ], [ 'k', 'i' ], [ 'm', 'k' ],
                       [ 'k', 'l' ], [ 'o', 'n' ] ],
            'src' : 'j',
            'dst' : 'm',
            'answer' : True,
         },
         {
            'edges' : [ [ 'i', 'j' ], [ 'k', 'i' ], [ 'm', 'k' ],
                       [ 'k', 'l' ], [ 'o', 'n' ] ],
            'src' : 'm',
            'dst' : 'j',
            'answer' : True,
         },
         {
            'edges' : [ [ 'i', 'j' ], [ 'k', 'i' ], [ 'm', 'k' ],
                       [ 'k', 'l' ], [ 'o', 'n' ] ],
            'src' : 'l',
            'dst' : 'j',
            'answer' : True,
         },
         {
            'edges' : [ [ 'i', 'j' ], [ 'k', 'i' ], [ 'm', 'k' ],
                       [ 'k', 'l' ], [ 'o', 'n' ] ],
            'src' : 'k',
            'dst' : 'o',
            'answer' : False,
         },
         {
            'edges' : [ [ 'i', 'j' ], [ 'k', 'i' ], [ 'm', 'k' ],
                       [ 'k', 'l' ], [ 'o', 'n' ] ],
            'src' : 'i',
            'dst' : 'o',
            'answer' : False,
         },
         {
            'edges' : [ [ 'b', 'a' ], [ 'c', 'a' ], [ 'b', 'c' ],
                       [ 'q', 'r' ], [ 'q', 's' ], [ 'q', 'u' ], [ 'q', 't' ] ],
            'src' : 'a',
            'dst' : 'b',
            'answer' : True,
         },
         {
            'edges' : [ [ 'b', 'a' ], [ 'c', 'a' ], [ 'b', 'c' ],
                       [ 'q', 'r' ], [ 'q', 's' ], [ 'q', 'u' ], [ 'q', 't' ] ],
            'src' : 'a',
            'dst' : 'c',
            'answer' : True,
         },
         {
            'edges' : [ [ 'b', 'a' ], [ 'c', 'a' ], [ 'b', 'c' ],
                       [ 'q', 'r' ], [ 'q', 's' ], [ 'q', 'u' ], [ 'q', 't' ] ],
            'src' : 'r',
            'dst' : 't',
            'answer' : True,
         },
         {
            'edges' : [ [ 'b', 'a' ], [ 'c', 'a' ], [ 'b', 'c' ],
                       [ 'q', 'r' ], [ 'q', 's' ], [ 'q', 'u' ], [ 'q', 't' ] ],
            'src' : 'r',
            'dst' : 'b',
            'answer' : False,
         },
   ]

   for test in testCases:
      edges = test[ 'edges']
      src = test[ 'src' ]
      dst = test[ 'dst' ]
      answer = test[ 'answer' ]
      assert( answer == undirectedPath( edges, src, dst ) )
