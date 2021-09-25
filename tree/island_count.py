#!/usr/bin/env python3

# https://structy.net/problems/island-count
#
# Write a function, islandCount, that takes in a grid containing Ws and Ls. W
# represents water and L represents land. The function should return the number of
# islands on the grid. An island is a vertically or horizontally connected region of
# land.

def islandCount( grid ):
   row = len( grid )
   col = len( grid[ 0 ] )
   visited = [ [ False for i in range( 0, col ) ] for j in range( 0, row ) ]

   stack = []
   count = 0
   for i in range( 0, row ):
      for j in range( 0, col ):
         if grid[ i ][ j ] == 'W':
            visited[ i ][ j ] = True
            continue

         if not visited[ i ][ j ]:
            stack.append( ( i, j ) )
            count += 1
         while len( stack ) != 0:
            cur = stack.pop()
            x = cur[ 0 ]
            y = cur[ 1 ]
            visited[ x ][ y ] = True

            if x - 1 >= 0 and not visited[ x - 1 ][ y ] and grid[ x - 1 ][ y ] == 'L':
               stack.append( ( x - 1, y ) )
            if x + 1 < row and not visited[ x + 1 ][ y ] and grid[ x + 1 ][ y ] == 'L':
               stack.append( ( x + 1, y ) )
            if y - 1 >= 0 and not visited[ x ][ y - 1 ] and grid[ x ][ y - 1 ] == 'L':
               stack.append( ( x, y - 1 ) )
            if y + 1 < col and not visited[ x ][ y + 1 ] and grid[ x ][ y + 1 ] == 'L':
               stack.append( ( x, y + 1 ) )

   return count

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
            'answer' : 3,
         },
         {
            'grid' : [
               ['L', 'W', 'W', 'L', 'W'],
               ['L', 'W', 'W', 'L', 'L'],
               ['W', 'L', 'W', 'L', 'W'],
               ['W', 'W', 'W', 'W', 'W'],
               ['W', 'W', 'L', 'L', 'L'],
            ],
            'answer' : 4,
         },
         {
            'grid' : [
               ['L', 'L', 'L'],
               ['L', 'L', 'L'],
               ['L', 'L', 'L'],
            ],
            'answer' : 1,
         },
         {
            'grid' : [
               ['W', 'W'],
               ['W', 'W'],
               ['W', 'W'],
            ],
            'answer' : 0,
         },
   ]

   for test in testCases:
      grid = test[ 'grid' ]
      answer = test[ 'answer' ]
      islandCount( grid )
      assert( answer == islandCount( grid ) )
