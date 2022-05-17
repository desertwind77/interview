#!/usr/bin/env python
# Given a number ‘n’, write a function to return all structurally unique Binary
# Search Trees (BST) that can store values 1 to ‘n’?

class Tree:
   def __init__( self, v, l=None,  r=None ):
      self.value = v
      self.left = l
      self.right = r

   def __str__( self ):
      leftStr = str( self.left ) if self.left else 'None'
      rightStr = str( self.right ) if self.right else 'None'
      return '( ' + leftStr + ', ' + str( self.value ) + ', ' + rightStr + ' )'

def doBst( nodes ):
   result = []

   if not nodes:
      return [ None ]
   else:
      for i in range( len( nodes ) ):
         leftNodes = []
         for j in range( 0, i ):
            leftNodes.append( nodes[ j ] )
         left = doBst( leftNodes )

         rightNodes = []
         for k in range( i + 1, len( nodes ) ):
            rightNodes.append( nodes[ k ] )
         right = doBst( rightNodes )

         for l in left:
            for r in right:
               cur = Tree( nodes[ i ] )
               cur.left = l
               cur.right = r
               result.append( cur )

   return result

def bst( num ):
   return doBst( list( range( 0, num ) ) )

class TreeNode:
   def __init__( self, val ):
      self.val = val
      self.left = None
      self.right = None

def findUniqueTrees( n ):
   if n <= 0:
      return []
   return findUniqueTreesRecursive( 1, n )

def findUniqueTreesRecursive( start, end ):
   result = []
   if start > end:
      result.append( None )
      return result

   for i in range( start, end + 1 ):
      leftSubtrees = findUniqueTreesRecursive( start, i - 1 )
      rightSubtrees = findUniqueTreesRecursive( i + 1, end )
      for leftTree in leftSubtrees:
         for rightTree in rightSubtrees:
            root = TreeNode( i )
            root.left = leftTree
            root.right =rightTree
            result.append( root )

   return result

print( bst( 2 ) )
print( bst( 3 ) )
