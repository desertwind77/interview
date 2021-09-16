#!/usr/bin/env python3

def howSum( targetSum, nums, mems={} ):
    '''print the combination of numbers in nums that can generate targetSum

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
        for i in nums:
            ( result, path ) = howSum( targetSum - i, nums, mems )
            if result:
                tmp = [ i ] + path
                mems[ targetSum ] = ( True, tmp )
                return ( True, tmp )
        mems[ targetSum ] = ( False, [] )
        return ( False, [] )

mems = {}
print( howSum( 7, [ 2, 3 ], mems ) )
mems = {}
print( howSum( 7, [ 5, 3, 4, 7 ], mems ) )
mems = {}
print( howSum( 8, [ 2, 3, 5 ], mems ) )
