#!/usr/bin/env python
# Path With Given Sequence (medium)
#
# Given a binary tree and a number sequence, find if the sequence is present as a
# root-to-leaf path in the given tree.

class TreeNode:
   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def findPath( root, seq ):
   if ( not root and seq ) or ( root and not seq ):
      return False

   if not root.left and not root.right and root.val == seq[ 0 ] and len( seq ) == 1:
      return True

   if root.val != seq[ 0 ]:
      return False

   return findPath( root.left, seq[ 1: ] ) or findPath( root.right, seq[ 1: ] )

def find_path( root, sequence ):
   if not root:
      return len( sequence ) == 0

   return find_path_recursive( root, sequence, 0 )

def find_path_recursive( curNode, sequence, index ):
   # root-to-leaf is shorter than sequence
   if not curNode:
      return False

   seqLen = len( sequence )
   # root-to-leaf is longer than sequence
   if index >= seqLen or curNode.val != sequence[ index ]:
      return False

   if curNode.left is None and curNode.right is None and \
         index == seqLen - 1:
      return True

   return find_path_recursive( curNode.left, sequence, index + 1 ) or \
         find_path_recursive( curNode.right, sequence, index + 1 )

def main():
   root = TreeNode(1)
   root.left = TreeNode(0)
   root.right = TreeNode(1)
   root.left.left = TreeNode(1)
   root.right.left = TreeNode(6)
   root.right.right = TreeNode(5)
   print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
   print("Tree has path sequence: " + str(findPath(root, [1, 0, 7])))
   print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
   print("Tree has path sequence: " + str(findPath(root, [1, 1, 6])))

main()
