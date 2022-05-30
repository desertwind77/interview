#!/usr/bin/env python3
# Binary Tree Path Sum (easy)
#
# Given a binary tree and a number ‘S’, find if the tree has
# a path from root-to-leaf such that the sum of all the node
# values of that path equals ‘S’.

class TreeNode:
   def __init__( self, val ):
      self.val = val
      self.left = None
      self.right = None

def hasPath( root, val ):
   if not root.left and not root.right:
      # leaf node
      return root.val == val
   else:
      # non-leaf node
      curVal = val - root.val
      leftResult = rightResult = False
      if root.left:
         leftResult = hasPath( root.left, curVal )
      if root.right:
         rightResult = hasPath( root.right, curVal )

      return leftResult or rightResult

def has_path( root, val ):
   if not root:
      return False

   if root.val == val and not root.left and not root.right:
      return True

   return has_path( root.left, val - root.val ) or \
         has_path( root.right, val - root.val )

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(hasPath(root, 23)))
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(hasPath(root, 16)))
  print("Tree has path: " + str(has_path(root, 16)))

main()
