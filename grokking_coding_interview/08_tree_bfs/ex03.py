#!/usr/bin/env python
# Zigzag Traversal (medium)
#
# Given a binary tree, populate an array to represent its zigzag level order
# traversal. You should populate the values of all nodes of the first level from left
# to right, then right to left for the next level and keep alternating in the same
# manner for the following levels.

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

   queue, curLevel = deque(), deque()

   queue.append( root )
   queue.append( None )
   rightToLeft = True
   while queue:
      top = queue.popleft()
      if top:
         if top.left:
            queue.append( top.left )
         if top.right:
            queue.append( top.right )

         if rightToLeft:
            curLevel.appendleft( top.val )
         else:
            curLevel.append( top.val )
      elif queue:
         result.append( list( curLevel ) )
         curLevel = deque()
         rightToLeft = not rightToLeft
         queue.append( None )
   result.append( list( curLevel ) )

   return result

def traverse2( root ):
   # time = O(N)
   # space = O(N)
   result = []
   if root is None:
      return result

   queue = deque()
   queue.append( root )
   leftToRight = True
   while queue:
      levelSize = len( queue )
      curLevel = deque()
      for _ in range( levelSize ):
         top = queue.popleft()
         if leftToRight:
            curLevel.append( top.val )
         else:
            curLevel.appendleft( top.val )

         if top.left:
            queue.append( top.left )
         if top.right:
            queue.append( top.right )

      result.append( list( curLevel ) )
      leftToRight = not leftToRight

   return result

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(9)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   root.right.left.left = TreeNode(20)
   root.right.left.right = TreeNode(17)
   print("Zigzag traversal: " + str(traverse1(root)))
   print("Zigzag traversal: " + str(traverse2(root)))

main()
