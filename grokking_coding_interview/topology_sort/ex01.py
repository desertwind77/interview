#!/usr/bin/env python
# Topological Sort of a directed graph (a graph with unidirectional
# edges) is a linear ordering of its vertices such that for every
# directed edge (U, V) from vertex U to vertex V, U comes before
# V in the ordering.
#
# Given a directed graph, find the topological ordering of its vertices.
from collections import deque

# This cannot handle graphs with a cycle
def topology_sort_dfs( vertices, edges ):
   ''' Topology sort using DFS'''
   def doVisit( i, edges, visited, stack ):
      visited[ i ] = True
      myEdges = [ x[ 1 ] for x in edges if x[ 0 ] == i ]
      for e in myEdges:
         if not visited[ e ]:
            doVisit( e, edges, visited, stack )
      stack.append( i )

   visited = [ False ] * vertices
   stack = []
   for i in range( vertices ):
      if not visited[ i ]:
         doVisit( i, edges, visited, stack )

   return [ i for i in reversed( stack ) ]

def topology_sort_bfs( vertices, edges ):
   sortedOrder = []
   if vertices <= 0:
      return sortedOrder

   # Initialize the graph
   inDegree = { i : 0 for i in range( vertices ) }
   adjacencyList= { i : [] for i in range( vertices ) }
   for e in edges:
      src, dst = e[ 0 ], e[ 1 ]
      inDegree[ dst ] += 1
      adjacencyList[ src ].append( dst )

   # Find all source of which inDegree = 0
   sources = [ n for n, v in inDegree.items() if v == 0 ]
   sources = deque( sources )

   # For each source, add it to sortedOrder and subtract 1 from all of its children's
   # in-degrees. If the child's in-degree becomes 0, add it to sources.
   while sources:
      vertex = sources.popleft()
      sortedOrder.append( vertex )
      for child in adjacencyList[ vertex ]:
         inDegree[ child ] -= 1
         if inDegree[ child ] == 0:
            sources.append( child )

   # topological sort is not possible because the graph has a cycle
   if len( sortedOrder ) != vertices:
      return []

   return sortedOrder

testCases = [
      { 'vertices' : 4,
        'edges' : [ [3, 2], [3, 0], [2, 0], [2, 1] ] },
      { 'vertices' : 5,
        'edges' : [ [4, 2], [4, 3], [2, 0], [2, 1], [3, 1] ] },
      { 'vertices' : 7,
        'edges' : [ [6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1] ] },
      { 'vertices' : 6,
        'edges' : [ [5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1 ] ] },
]

for test in testCases:
   v = test[ 'vertices' ]
   e = test[ 'edges' ]
   print( topology_sort_dfs( v, e ) )
   print( topology_sort_bfs( v, e ) )
   print()
