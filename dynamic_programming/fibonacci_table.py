#!/usr/bin/env python3

def fib( n ):
    result = [ 0 ] * ( n + 1 )

    for i in range( 0, n + 1 ):
        if i == 0:
            result[ i ] = 0
        elif i == 1:
            result[ i ] = 1
        else:
            result[ i ] = result[ i - 1 ] + result[ i - 2 ]

    return result[ i ]

print( 'fib( %d ) = %d' % ( 100, fib( 100 ) ) )
