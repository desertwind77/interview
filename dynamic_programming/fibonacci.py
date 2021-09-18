#!/usr/bin/env python3

def fib1( n, series={} ):
   '''
   Top-down dynamic programming to solve the Fibonacci series
   '''
   if n in series:
      return series[ n ]
   else:
      if n == 0:
          series[ n ] = 0
      elif n == 1:
          series[ n ] = 1
      else:
          series[ n ] = fib1( n - 1, series ) + fib1( n - 2, series )

      return series[ n ]

def fib2( n ):
   '''
   Bottom-up dynamic programming to solve the Fibonacci series
   '''
   result = [ 0 ] * ( n + 1 )

   for i in range( 0, n + 1 ):
      if i == 0:
         result[ i ] = 0
      elif i == 1:
         result[ i ] = 1
      else:
         result[ i ] = result[ i - 1 ] + result[ i - 2 ]

   return result[ i ]

def fib3( n ):
   '''
   Bottom-up dynamic programming to solve the Fibonacci series
   with space complexity = O(1)
   '''
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      fn_2 = 0
      fn_1 = 1
      fn = 0

      for i in range( 2, n + 1 ):
         fn = fn_1 + fn_2
         fn_2 = fn_1
         fn_1 = fn

      return fn

if __name__ == '__main__':
   testCases = [
         {
            'input'  : 100,
            'output' : 354224848179261915075,
         },
   ]

   for test in testCases:
      n = test[ 'input' ]
      output = test[ 'output' ]
      assert( output == fib1( n ) )
      assert( output == fib2( n ) )
      assert( output == fib3( n ) )
