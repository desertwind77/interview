#!/usr/bin/env python
# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can
# have some prerequisite tasks which need to be completed before
# it can be scheduled. Given the number of tasks and a list of
# prerequisite pairs, write a method to print all possible ordering
# of tasks meeting all prerequisites.

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
   #sources = deque( sources )

   for i in range( len( sources ) ):
      doPrint( i, vertices, sources, inDegree, adjacencyList, result )

def doPrint( i, vertices, sources, inDegree, adjacencyList, result ):
   newSources = sources[:]
   vertex = newSources.pop( i )
   result.append( vertex )

   for c in adjacencyList[ vertex ]:
      inDegree[ c ] -= 1
      if inDegree[ c ] == 0:
         newSources.append( c )

   for s  in range( len( newSources ) ):
      doPrint( s, vertices, newSources, inDegree, adjacencyList, result )

   if len( result ) == vertices:
      print( result )

   result.pop( - 1 )
   for c in adjacencyList[ vertex ]:
      inDegree[ c ] += 1


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
