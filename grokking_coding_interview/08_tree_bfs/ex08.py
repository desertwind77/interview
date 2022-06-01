#!/usr/bin/env python
# Connect All Level Order Siblings (medium)
#
# Given a binary tree, connect each node with its level order successor. The last
# node of each level should point to the first node of the next level.

from __future__ import print_function
from collections import deque


class TreeNode:
   def __init__(self, val):
      self.val = val
      self.left, self.right, self.next = None, None, None

   def print_tree( self ):
      cur = self

      while cur:
         print( str( cur.val ) + ' ', end='' )
         cur = cur.next
      print()

def connect_all_siblings( root ):
   # time = O(N)
   # space = O(N)
   queue = deque()
   queue.append( root )
   prev = None

   while queue:
      top = queue.popleft()
      if top.left:
         queue.append( top.left )
      if top.right:
         queue.append( top.right )
      if prev:
         prev.next = top
      prev = top

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(9)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   connect_all_siblings(root)
   root.print_tree()

main()
