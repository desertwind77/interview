#!/usr/bin/env python3
'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], return an
array of all the integers in the range [1, n] that do not appear in nums.

Constraints:
   n == nums.length
   1 <= n <= 105
   1 <= nums[i] <= n
'''

def missingNumber( array ):
   for i in range( 0, len( array ) ):
      while array[ i ] != i + 1 and array[ array[ i ] - 1 ] != array[ i ]:
         tmp = array[ array[ i ] - 1 ]
         array[ array[ i ] - 1 ] = array[ i ]
         array[ i ] = tmp

   answer = [ i for i in range( 0, len( array ) ) if array[ i ] != i + 1 ]
   return answer

if __name__ == '__main__':
   testCases = [
         {
            'input' : [ 4, 3, 2, 7, 8, 2, 3, 1 ],
            'answer' : [ 5, 6 ],
         },
         {
            'input' : [ 1, 1 ],
            'answer' : [ 2 ],
         },
   ]

   for test in testCases:
      array = test[ 'input' ]
      answer = test[ 'answer' ]
      assert( answer == missingNumber( array ) )
