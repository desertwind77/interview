#!/usr/bin/env python
# Connect Level Order Siblings (medium)
#
# Given a binary tree, connect each node with its level order successor. The last
# node of each level should point to a null node.

from __future__ import print_function
from collections import deque

class TreeNode:
   def __init__(self, val):
      self.val = val
      self.left, self.right, self.next = None, None, None

   # level order traversal using 'next' pointer
   def print_level_order( self ):
      nextLevelRoot = self

      while nextLevelRoot:
         cur = nextLevelRoot
         nextLevelRoot = None

         while cur:
            print( str( cur.val ) + ' ', end='' )
            if not nextLevelRoot:
               if cur.left:
                  nextLevelRoot = cur.left
               elif cur.right:
                  nextLvelRoot = cur.right
            cur = cur.next
         print()

def connect_level_order_siblings( root ):
   # time = O(N)
   # space = O(N)
   queue = deque()
   queue.append( root )
   queue.append( None )
   prev = None

   while queue:
      top = queue.popleft()
      if top:
         if prev:
            prev.next = top
         if top.left:
            queue.append( top.left )
         if top.right:
            queue.append( top.right )
         prev = top
      elif queue:
         prev = None
         queue.append( None )

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(9)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   connect_level_order_siblings(root)

   print("Level order traversal using 'next' pointer: ")
   root.print_level_order()

main()
