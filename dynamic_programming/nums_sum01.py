#!/usr/bin/env python3

def canSum( targetSum, nums, mems={} ):
   '''See if we can generate targetSum by using numbers in nums.

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
         if canSum( targetSum - i, nums, mems=mems ):
            mems[ targetSum ] = True
            return True
      mems[ targetSum ] = False
      return False

if __name__ == '__main__':
   testCases = [
         {
            'targetSum' : 7,
            'nums'      : [ 2, 3 ],
            'answer'    : True,
         },
         {
            'targetSum' : 7,
            'nums'      : [ 5, 3, 4, 7 ],
            'answer'    : True,
         },
         {
            'targetSum' : 7,
            'nums'      : [ 2, 4 ],
            'answer'    : False,
         },
         {
            'targetSum' : 8,
            'nums'      : [ 2, 3, 5 ],
            'answer'    : True,
         },
         {
            'targetSum' : 300,
            'nums'      : [ 7, 14 ],
            'answer'    : False,
         },
   ]

   for test in testCases:
      targetSum = test[ 'targetSum' ]
      nums = test[ 'nums' ]
      answer = test[ 'answer' ]
      assert( answer == canSum( targetSum, nums, mems={} ) )
