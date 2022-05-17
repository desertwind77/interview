#!/usr/bin/env python
# Given a number ‘n’, write a function to return the count of structurally unique
# Binary Search Trees (BST) that can store values 1 to ‘n’.

class Node:
   def __init__( self, v, l=None, r=None ):
      self.value = v
      self.left = l
      self.right = r

   def __str__( self ):
      lStr = str( self.left ) if self.left else ''
      rStr = str( self.right ) if self.right else ''
      return '( %s, %s, %s )' % ( lStr, str( self.value ), rStr )

def doBst( arr ):
   result = []
   if not arr:
      result.append( [ None ] )
   else:
      size = len( arr )
      for i in range( size ):
         ln = [ arr[ j ] for j in range( 0, i ) ]
         rn = [ arr[ j ] for j in range( i+1, size ) ]

         left = doBst( ln )
         right = doBst( rn )
         for l in left:
            for r in right:
               cur = Node( arr[ i ] )
               cur.left = l
               cur.right = r
               result.append( cur )

   return result

def countBst1( num ):
   result = doBst( list( range( num ) ) )
   return len( result )

def doCountBst2( start, end ):
   if start >= end:
      return 1

   count = 0
   for i in range( start, end + 1 ):
      left = doCountBst2( start, i - 1 )
      right = doCountBst2( i + 1, end )
      count += left * right

   return count

def countBst2( num ):
   return doCountBst2( 1, num )

def countBst3( num, cache=None ):
   if cache and num in cache:
      return cache[ num ]

   if num <= 1:
      return 1

   count = 0
   for i in range( 1, num + 1 ):
      left = countBst3( i - 1, cache )
      right = countBst3( num - i, cache )
      count += left * right

   cache[ num ] = count
   return count

testCases = [
      {
         'input' : 2,
         'output' : 2,
      },
      {
         'input' : 3,
         'output' : 5,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( countBst1( i ) == o )
   assert( countBst2( i ) == o )
   assert( countBst3( i, {} ) == o )
