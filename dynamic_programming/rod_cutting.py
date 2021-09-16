#!/usr/bin/env python3

def rod_cutting( length, profit, maxProfit={}, maxCut={} ):
    '''Cut the rod in such a way that achieves the maximum profit

    length      the length of the rod
    profit      the array containing the profit at each length
    '''
    if length in maxProfit:
        return maxProfit[ length ]

    if length in [ 0, 1 ]:
        return profit[ length ]
    else:
        curMax = profit[ length ]
        curCut = ( 0, length )
        for i in range( 1, int( length / 2 ) + 1 ):
            tmp = rod_cutting( i, profit, maxProfit, maxCut ) + \
                    rod_cutting( length - i, profit, maxProfit, maxCut )
            if tmp > curMax:
                curMax = tmp
                curResult = ( i, length - i )
        maxProfit[ length ] = curMax
        maxCut[ length ] = curCut
        return curMax

print( 'max = ', rod_cutting( 5, [ 0, 1, 3, 5, 5, 5 ] ) )
print( 'max = ', rod_cutting( 4, [ 0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 ] ) )
