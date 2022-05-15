#!/usr/bin/env python
# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task
# can have some prerequisite tasks which need to be completed
# before it can be scheduled. Given the number of tasks and a
# list of prerequisite pairs, find out if it is possible to
# schedule all the tasks.
from collections import deque

def check( tasks, prereqs ):
   sortedOrder = []
   inDegree = { i : 0 for i in range( tasks ) }
   adjacencyList = { i : [] for i in range( tasks ) }

   for p in prereqs:
      src, dst = p[ 0 ], p[ 1 ]
      inDegree[ dst ] += 1
      adjacencyList[ src ].append( dst )

   sources = [ i for i, v in inDegree.items() if v == 0 ]
   sources = deque( sources )

   while sources:
      src = sources.popleft()
      sortedOrder.append( src )
      for s in adjacencyList[ src ]:
         inDegree[ s ] -= 1
         if inDegree[ s ] == 0:
            sources.append( s )

   return len( sortedOrder ) == tasks

testCases = [
      { 'tasks' : 3,
        'prerequisites' : [ [0, 1], [1, 2] ] },
      { 'tasks' : 3,
        'prerequisites' : [ [0, 1], [1, 2], [2, 0] ] },
      { 'tasks' : 6,
        'prerequisites' : [ [2, 5], [0, 5], [0, 4], [1, 4],
                            [3, 2], [1, 3] ] },
]

for test in testCases:
   t = test[ 'tasks' ]
   p = test[ 'prerequisites' ]
   print( check( t, p ) )
   print()
