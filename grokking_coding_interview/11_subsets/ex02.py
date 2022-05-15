#!/usr/bin/env python
# Given a set of numbers that might contain duplicates,
# find all of its distinct subsets.

def genUniqueSubsets1( arr ):
   result = [ [] ]

   arr = sorted( arr )
   for i in range( len( arr ) ):

      if i > 0 and arr[ i ] == arr[ i - 1 ]:
         addList = prev
      else:
         addList = result

      cur = []
      for r in addList:
         tmp = r[:]
         tmp.append( arr[ i ] )
         cur.append( tmp )
      result += cur
      prev = cur

   return result

def genUniqueSubsets2( arr ):
   result = [ [] ]

   arr = sorted( arr )
   last = 0
   for i in range( len( arr ) ):
      if i > 0 and arr[ i ] == arr[ i - 1 ]:
         addList = result[ last: ]
      else:
         addList = result

      last = len( result )
      cur = []
      for r in addList:
         tmp = r[:]
         tmp.append( arr[ i ] )
         cur.append( tmp )
      result += cur

   return result

def genUniqueSubsets3( nums ):
   list.sort( nums )
   subsets = [ [] ]
   startIndex, endIndex = 0, 0

   for i in range( len( nums ) ):
      startIndex = 0

      if i > 0 and ( nums[ i ] == nums[ i - 1 ] ):
         startIndex = endIndex + 1
      endIndex = len( subsets ) - 1

      for j in range( startIndex, endIndex + 1 ):
         set1 = list( subsets[ j ] )
         set1.append( nums[ i ] )
         subsets.append( set1 )

   return subsets

testCases = [
      {
         'input'  : [ 1, 3, 3 ],
         'output' : [ [], [ 1 ], [ 3 ], [ 1, 3 ], [ 3, 3 ], [ 1, 3, 3 ] ],
      },
      {
         'input'  : [ 1, 5, 3, 3 ],
         'output' : [ [], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3],
                      [3, 3], [1, 3, 3], [5, 3, 3], [1, 5, 3, 3] ],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   o = [ sorted( i ) for i in o ]
   o = sorted( o )
   assert( sorted( genUniqueSubsets1( i ) ) == o )
   assert( sorted( genUniqueSubsets2( i ) ) == o )
   assert( sorted( genUniqueSubsets3( i ) ) == o )
