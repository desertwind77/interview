#!/usr/bin/env python3

def allSum( targetSum, nums, mems={} ):
   '''Find all the combinations to generate targetSum by using numbers in nums.

   Note:
   - All elements are positive.
   - We can resule elements in the array as many times as needed.
   '''
   if targetSum in mems:
      return mems[ targetSum ]
   elif targetSum == 0:
      return []
   elif targetSum < 0:
      return None
   else:
      mems[ targetSum ] = None

      for i in nums:
         result = allSum( targetSum - i, nums, mems=mems )
         if result == None:
            continue
         elif result == []:
            if mems[ targetSum ] == None:
               mems[ targetSum ] = []
            mems[ targetSum ].append( [ i ] )
         else:
            for ans in result:
               newComb = sorted( [ i ] + ans )
               if mems[ targetSum ] == None:
                  mems[ targetSum ] = []
               if newComb not in mems[ targetSum ]:
                  mems[ targetSum ].append( newComb )

      return mems[ targetSum ]

if __name__ == '__main__':
   testCases = [
         {
            'targetSum' : 7,
            'nums'      : [ 2, 3 ],
            'answer'    : [ [ 2, 2, 3] ],
         },
         {
            'targetSum' : 7,
            'nums'      : [ 5, 3, 4, 7 ],
            'answer'    : [ [ 3, 4 ], [ 7 ] ],
         },
         {
            'targetSum' : 7,
            'nums'      : [ 2, 4 ],
            'answer'    : None,
         },
         {
            'targetSum' : 8,
            'nums'      : [ 2, 3, 5 ],
            'answer'    : [ [ 2, 2, 2, 2 ], [ 2, 3, 3 ], [ 3, 5 ] ],
         },
         {
            'targetSum' : 300,
            'nums'      : [ 7, 14 ],
            'answer'    : None,
         },
   ]

   for test in testCases:
      targetSum = test[ 'targetSum' ]
      nums = test[ 'nums' ]
      answer = test[ 'answer' ]
      assert( answer == allSum( targetSum, nums, mems={} ) )
