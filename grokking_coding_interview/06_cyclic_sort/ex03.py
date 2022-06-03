#!/usr/bin/env python
#
# Find all Missing Numbers (easy)
#
# We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
# The array can have duplicates, which means some numbers will be missing. Find all
# those missing numbers.

def sort( arr ):
   size = len( arr )

   for i in range( size ):
      while arr[ i ] != i + 1 and arr[ arr[ i ] - 1 ] != arr[ i ]:
         tmp = arr[ i ]
         arr[ i ], arr[ tmp - 1 ] = arr[ tmp - 1 ], arr[ i ]

   result = []
   for i in range( size ):
      if arr[ i ] != i + 1:
         result.append( i + 1 )

   return result

testCases = [
   # index : 0 1 2 3 4 5 6 7
   # array : 2 3 1 8 2 3 5 1
   # 0       3 2 1 8 2 3 5 1
   #         1 2 3 8 2 3 5 1
   # 1       1 2 3 8 2 3 5 1
   # 2       1 2 3 8 2 3 5 1
   # 3       1 2 3 8 2 3 5 1
   # 4       1 2 3 8 2 3 5 1
   # 5       1 2 3 8 2 3 5 1
   # 6       1 2 3 8 2 5 3 1
      {
         'input' : [2, 3, 1, 8, 2, 3, 5, 1],
         'output' : [ 4, 6, 7 ],
      },
      {
         'input' : [2, 4, 1, 2],
         'output' : [3],
      },
      {
         'input' : [2, 3, 2, 1],
         'output' : [4],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   result = sort( i )
   print( i )
   print( result )
   print()
