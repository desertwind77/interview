#!/usr/bin/env python
# Problem Challenge 2: Comparing Strings containing Backspaces (medium)
#
# Given two strings containing backspaces (identified by the character ‘#’), check if
# the two strings are equal.

def summarize( txt ):
   size = len( txt )
   count = 0
   result = ''

   for i in range( size - 1, -1, -1 ):
      if txt[ i ] == '#':
         count += 1
      else:
         if count > 0:
            count -= 1
         else:
            result = txt[ i ] + result

   return result

def compare( s1, s2 ):
   return summarize( s1 ) == summarize( s2 )

testCases = [
      {
         'str1' : "xy#z",
         'str2' : "xzz#",
         'output' : True,
      },
      {
         'str1' : "xy#z",
         'str2' : "xyz#",
         'output' : False,
      },
      {
         'str1' : "xp#",
         'str2' : "xyz##",
         'output' : True,
      },
      {
         'str1' : "xywrrmp",
         'str2' : "xywrrmu#p",
         'output' : True,
      },

]

for test in testCases:
   s1 = test[ 'str1' ]
   s2 = test[ 'str2' ]
   o = test[ 'output' ]
   assert( o == compare( s1, s2 ) )
