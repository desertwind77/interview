#!/usr/bin/env python3
'''
Find the maximum sum over all subarrays of a given array of integer
'''

def maxSubarray_brute_force( arr ):
   # time = O( n^3 )
   size = len( arr )
   maxSum = 0

   for i in range( 0, size ):
      for j in range( i + 1, size ):
         curSum = 0
         for k in range( i, j ):
            curSum += arr[ k ]

         if curSum > maxSum:
            maxSum = curSum

   return maxSum

def maxSubarray_n_square( arr ):
   # time = O( n^2 )
   size = len( arr )
   sumArray = [ 0 ] * size

   for i in range( 0, size ):
      for j in range( 0, i + 1 ):
         sumArray[ i ] += arr[ j ]

   maxSum = 0
   for i in range( 0, size ):
      for j in range( i, size ):
         prev = 0
         if i > 0:
            prev = sumArray[ i - 1 ]

         sum_i_j = sumArray[ j ] - prev
         if sum_i_j > maxSum:
            maxSum = sum_i_j

   return maxSum

def maxSubarray_bottom_up( arr ):
   # time = O(n), space = O(n)
   size = len( arr )
   if size == 0:
      return 0

   totalSum = [ 0 ] *size
   maxSum = [ 0 ] * size

   for i in range( 0, size ):
      if i == 0:
         totalSum[ i ] = arr[ i ]
         maxSum[ i ] = arr[ i ]
      else:
         totalSum[ i ] = totalSum[ i - 1 ] + arr[ i ]

         if arr[ i ] > totalSum[ i ] and arr[ i ] > maxSum[ i - 1 ]:
            maxSum[ i ] = arr[ i ]
         elif totalSum[ i ] >= maxSum[ i - 1 ]:
            maxSum[ i ] = totalSum[ i ]
         else:
            maxSum[ i ] = maxSum[ i - 1 ]

   return maxSum[ size - 1 ]

def maxSubarray_bottom_up2( arr ):
   # time = O(n), space = O(1)
   size = len( arr )
   if size == 0:
      return 0

   for i in range( 0, size ):
      if i == 0:
         totalSum = arr[ 0 ]
         maxSum = arr[ 0 ]
      else:
         totalSum += arr[ i ]

         if arr[ i ] > totalSum and arr[ i ] > maxSum:
            maxSum = arr[ i ]
         elif totalSum >= maxSum:
            maxSum = totalSum

   return maxSum

if __name__ == '__main__':
   testCases = [
         {
            'array'  : [ 904, 40, 523, 12, -335, -385, -124, 481, -31 ],
            'answer' : 1479,
         },
         {
            'array'  : [ 9, 3, 5, 1, -10, -5, -9, 8, -3 ],
            'answer' : 18,
         },
         {
            'array'  : [ 9, 3, 5, 1, -10, -5, -9, 25, -3 ],
            'answer' : 25,
         },
         {
            'array'  : [ 9, 3, 5, 1, -10, -5, 25, -3 ],
            'answer' : 28,
         },
   ]

   for test in testCases:
      array = test[ 'array' ]
      answer = test[ 'answer' ]
      assert( answer == maxSubarray_brute_force( array ) )
      assert( answer == maxSubarray_n_square( array ) )
      assert( answer == maxSubarray_bottom_up( array ) )
      assert( answer == maxSubarray_bottom_up2( array ) )
