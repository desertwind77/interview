#!/usr/bin/env python3
# Given a list of N coins, their values (V1, V2, ..., Vn) and the total sum S. Find
# the minimum number of coins, the sum of wichi is S (we can use as many coins of one
# type as we want) or report that its' not possible to select coins in such a way
# that they sum up to S.)

def minCoin( coins, total ):
   size = total + 1
   result = [ float( 'inf' ) ] * size

   result[ 0 ] = 0
   for i in range( 0, size ):
      for j in coins:
         if j == i:
            result[ i ] = 1
         elif j < i and result[ i ] > 1 + result[ i - j ]:
            result[ i ] = 1 + result[ i - j ]

   return result[ total ]

if __name__ == '__main__':
   testcases = [
         {
            'coins' : [ 1, 3, 5, 7 ],
            'total' : 10,
         },
   ]

   for test in testcases:
      coins = test[ 'coins' ]
      total = test[ 'total' ]
      assert( minCoin( coins, total ) )
