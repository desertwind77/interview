#!/usr/bin/env python3

# https://structy.net/problems/connected-components-count
# Write a function, connectedComponentsCount, that takes in the adjacency list of an
# undirected graph. The function should return the number of connected components
# within the graph.

def connectedComponentsCount( graph ):
   stack = []
   visited = {}

   count = 0
   for node, _ in graph.items():
      if not visited.get( node, None ):
         stack.append( node )
         count += 1

         while len( stack ) != 0:
            cur = stack.pop()
            visited[ cur ] = True

            for n in graph[ cur ]:
               if not visited.get( n, None ):
                  stack.append( n )

   return count

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
            'answer' : 2,
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
            'answer' : 1,
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
            'answer' : 3,
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
            'answer' : 5,
         },
   ]

   for test in testCases:
      graph = test[ 'graph' ]
      answer = test[ 'answer' ]
      assert( answer == connectedComponentsCount( graph ) )
