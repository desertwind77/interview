#!/usr/bin/env python
#
# Path with Maximum Sum
#
# Find the path with the maximum sum in a given binary tree. Write a function that
# returns the maximum sum.
#
# A path can be defined as a sequence of nodes between any two nodes and doesn’t
# necessarily pass through the root. The path must contain at least one node.

import math

class TreeNode:
   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class MaximumPathSum1:
   def findMaxPathSum( self, root ):
      self.max = -math.inf
      self.doFindMaxPathSum( root )
      return self.max

   def doFindMaxPathSum( self, root ):
      if root is None:
         return 0

      leftSum = self.doFindMaxPathSum( root.left )
      rightSum = self.doFindMaxPathSum( root.right )

      # We want a path from any node to any node which is not necessary a leaf.
      # So we can ignore the path with negative sum.
      leftSum = max( leftSum, 0 )
      rightSum = max( rightSum, 0 )

      curVal = root.val + leftSum + rightSum
      self.max = max( self.max, curVal )

      return max( leftSum, rightSum ) + root.val

def main():
   #maximumPathSum = MaximumPathSum()
   maxSum = MaximumPathSum1()

   root = TreeNode(1)
   root.left = TreeNode(2)
   root.right = TreeNode(3)
   #print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
   print("Maximum Path Sum: " + str( maxSum.findMaxPathSum( root ) ) )

   root.left.left = TreeNode(1)
   root.left.right = TreeNode(3)
   root.right.left = TreeNode(5)
   root.right.right = TreeNode(6)
   root.right.left.left = TreeNode(7)
   root.right.left.right = TreeNode(8)
   root.right.right.left = TreeNode(9)
   #print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
   print("Maximum Path Sum: " + str( maxSum.findMaxPathSum( root ) ) )

   root = TreeNode(-1)
   root.left = TreeNode(-3)
   #print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
   print("Maximum Path Sum: " + str( maxSum.findMaxPathSum( root ) ) )

main()
