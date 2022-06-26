#!/usr/bin/env python
#
# Fruits into Baskets (medium)
#
# You are visiting a farm to collect fruits. The farm has a single row of fruit
# trees. You will be given two baskets, and your goal is to pick as many fruits as
# possible to be placed in the given baskets.
#
# You will be given an array of characters where each character represents a fruit
# tree. The farm has following restrictions:
#
# - Each basket can have only one type of fruit. There is no limit to how many fruit a
#   basket can hold.
# - You can start with any tree, but you can’t skip a tree once you have started.
# - You will pick exactly one fruit from every tree until you cannot, i.e., you will
#   stop when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both baskets.

from collections import defaultdict

def fruit( arr ):
   size = len( arr )
   start = 0
   count = defaultdict( int )
   maxFruit = 0

   for i in range( size ):
      count[ arr[ i ] ] += 1

      while start <= i and len( count.keys() )> 2:
         count[ arr[ start ] ] -= 1
         if count[ arr[ start ] ] == 0:
            del count[ arr[ start ] ]
         start += 1

      total = 0
      for _, val in count.items():
         total += val
      maxFruit = max( maxFruit, total )

   return maxFruit

testCases = [
      # index   : 0  1  2  3  4
      # input   : A  B  C  A  C
      # start   : 0  0  1  2  3
      # baskets : A1 A1 B1 C1 C2
      #              B1 C1 A1 A1
      {
         'input' : ['A', 'B', 'C', 'A', 'C'],
         'output' : 3,
      },
      {
         'input' : ['A', 'B', 'C', 'B', 'B', 'C'],
         'output' : 5,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( fruit( i ) == o )
