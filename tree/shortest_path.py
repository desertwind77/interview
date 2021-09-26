#!/usr/bin/env python3

# https://structy.net/problems/shortest-path
# Write a function, shortestPath, that takes in an array of edges for an undirected
# graph and two nodes (nodeA, nodeB). The function should return the length of the
# shortest path between A and B. Consider the length as the number of edges in the
# path, not the number of nodes. If there is no path between A and B, then return -1.

from collections import defaultdict
from min_heap1 import MinHeap

class Node:
   def __init__( self, name, cost ):
      self.name = name
      self.cost = cost

   def __lt__( self, other ):
      return self.cost < other.cost

def shortestPath( edges, src, dst ):
   graph = defaultdict( list )

   for e in edges:
      n0 = e[ 0 ]
      n1 = e[ 1 ]
      graph[ n0 ].append( n1 )
      graph[ n1 ].append( n0 )
   graph = dict( graph )

   queue = MinHeap()
   visited = {}
   distance = defaultdict( int )

   queue.insertKey( Node( src, 0 ) )
   while len( queue.heap ) != 0:
      cur = queue.extractMin()
      visited[ cur.name ] = True
      if distance[ cur.name ] == 0 or distance[ cur.name ] > cur.cost:
         distance[ cur.name ] = cur.cost

      neighbors = graph[ cur.name ]
      for n in neighbors:
         if not visited.get( n, None ):
            queue.insertKey( Node( n, cur.cost + 1 ) )

   return distance.get( dst, - 1 )

if __name__ == '__main__':
   testCases = [
         {
            'edges' : [ [ 'w', 'x' ], [ 'x', 'y' ], [ 'z', 'y' ],
                        [ 'z', 'v' ], [ 'w', 'v' ] ],
            'src' : 'w',
            'dst' : 'z',
            'answer' : 2,
         },
         {
            'edges' : [ [ 'w', 'x' ], [ 'x', 'y' ], [ 'z', 'y' ],
                        [ 'z', 'v' ], [ 'w', 'v' ] ],
            'src' : 'y',
            'dst' : 'x',
            'answer' : 1,
         },
         {
            'edges' : [ [ 'a', 'c' ], [ 'a', 'b' ], [ 'c', 'b' ], [ 'c', 'd' ],
                        [ 'b', 'd' ], [ 'e', 'd' ], [ 'g', 'f' ] ],
            'src' : 'a',
            'dst' : 'e',
            'answer' : 3,
         },
         {
            'edges' : [ [ 'a', 'c' ], [ 'a', 'b' ], [ 'c', 'b' ], [ 'c', 'd' ],
                        [ 'b', 'd' ], [ 'e', 'd' ], [ 'g', 'f' ] ],
            'src' : 'e',
            'dst' : 'c',
            'answer' : 2,
         },
         {
            'edges' : [ [ 'a', 'c' ], [ 'a', 'b' ], [ 'c', 'b' ], [ 'c', 'd' ],
                        [ 'b', 'd' ], [ 'e', 'd' ], [ 'g', 'f' ] ],
            'src' : 'b',
            'dst' : 'g',
            'answer' : -1,
         },
         {
            'edges' : [ [ 'c', 'n' ], [ 'c', 'e' ], [ 'c', 's' ],
                        [ 'c', 'w' ], [ 'w', 'e' ] ],
            'src' : 'w',
            'dst' : 'e',
            'answer' : 1,
         },
         {
            'edges' : [ [ 'c', 'n' ], [ 'c', 'e' ], [ 'c', 's' ],
                        [ 'c', 'w' ], [ 'w', 'e' ] ],
            'src' : 'n',
            'dst' : 'e',
            'answer' : 2,
         },
         {
            'edges' : [ [ 'm', 'n' ], [ 'n', 'o' ], [ 'o', 'p' ], [ 'p', 'q' ],
                        [ 't', 'o' ], [ 'r', 'q' ], [ 'r', 's' ] ],
            'src' : 'm',
            'dst' : 's',
            'answer' : 6,
         },
   ]

   for test in testCases:
      edges = test[ 'edges' ]
      src = test[ 'src' ]
      dst = test[ 'dst' ]
      answer = test[ 'answer' ]
      assert( answer == shortestPath( edges, src, dst ) )
