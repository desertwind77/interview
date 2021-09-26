#!/usr/bin/env python3

from collections import defaultdict

# https://structy.net/problems/minimum-island
# Write a function, minimumIsland, that takes in a grid containing Ws and Ls. W
# represents water and L represents land. The function should return the size of the
# smallest island. An island is a vertically or horizontally connected region of
# land.
#
# You may assume that the grid contains at least one island.

def minimumIsland( grid ):
   row = len( grid )
   col = len( grid[ 0 ] )
   visited = [ [ False for _ in range( 0, col ) ] for _ in range( 0, row ) ]
   islands = defaultdict( list )


   stack = []
   count = 0
   for i in range( 0, row ):
      for j in range( 0, col ):
         if visited[ i ][ j ]:
            continue
         if grid[ i ][ j ] == 'W':
            visited[ i ][ j ]  = True
            continue

         stack.append( ( i, j ) )
         while len( stack ) != 0:
            cur = stack.pop()
            x = cur[ 0 ]
            y = cur[ 1 ]
            visited[ x ][ y ] = True
            if cur not in islands[ count ]:
               islands[ count ].append( cur )

            u = x - 1
            d = x + 1
            l = y - 1
            r = y + 1
            if u >= 0 and not visited[ u ][ y ] and grid[ u ][ y ] == 'L':
               stack.append( ( u, y ) )
            if d < row and not visited[ d ][ y ] and grid[ d ][ y ] == 'L':
               stack.append( ( d, y ) )
            if l >= 0 and not visited[ x ][ l ] and grid[ x ][ l ] == 'L':
               stack.append( ( x, l ) )
            if r < col and not visited[ x ][ r ] and grid[ x ][ r ] == 'L':
               stack.append( ( x, r ) )
         count += 1

   minIsland = -1
   for _, i in islands.items():
      size = len( i )
      if minIsland < 0 or minIsland > size:
         minIsland = size

   return minIsland

if __name__ == '__main__':
   testCases = [
         {
            'grid' : [
               ['W', 'L', 'W', 'W', 'W'],
               ['W', 'L', 'W', 'W', 'W'],
               ['W', 'W', 'W', 'L', 'W'],
               ['W', 'W', 'L', 'L', 'W'],
               ['L', 'W', 'W', 'L', 'L'],
               ['L', 'L', 'W', 'W', 'W'],
            ],
            'answer' : 2,
         },
         {
            'grid' : [
               ['L', 'W', 'W', 'L', 'W'],
               ['L', 'W', 'W', 'L', 'L'],
               ['W', 'L', 'W', 'L', 'W'],
               ['W', 'W', 'W', 'W', 'W'],
               ['W', 'W', 'L', 'L', 'L'],
            ],
            'answer' : 1,
         },
         {
            'grid' : [
               ['L', 'L', 'L'],
               ['L', 'L', 'L'],
               ['L', 'L', 'L'],
            ],
            'answer' : 9,
         },
         {
            'grid' : [
               ['W', 'W'],
               ['L', 'L'],
               ['W', 'W'],
               ['W', 'L']
            ],
            'answer' : 1,
         },
   ]

   for test in testCases:
      grid = test[ 'grid' ]
      answer = test[ 'answer' ]
      assert( answer == minimumIsland( grid ) )
