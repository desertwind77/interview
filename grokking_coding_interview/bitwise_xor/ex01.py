#!/usr/bin/env python
# In a non-empty array of integers, every number
# appears twice except for one, find that single number.

def missing( seq ):
   sum = 0
   for s in seq:
      sum ^= s
   return sum

testCases = [
      { 'input' : [ 1, 4, 2, 1, 3, 2, 3 ],
        'output' : 4 },
      { 'input' : [ 7, 9, 7 ],
        'output' : 9 },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( missing( i ) == o )
