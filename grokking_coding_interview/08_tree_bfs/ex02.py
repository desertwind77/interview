#!/usr/bin/env python
# Reverse Level Order Traversal (easy)
#
# Given a binary tree, populate an array to represent its level-by-level traversal in
# reverse order, i.e., the lowest level comes first. You should populate the values
# of all nodes in each level from left to right in separate sub-arrays.

from collections import deque


class TreeNode:
   def __init__(self, val):
      self.val = val
      self.left, self.right = None, None

def traverse1( root ):
   # time = O(N)
   # space = O(N)
   result = deque()
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
         result.appendleft( curLevel )
         curLevel = []
         queue.append( None )
   result.appendleft( curLevel )

   return list( result )

def traverse2( root ):
   # time = O(N)
   # space = O(N)
   result = deque()
   if root is None:
      return result

   queue = deque()
   queue.append( root )
   while queue:
      levelSize = len( queue )
      curLevel = []
      for _ in range( levelSize ):
         top = queue.popleft()
         curLevel.append( top.val )
         if top.left:
            queue.append( top.left )
         if top.right:
            queue.append( top.right )
      result.appendleft( curLevel )

   return list( result )

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(9)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   print("Reverse level order traversal: " + str(traverse1(root)))
   print("Reverse level order traversal: " + str(traverse2(root)))

main()
