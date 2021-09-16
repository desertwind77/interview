#!/usr/bin/env python3

def bestSum( targetSum, nums, mems={} ):
    '''Print the smallest combination of numbers in nums that can generate targetSum

    Note:
    - All elements are positive.
    - We can resule elements in the array as many times as needed.
    '''
    if targetSum in mems:
        return mems[ targetSum ]

    if targetSum == 0:
        return ( True, [] )
    elif targetSum < 0:
        return ( False, [] )
    else:
        smallest = None
        for i in nums:
            ( result, path ) = bestSum( targetSum - i, nums, mems )
            if result and ( not smallest or len( path ) < len( smallest ) ):
                smallest = [ i ] + path
        if smallest:
            mems[ targetSum ] = ( True, smallest )
        else:
            mems[ targetSum ] = ( False, [] )
        return mems[ targetSum ] 

mems = {}
print( bestSum( 7, [ 2, 3 ], mems ) )
mems = {}
print( bestSum( 7, [ 5, 3, 4, 7 ], mems ) )
mems = {}
print( bestSum( 8, [ 2, 3, 5 ], mems ) )
