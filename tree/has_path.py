#!/usr/bin/env python3

# https://structy.net/problems/has-path
# Write a function, hasPath, that takes in an object representing the adjacency list
# of a directed acyclic graph and two nodes (src, dst). The function should return a
# boolean indicating whether or not there exists a directed path between the source
# and destination nodes.

def hasPath( graph, src, dst ):
   # Using DFS
   stack = [ src ]
   visited = {}

   while len( stack ) != 0:
      cur = stack.pop()

      neighbors = graph[ cur ]
      for i in neighbors:
         if i == dst:
            return True
         stack.append( i )

      visited[ cur ] = True

   return False

if __name__ == '__main__':
   testCases = [
         {
            'graph' : {
               'f' : [ 'g', 'i' ],
               'g' : [ 'h' ],
               'h' : [],
               'i' : [ 'g', 'k' ],
               'j' : [ 'i' ],
               'k' : [],
            },
            'src' : 'f',
            'dst' : 'k',
            'answer' : True,
         },
         {
            'graph' : {
               'f' : [ 'g', 'i' ],
               'g' : [ 'h' ],
               'h' : [],
               'i' : [ 'g', 'k' ],
               'j' : [ 'i' ],
               'k' : [],
            },
            'src' : 'f',
            'dst' : 'j',
            'answer' : False,
         },
         {
            'graph' : {
               'f' : [ 'g', 'i' ],
               'g' : [ 'h' ],
               'h' : [],
               'i' : [ 'g', 'k' ],
               'j' : [ 'i' ],
               'k' : [],
            },
            'src' : 'i',
            'dst' : 'h',
            'answer' : True,
         },
         {
            'graph' : {
               'v' : [ 'x', 'w' ],
               'w' : [],
               'x' : [],
               'y' : [ 'z' ],
               'z' : [],
            },
            'src' : 'v',
            'dst' : 'w',
            'answer' : True,
         },
         {
            'graph' : {
               'v' : [ 'x', 'w' ],
               'w' : [],
               'x' : [],
               'y' : [ 'z' ],
               'z' : [],
            },
            'src' : 'v',
            'dst' : 'z',
            'answer' : False,
         },
   ]

   for test in testCases:
      graph = test[ 'graph' ]
      src = test[ 'src' ]
      dst = test[ 'dst' ]
      answer = test[ 'answer' ]
      assert( answer == hasPath( graph, src, dst ) )
