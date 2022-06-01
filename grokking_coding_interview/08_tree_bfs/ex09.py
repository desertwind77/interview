#!/usr/bin/env python
# Right View of a Binary Tree (easy)
#
# Given a binary tree, return an array containing nodes in its right view. The right
# view of a binary tree is the set of nodes visible when the tree is seen from the
# right side.

from __future__ import print_function
from collections import deque

class TreeNode:
   def __init__(self, val):
      self.val = val
      self.left, self.right = None, None

def tree_right_view( root ):
   # time = O(N)
   # space = O(N)
   result = []

   if root is None:
      return result

   queue = deque()
   queue.append( root )
   queue.append( None )
   prev = None

   while queue:
      top = queue.popleft()
      if top:
         if top.left:
            queue.append( top.left )
         if top.right:
            queue.append( top.right )
         prev = top
      elif queue:
         result.append( prev )
         prev = None
         queue.append( None )
      else:
         result.append( prev )

   return result

def tree_right_view2( root ):
   result = []

   if root is None:
      return result

   queue = deque()
   queue.append ( root )
   while queue:
      levelSize = len( queue )

      for i in range( levelSize ):
         cur = queue.popleft()

         if i == levelSize - 1:
            result.append( cur )
         if cur.left:
            queue.append( cur.left )
         if cur.right:
            queue.append( cur.right )

   return result

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(9)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   root.left.left.left = TreeNode(3)
   #result = tree_right_view(root)
   result = tree_right_view2(root)

   print("Tree right view: ")
   for node in result:
      print(str(node.val) + " ", end='')

main()
