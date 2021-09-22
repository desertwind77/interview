#!/usr/bin/env python3

def genCandidates( num_list ):
    result = []
    for i in range( 0, len( num_list ) ):
        tmp = num_list[:]
        tmp.pop( i )
        result.append( tmp )
    return result

def uniqueCanSum( targetSum, nums, mem={} ):
    '''
    See if we can generate targetSum by using numbers in nums. Each number may be
    negative or positve and can be used only once.
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

if __name__ == '__main__':
   testCases = [
         {
            'targetSum' : 17,
            'nums'      : [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
            'answer'    : True,
         },
         {
            'targetSum' : 1700,
            'nums'      : [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
            'answer'    : False,
         },
   ]

   for test in testCases:
      targetSum = test[ 'targetSum' ]
      nums = test[ 'nums' ]
      answer = test[ 'answer' ]
      assert( answer == uniqueCanSum( targetSum, nums ) )
