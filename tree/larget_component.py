#!/usr/bin/env python3

from collections import defaultdict

# Write a function, largestComponent, that takes in the adjacency list of an
# undirected graph. The function should return the size of the largest connected
# component in the graph.

def largestComponent( graph ):
   stack = []
   visited = {}
   components = defaultdict( list )

   count = 0
   for node, _ in graph.items():
      if not visited.get( node, None ):
         stack.append( node )

         while len( stack ) != 0:
            cur = stack.pop()
            if not cur in components[ count ]:
               components[ count ].append( cur )
            visited[ cur ] = True

            for n in graph[ cur ]:
               if not visited.get( n, None ):
                  stack.append( n )

         count += 1

   maxCount = 0
   for _, members in components.items():
      if maxCount < len( members ):
         maxCount = len( members )

   return maxCount

if __name__ == '__main__':
   testCases = [
         {
            'graph' : {
               0 : [ 8, 1, 5 ],
               1 : [ 0 ],
               5 : [ 0, 8 ],
               8 : [ 0, 5 ],
               2 : [ 3, 4 ],
               3 : [ 2, 4 ],
               4 : [ 3, 2 ],
            },
            'answer' : 4,
         },
         {
            'graph' : {
               1 : [ 2 ],
               2 : [ 1, 8 ],
               6 : [ 7 ],
               9 : [ 8 ],
               7 : [ 6, 8 ],
               8 : [ 9, 7, 2 ],
            },
            'answer' : 6,
         },
         {
            'graph' : {
               3 : [],
               4 : [ 6 ],
               6 : [ 4, 5, 7, 8 ],
               8 : [ 6 ],
               7 : [ 6 ],
               5 : [ 6 ],
               1 : [ 2 ],
               2 : [ 1 ],
            },
            'answer' : 5,
         },
         {
            'graph' : {},
            'answer' : 0,
         },
         {
            'graph' : {
               0 : [ 4, 7 ],
               1 : [],
               2 : [],
               3 : [ 6 ],
               4 : [ 0 ],
               6 : [ 3 ],
               7 : [ 0 ],
               8 : [],
            },
            'answer' : 3,
         },
   ]

   for test in testCases:
      graph = test[ 'graph' ]
      answer = test[ 'answer' ]
      assert( answer == largestComponent( graph ) )
