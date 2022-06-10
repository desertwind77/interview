#!/usr/bin/env python
#
# Happy Number (medium)
#
# Any number will be called a happy number if, after repeatedly replacing it with a
# number equal to the sum of the square of all of its digits, leads us to number ‘1’.
# All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in
# a cycle of numbers which does not include ‘1’.

def nextNumber( num ):
   nums = []

   while num != 0:
      reminder = num % 10
      num = int( num / 10 )
      nums.append( reminder )

   return sum( [ i*i for i in nums ] )

def find_happy_number( num ):
   slow = fast = num

   while fast != 1 and nextNumber( fast ) != 1:
      slow = nextNumber( slow )
      fast = nextNumber( nextNumber( fast ) )
      if slow == fast:
         return False

   return True

testCases = [
      {
         'input' : 23,
         'output' : True,
      },
      {
         'input' : 12,
         'output' : False,
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   print( find_happy_number( i ) )

