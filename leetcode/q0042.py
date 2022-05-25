#!/usr/bin/env python3
# Leetcode 42 : Trapping Rain Water
# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.

def trapBruteForce( height ):
   # time = O( n^2 )
   # space = O( 1 )
   size = len( height )

   trap = 0
   for i in range( size ):
      maxLeft, maxRight = 0, 0

      for j in range( i-1, -1, -1 ):
         if height[ j ] > maxLeft:
            maxLeft = height[ j ]

      for k in range( i+1, size ):
         if height[ k ] > maxRight:
            maxRight = height[ k ]

      curMaxHeight = min( maxLeft, maxRight )
      if curMaxHeight > height[ i ]:
         trap += curMaxHeight - height[ i ]

   return trap

def trapDynamicProgramming( height ):
   # time = O( n )
   # space = O( n )
   # index  : 0 1 2 3 4 5 6 7 8 9 10 11
   # height : 0 1 0 2 1 0 1 3 2 1  2  1
   # left   : 0 0 1 1 2 2 2 3 3 3  3  3
   # right  : 3 3 3 3 3 3 3 2 2 2  1  0
   # curMax : 0 0 1 1 2 2 2 2 2 2  1  0
   size = len( height )
   left, right = [0]*size, [0]*size

   left[ 0 ] = 0
   for i in range( 1, size ):
      left[ i ] = max( left[ i-1 ], height[ i-1] )

   right[ size - 1 ] = 0
   for i in range( size - 2, -1, -1 ):
      right[ i ] = max( right[ i+1 ], height[ i+1 ] )

   trap = 0
   for i in range( size ):
      if left[ i ] != 0 and right[ i ] != 0:
         curMaxHeight = min( left[ i ], right[ i ] )
         if curMaxHeight > height[ i ]:
            trap += curMaxHeight - height[ i ]

   return trap

def trapStack( height ):
   # time = O(n)
   # space = O(n)
   # very very very complicated
   size = len( height )
   stack = []
   trap = 0

   # index  : 0 1 2 3 4 5 6 7 8 9 10 11
   # height : 0 1 0 2 1 0 1 3 2 1  2  1
   # i   stack    pop   distance    curHeight                              stack
   # 0   []                                                                0
   # 1   0        0                                                        1
   # 2   1                                                                 1,2
   # 3   1,2      2     3-1-1=1     min(h[1],h[3])-h[2] = min(1,2)-0 = 1   1
   #     1        1                                                        3
   # 4   3                                                                 3,4
   # 5   3,4                                                               3,4,5
   # 6   3,4,5    5     6-4-1=1     min(h[4],h[6])-h[5] = min(1,1)-0 = 1   3,4,6
   # 7   3,4,6    6     7-4-1=2     min(h[4],h[7])-h[6] = min(1,3)-1 = 0   3,4
   #     3,4      4     7-3-1=3     min(h[3],h[7])-h[4] = min(2,3)-1 = 1   3
   #     3                                                                 7
   # 8   7                                                                 7,8
   # 9   7,8                                                               7,8,9
   # 10  7,8,9    9     10-8-1=1    min(h[10],h[8])-h[9] = min(2,2)-1 = 1  7,8,10
   # 11  7,8,10                                                            7,8,10,11
   for i in range( size ):
      while stack and height[ i ] > height[ stack[ -1 ] ]:
         top = stack.pop( -1 )
         if not stack:
            break
         distance = i - stack[ -1 ] - 1
         curHeight = min( height[ stack[ -1 ] ], height[ i ] ) - height[ top ]
         trap += distance * curHeight
      stack.append( i )

   return trap

def trapTwoPointer( height ):
   # time = O( n )
   # space = O( 1 )
   # There is two borders: left and right. The level of trapped water depends on
   # min( height[ left ], height[ right ] ). If height[ left ] < height[ right ],
   # move left up by 1 and vice versa. Once either left or right reaches the peak,
   # it will never move again. The other end will move toward it.
   size = len( height )
   left, right = 0, size - 1
   leftMax, rightMax = 0, 0

   trap = 0
   while left < right:
      if height[ left ] < height[ right ]:
         if height[ left ] >= leftMax:
            leftMax = height[ left ]
         else:
            trap += leftMax - height[ left ]
         left += 1
      else:
         if height[ right ] >= rightMax:
            rightMax = height[ right ]
         else:
            trap += rightMax - height[ right ]
         right -= 1

   return trap

testCases = [
      {
         'height' : [0,1,0,2,1,0,1,3,2,1,2,1],
         'output' : 6,
      },
      {
         'height' : [4,2,0,3,2,5],
         'output' : 9,
      },
]

for test in testCases:
   h = test[ 'height' ]
   o = test[ 'output' ]
   assert( trapBruteForce( h ) == o )
   assert( trapDynamicProgramming( h ) == o )
   assert( trapStack( h ) == o )
   assert( trapTwoPointer( h ) == o )
