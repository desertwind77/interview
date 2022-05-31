#!/usr/bin/env python
# Count Paths for a Sum (medium)
#
# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum
# of all the node values of each path equals ‘S’. Please note that the paths can
# start or end at any node but all paths must follow direction from parent to child
# (top to bottom).

class TreeNode:
   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def countPaths( root, target ):
   return doCountPaths( root, [], target )

def doCountPaths( root, prefix, target ):
   if root is None:
      return 0

   prefix.append( root.val )

   pathCount = total = 0
   for i in range( len( prefix ) - 1, -1, -1 ):
      total += prefix[ i ]
      if total == target:
         pathCount += 1

   pathCount += doCountPaths( root.left, prefix, target )
   pathCount += doCountPaths( root.right, prefix, target )

   del prefix[ -1 ]

   return pathCount

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(4)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Tree has paths: " + str(countPaths(root, 11)))

main()
