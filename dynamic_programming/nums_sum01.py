#!/usr/bin/env python3

def canSum( targetSum, nums, mems={} ):
    '''see if we can generate targetSum by using numbers in nums.

    Note:
    - All elements are positive.
    - We can resule elements in the array as many times as needed.
    '''
    if targetSum in mems:
        return mems[ targetSum ]
    if targetSum == 0:
        return True
    elif targetSum < 0:
        return False
    else:
        for i in nums:
            if canSum( targetSum - i, nums, mems ):
                mems[ targetSum ] = True
                return True
        mems[ targetSum ] = False
        return False

# True
mems = {}
print( canSum( 7, [ 2, 3 ], mems ) )
# True
mems = {}
print( canSum( 7, [ 5, 3, 4, 7 ], mems ) )
# False
mems = {}
print( canSum( 7, [ 2, 4 ], mems ) )
# True
mems = {}
print( canSum( 8, [ 2, 3, 5 ], mems ) )
# False
mems = {}
print( canSum( 300, [ 7, 14 ], mems ) )
