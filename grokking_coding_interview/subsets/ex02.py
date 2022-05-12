#!/usr/bin/env python
# Given a set of numbers that might contain duplicates,
# find all of its distinct subsets.

def genUniqueSubsets( arr ):
   result = [ [] ]

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
   assert( genUniqueSubsets( i ) == o )
