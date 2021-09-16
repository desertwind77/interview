#!/usr/bin/env python3

def genCandidates( num_list ):
    result = []
    for i in range( 0, len( num_list ) ):
        tmp = num_list[:]
        tmp.pop( i )
        result.append( tmp )
    return result

def uniqueCanSum( targetSum, nums, mem={} ):
    '''see if we can generate targetSum by using numbers in nums

    Note : we can use each number for only one times and numbers
    may be negative or positive.
    '''
    key = tuple( nums )
    if key in mem:
        return mem[ key ]

    if len( nums ) == 1:
        return nums[ 0 ] == targetSum
    else:
        if sum( nums ) == targetSum:
            mem[ key ] = True
            return True 
        else:
            mem[ key ] = False
            for t in genCandidates( nums ):
                if uniqueCanSum( targetSum, t, mem ):
                    return True
            return False

nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
targetSum = 1700

print( uniqueCanSum( targetSum, nums ) )
