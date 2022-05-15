#!/usr/bin/env python
# Given a set with distinct elements, find all of its distinct subsets.

def genSubsets( arr ):
   result = [ [] ]

   for a in arr:
      cur = []
      for r in result:
         tmp = r[:]
         tmp.append( a )
         cur.append( tmp )
      result += cur

   return result

testCases = [
      {
         'input'  : [ 1, 3 ],
         'output' : [ [], [ 1 ], [ 3 ], [ 1, 3 ] ],
      },
      {
         'input'  : [ 1, 5, 3 ],
         'output' : [ [], [ 1 ], [ 5 ], [ 3 ], [ 1, 5 ],
                      [ 1, 3 ], [ 5, 3 ], [ 1, 5, 3 ] ],
      }
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   print( genSubsets( i ) )
