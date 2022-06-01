#!/usr/bin/env python
# Level Averages in a Binary Tree (easy)
#
# Given a binary tree, populate an array to represent the averages of all of its
# levels.

from collections import deque

class TreeNode:
   def __init__(self, val):
      self.val = val
      self.left, self.right = None, None

def find_level_averages1( root ):
   # time = O(N)
   # space = O(N)
   result = []
   if root is None:
      return result

   queue = deque()
   queue.append( root )
   queue.append( None )

   curLevel = []
   while queue:
      top = queue.popleft()
      if top:
         if top.left:
            queue.append( top.left )
         if top.right:
            queue.append( top.right )
         curLevel.append( top.val )
      elif queue:
         curAvg = round( sum( curLevel ) * 1.0 / len( curLevel ), 2 )
         result.append( curAvg )
         curLevel = []
         queue.append( None )
   curAvg = round( sum( curLevel ) * 1.0 / len( curLevel ), 2 )
   result.append( curAvg )

   return result

def find_level_averages2( root ):
   # time = O(N)
   # space = O(N)
   result = []
   if root is None:
      return result

   queue = deque()
   queue.append( root )

   while queue:
      levelSize = len( queue )
      levelSum = 0.0

      for _ in range( levelSize ):
         top = queue.popleft()
         levelSum += top.val

         if top.left:
            queue.append( top.left )
         if top.right:
            queue.append( top.right )
      result.append( levelSum / levelSize )

   return result

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(9)
   root.left.right = TreeNode(2)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   print("Level averages are: " + str(find_level_averages1(root)))
   print("Level averages are: " + str(find_level_averages2(root)))

main()
