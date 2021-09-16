#!/usr/bin/env python3

def fib( n, series={} ):
    '''Calculate the fibonacci series using dynamic programming'''
    if n in series:
        return series[ n ]
    else:
        if n == 0:
            series[ n ] = 0
        elif n == 1:
            series[ n ] = 1
        else:
            series[ n ] = fib( n - 1, series ) + fib( n - 2, series )

        return series[ n ]

print( 'fib( %d ) = %d' % ( 100, fib( 100 ) ) )
