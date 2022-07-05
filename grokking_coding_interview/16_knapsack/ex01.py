#!/usr/bin/env python
#
# 0/1 Knapsack (medium)
#
# Introduction:
# Given the weights and profits of ‘N’ items, we are asked to put these items in a
# knapsack with a capacity ‘C.’ The goal is to get the maximum profit out of the
# knapsack items. Each item can only be selected once, as we don’t have multiple
# quantities of any item.
#
# Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get
# maximum profit. Here are the weights and profits of the fruits:
#
# Items: { Apple, Orange, Banana, Melon }
# Weights: { 2, 3, 1, 4 }
# Profits: { 4, 5, 3, 7 }
# Knapsack capacity: 5
#
# Let’s try to put various combinations of fruits in the knapsack, such that their
# total weight is not more than 5:
#
# Apple + Orange (total weight 5) => 9 profit
# Apple + Banana (total weight 3) => 7 profit
# Orange + Banana (total weight 4) => 8 profit
# Banana + Melon (total weight 5) => 10 profit
#
# This shows that Banana + Melon is the best combination as it gives us the maximum
# profit, and the total weight does not exceed the capacity.
#
# Problem Statement:
# Given two integer arrays to represent weights and profits of ‘N’ items, we need to
# find a subset of these items which will give us maximum profit such that their
# cumulative weight is not more than a given number ‘C.’ Each item can only be
# selected once, which means either we put an item in the knapsack or we skip it.

def knapsack_recursive( weight, profit, capacity, index ):
   if capacity <= 0 or index >= len( weight ):
      return 0

   profit1 = 0
   if capacity >= weight[ index ]:
      profit1 = profit[ index ] + \
            knapsack_recursive( weight, profit,
                                capacity - weight[ index ], index + 1 )
   profit2 = knapsack_recursive( weight, profit, capacity, index + 1 )

   return max( profit1, profit2 )

def knapsack1( weight, profit, capacity ):
   # Brute Force : recursive
   return knapsack_recursive( weight, profit, capacity, 0 )

def knapsack_recursive2( weight, profit, capacity, index, lookupTable ):
   if capacity <= 0 or index >= len( weight ):
      return 0

   if lookupTable[ index ][ capacity ] != -1:
      return lookupTable[ index ][ capacity ]

   profit1 = 0
   if capacity >= weight[ index ]:
      profit1 = profit[ index ] + \
            knapsack_recursive2( weight, profit,
                  capacity - weight[ index ], index + 1, lookupTable )
   profit2 = knapsack_recursive2( weight, profit, capacity, index + 1, lookupTable )

   lookupTable[ index ][ capacity ] = max( profit1, profit2 )

   return lookupTable[ index ][ capacity ]

def knapsack2( weight, profit, capacity ):
   # Brute Force : recursive with memorization
   lookupTable = \
         [ [ -1 for _ in range( capacity + 1 ) ] for _ in range( len( weight ) ) ]
   return knapsack_recursive2( weight, profit, capacity, 0, lookupTable )

def knapsack4( weights, profits, capacity ):
   # Bottom-up dynamic programming
   # time = O( N * C ) where N = len( weight ), C = capacity
   # space = O( N * C )
   n = len( weights )
   if capacity <= 0 or n == 0 or n != len( profits ):
      return 0

   dp = [ [ 0 for _ in range( capacity + 1 ) ] for _ in range( n ) ]

   # populate column 0 of all rows
   for i in range( n ):
      dp[ i ][ 0 ] = 0

   # populate column 1 to capacity of row 0
   for c in range( 1, capacity + 1 ):
      if c >= weights[ 0 ]:
         dp[ 0 ][ c ] =  profits[ 0 ]

   for i in range( 1, n ):
      for c in range( 1, capacity + 1 ):
         # Exclude the item i in the selection
         profit1 = dp[ i - 1 ][ c ]
         # Include the item i in the selection if the capacity allows
         profit2 = 0
         if weights[ i ] <= c:
            profit2 = profits[ i ] + dp[ i - 1 ][ c - weights[ i ] ]

         dp[ i ][ c ] = max( profit1, profit2 )

   return dp[ n - 1 ][ capacity ]

testCases = [
      # index \ capacity   0  1  2  3  4  5
      # 0                  0  0  4  4  4  4
      # 1                  0  0  4  5  5  9
      # 2                  0  3  4  7  8  9
      # 3                  0  3  4  7  8  10
      {
         'weight'   : [ 2, 3, 1, 4 ],
         'profit'   : [ 4, 5, 3, 7 ],
         'capacity' : 5,
         'output'   : 10,
      },
      {
         'weight'   : [ 1, 6, 10, 16 ],
         'profit'   : [ 1, 2, 3, 5 ],
         'capacity' : 7,
         'output'   : 3,
      },
      {
         'weight'   : [ 1, 6, 10, 16 ],
         'profit'   : [ 1, 2, 3, 5 ],
         'capacity' : 6,
         'output'   : 2,
      },
]

for test in testCases:
   w = test[ 'weight' ]
   p = test[ 'profit' ]
   k = test[ 'capacity' ]
   o = test[ 'output' ]
   assert( knapsack1( w, p, k ) == o )
   assert( knapsack2( w, p, k ) == o )
   assert( knapsack4( w, p, k ) == o )
