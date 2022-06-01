#!/usr/bin/env python
# Binary Tree Level Order Traversal (easy)
#
# Given a binary tree, populate an array to represent its level-by-level traversal.
# You should populate the values of all nodes of each level from left to right in
# separate sub-arrays.

from collections import deque

class TreeNode:
   def __init__(self, val):
      self.val = val
      self.left, self.right = None, None

def traverse1( root ):
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
      root = queue.popleft()
      if root:
         if root.left:
            queue.append( root.left )
         if root.right:
            queue.append( root.right )

         curLevel.append( root.val )
      elif queue:
         result.append( curLevel )
         curLevel = []
         queue.append( None )

   result.append( curLevel )

   return result

def traverse2( root ):
   result = []
   if root is None:
      return result

   queue = deque()
   queue.append( root )

   while queue:
      levelSize = len( queue )
      curLevel = []

      for _ in range( levelSize ):
         curNode = queue.popleft()
         curLevel.append( curNode.val )

         if curNode.left:
            queue.append( curNode.left )
         if curNode.right:
            queue.append( curNode.right )

      result.append( curLevel )

   return result

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(9)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   print("Level order traversal: " + str(traverse1(root)))
   print("Level order traversal: " + str(traverse2(root)))

main()
