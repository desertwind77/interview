#!/usr/bin/env python
# Problem Challenge 2: Comparing Strings containing Backspaces (medium)
#
# Given two strings containing backspaces (identified by the character ‘#’), check if
# the two strings are equal.

def nextIndex( txt, index ):
   backspace = 0

   while index >= 0:
      if txt[ index ] == '#':
         backspace += 1
      elif backspace > 0:
         backspace -= 1
      else:
         break

      index -= 1

   return index

def compare( str1, str2 ):
   index1 = len( str1 ) - 1
   index2 = len( str2 ) - 1

   while index1 >=0 or index2 >= 0:
      i1 = nextIndex( str1, index1 )
      i2 = nextIndex( str2, index2 )

      if i1 < 0 and i2 < 0:
         return True
      elif i1 < 0 or i2 < 0:
         return False
      if str1[ i1 ] != str2[ i2 ]:
         return False

      index1 = i1 - 1
      index2 = i2 - 1

   return True

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
