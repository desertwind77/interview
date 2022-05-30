#!/usr/bin/env python
# Sum of Path Numbers (medium)
#
# Given a binary tree where each node can only have a digit (0-9) value, each
# root-to-leaf path will represent a number. Find the total sum of all the numbers
# represented by all paths.

class TreeNode:
   def __init__( self, val ):
      self.val = val
      self.left = None
      self.right = None

def findSumOfPathNumbers( root ):
   results = []
   doFindSumOfPathNumbers( root, 0, results )

   total = 0
   for r in results:
      total += r
   return total

def doFindSumOfPathNumbers( root, prefix, results ):
   if not root:
      return

   curVal = prefix * 10 + root.val

   if not root.left and not root.right:
      results.append( curVal )
   else:
      doFindSumOfPathNumbers( root.left, curVal, results )
      doFindSumOfPathNumbers( root.right, curVal, results )

def find_sum_of_path_numbers( root ):
   pass

def find_sum_of_path_numbers_recursive( root, prefix ):
   if not root:
      return 0

   curVal = prefix * 10 + root.val
   if not root.left and not root.right:
      return curVal

   return find_sum_of_path_numbers_recursive( root.left, curVal ) + \
         find_sum_of_path_numbers_recursive( root.right, curVal )

def main():
   root = TreeNode(1)
   root.left = TreeNode(0)
   root.right = TreeNode(1)
   root.left.left = TreeNode(1)
   root.right.left = TreeNode(6)
   root.right.right = TreeNode(5)
   print( "Total Sum of Path Numbers: " )
   print( findSumOfPathNumbers( root ) )
   #print( find_sum_of_path_numbers( root ) )

main()
