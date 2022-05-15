#!/usr/bin/env python
# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can
# have some prerequisite tasks which need to be completed before
# it can be scheduled. Given the number of tasks and a list of
# prerequisite pairs, write a method to print all possible ordering
# of tasks meeting all prerequisites.
from collections import deque

def all_topology_sort_bfs( vertices, edges ):
   if vertices <= 0:
      return False

   # Initialization
   result = []
   inDegree = { i : 0 for i in range( vertices ) }
   adjacencyList= { i : [] for i in range( vertices ) }
   for e in edges:
      src, dst = e[ 0 ], e[ 1 ]
      inDegree[ dst ] += 1
      adjacencyList[ src ].append( dst )

   # Find all source of which inDegree = 0
   sources = [ n for n, v in inDegree.items() if v == 0 ]
   sources = deque( sources )

   doPrint( adjacencyList, inDegree, sources, result )

def doPrint( graph, inDegree, sources, sortedOrder ):
   if sources:
      for vertex in sources:
         sortedOrder.append( vertex )
         sourcesForNextCall = deque( sources )
         sourcesForNextCall.remove( vertex )

         for child in graph[ vertex ]:
            inDegree[ child ] -= 1
            if inDegree[ child ] == 0:
               sourcesForNextCall.append( child )

         doPrint( graph, inDegree, sourcesForNextCall, sortedOrder )

         sortedOrder.remove( vertex )
         for child in graph[ vertex ]:
            inDegree[ child ] += 1

   if len( sortedOrder ) == len( inDegree ):
      print( sortedOrder )

testCases = [
      { 'vertices' : 3,
        'edges' : [ [0, 1], [1, 2] ] },
      { 'vertices' : 4,
        'edges' : [ [3, 2], [3, 0], [2, 0], [2, 1] ] },
      { 'vertices' : 6,
        'edges' : [ [2, 5], [0, 5], [0, 4], [1, 4],
                    [3, 2], [1, 3 ] ] },
]

for test in testCases:
   v = test[ 'vertices' ]
   e = test[ 'edges' ]
   all_topology_sort_bfs( v, e )
   print()
