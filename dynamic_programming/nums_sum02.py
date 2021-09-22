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

if __name__ == '__main__':
   testCases = [
         {
            'targetSum' : 7,
            'nums'      : [ 2, 3 ],
            'answer'    : [ 2, 2, 3 ],
         },
         {
            'targetSum' : 7,
            'nums'      : [ 5, 3, 4, 7 ],
            'answer'    : [ 7 ],
         },
         {
            'targetSum' : 7,
            'nums'      : [ 2, 4 ],
            'answer'    : [],
         },
         {
            'targetSum' : 8,
            'nums'      : [ 2, 3, 5 ],
            'answer'    : [ 3, 5 ],
         },
         {
            'targetSum' : 300,
            'nums'      : [ 7, 14 ],
            'answer'    : [],
         },
   ]

   for test in testCases:
      targetSum = test[ 'targetSum' ]
      nums = test[ 'nums' ]
      answer = test[ 'answer' ]

      _, result = bestSum( targetSum, nums, mems={} )
      assert( answer == sorted( result ) )
