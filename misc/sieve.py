#!/usr/bin/env python3
import math
'''
Find the prime number using Sieve of Eratosthenes
'''

def sieve1( n ):
   primes = [ True ] * ( n + 1 )
   primes[ 0 ] = primes[ 1 ] = False

   for i in range( 2, n + 1 ):
      multiplier = 2
      while i * multiplier <= n:
         primes[ i * multiplier ] = False
         multiplier += 1

   answer = [ i for i in range( 2, n + 1 ) if primes[ i ] ]
   return answer

def sieve2( n ):
   primes = [ True ] * ( n + 1 )
   primes[ 0 ] = primes[ 1 ] = False
   m = int( math.sqrt( n ) )

   for i in range( 2, m + 1 ):
      if primes[ i ]:
         k = i * i
         while k <= n:
            primes[ k ] = False
            k += i

   answer = [ i for i in range( 2, n + 1 ) if primes[ i ] ]
   return answer

if __name__ == '__main__':
   testCases = [
         {
            'input' : 20,
            'answer' : [ 2, 3, 5, 7, 11, 13, 17, 19 ],
         }
   ]

   for test in testCases:
      n = test[ 'input' ]
      answer = test[ 'answer' ]
      assert( answer == sieve1( n ) )
      assert( answer == sieve2( n ) )
