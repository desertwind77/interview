#!/usr/bin/env python
# Tree Diameter (medium)
#
# Given a binary tree, find the length of its diameter. The diameter of a tree is the
# number of nodes on the longest path between any two leaf nodes. The diameter of a
# tree may or may not pass through the root.
#
# Note: You can always assume that there are at least two leaf nodes in the given
# tree.

class TreeNode:
   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def findHeight( root ):
   if not root.left and not root.right:
      return [ 1, 1 ]

   leftResult = rightResult = None
   leftHeight = rightHeight = 0
   leftLength = rightLength = 0

   if root.left:
      leftHeight, leftLength = findHeight( root.left )

   if root.right:
      rightHeight, rightLength = findHeight( root.right )

   height = max( leftHeight, rightHeight ) + 1
   curLength = leftHeight + rightHeight + 1
   length = max( max( leftLength, rightLength ), curLength )

   return [ height, length ]

def findDiameter( root ):
   _, length = findHeight( root )
   return length

class TreeDiameter:
   def __init__( self ):
      self.treeDiameter = 0

   def find_diameter( self, root ):
      self.calculate_height( root )
      return self.treeDiameter

   def calculate_height( self, curNode ):
      if curNode is None:
         return 0

      leftHeight = self.calculate_height( curNode.left )
      rightHeight = self.calculate_height( curNode.right )

      if curNode.left and curNode.right:
         # Node needs to have both left and right child so that
         # it can have leaves on both sides
         diameter = leftHeight + rightHeight + 1
         self.treeDiameter = max( self.treeDiameter, diameter )

      return max( leftHeight, rightHeight ) + 1


def main():
   treeDiameter = TreeDiameter()
   root = TreeNode(1)
   root.left = TreeNode(2)
   root.right = TreeNode(3)
   root.left.left = TreeNode(4)
   root.right.left = TreeNode(5)
   root.right.right = TreeNode(6)
   print("Tree Diameter: " + str( findDiameter( root ) ) )
   print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))

   root.left.left = None
   root.right.left.left = TreeNode(7)
   root.right.left.right = TreeNode(8)
   root.right.right.left = TreeNode(9)
   root.right.left.right.left = TreeNode(10)
   root.right.right.left.left = TreeNode(11)
   print("Tree Diameter: " + str( findDiameter( root ) ) )
   print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))

main()
