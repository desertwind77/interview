#!/usr/bin/env python
# All Paths for a Sum (medium)
#
# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that
# the sum of all the node values of each path equals ‘S’.

class TreeNode:
   def __init__( self, val ):
      self.val = val
      self.left = None
      self.right = None

def findPaths( root, target ):
   return doFindPath( root, [], target )

def doFindPath( root, prefix, target ):
   if not root.left and not root.right:
      if root.val == target:
         prefix.append( root.val )
         return [ prefix ]
      else:
         return None

   leftResult = rightResult = None
   result = []

   if root.left:
      leftResult = \
            doFindPath( root.left, prefix[:] + [ root.val ], target - root.val )
      if leftResult:
         result += leftResult

   if root.right:
      rightResult = \
            doFindPath( root.right, prefix[:] + [ root.val ], target - root.val )
      if rightResult:
         result += rightResult

   return result

def find_paths( root, required_sum ):
   allPaths = []
   find_paths_recursive( root, required_sum, [], allPaths )
   return allPaths

def find_paths_recursive( root, required_sum, currentPath, allPaths ):
   if not root:
      return

   currentPath.append( root.val )

   if root.val == required_sum and not root.left and not root.right:
      allPaths.append( list( currentPath ) )
   else:
      find_paths_recursive( root.left, required_sum - root.val,
                            currentPath, allPaths )
      find_paths_recursive( root.right, required_sum - root.val,
                            currentPath, allPaths )

   # remove the current node from the path to backtrack, we need to
   # remove the current node while we are going up the recursive call stack.
   del currentPath[ -1 ]

def main():
   root = TreeNode(12)
   root.left = TreeNode(7)
   root.right = TreeNode(1)
   root.left.left = TreeNode(4)
   root.right.left = TreeNode(10)
   root.right.right = TreeNode(5)
   required_sum = 23
   print( "Tree paths with required_sum " + str( required_sum ) + ": " )
   print( findPaths( root, required_sum ) )
   print( find_paths( root, required_sum ) )

main()
