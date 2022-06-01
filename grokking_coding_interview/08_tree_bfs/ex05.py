#!/usr/bin/env python
# Minimum Depth of a Binary Tree (easy)
#
# Find the minimum depth of a binary tree. The minimum depth is the number of nodes
# along the shortest path from the root node to the nearest leaf node.

from collections import deque
import math

class TreeNode:
   def __init__(self, val):
      self.val = val
      self.left, self.right = None, None

def find_minimum_depth1( root ):
   # time = O(N)
   # space = O(N)
   if root is None:
      return 0

   queue = deque()
   minDepth = math.inf

   queue.append( ( root, 1 ) )
   while queue:
      topRoot, topDepth = queue.popleft()

      if not topRoot.left and not topRoot.right:
         minDepth = min( minDepth, topDepth )
      elif topRoot.left:
         queue.append( ( topRoot.left, topDepth + 1 ) )
      elif topRoot.right:
         queue.append( ( topRoot.right, topDepth + 1 ) )

   return minDepth

def find_minimum_depth2( root ):
   # time = O(N)
   # space = O(N)
   if root is None:
      return 0

   queue = deque()
   queue.append( root )
   minDepth = 0

   while queue:
      minDepth += 1
      levelSize = len( queue )

      for _ in range( levelSize ):
         cur = queue.popleft()

         if not cur.left and not cur.right:
            return minDepth

         if cur.left:
            queue.append( cur.left )
         if cur.right:
            queue.append( cur.right )

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   print("Tree Minimum Depth: " + str(find_minimum_depth1(root)))
   print("Tree Minimum Depth: " + str(find_minimum_depth2(root)))

   root.left.left = TreeNode(9)
   root.right.left.left = TreeNode(11)
   print("Tree Minimum Depth: " + str(find_minimum_depth1(root)))
   print("Tree Minimum Depth: " + str(find_minimum_depth2(root)))

main()
