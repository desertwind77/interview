#!/usr/bin/env python3
#
# Return boolean if target can be constructed by concatenating elements of the
# wordBank array.
#
# 1) Non-dynamic programming
# Executed in  865.12 millis    fish           external
#    usr time   23.47 millis   74.00 micros   23.40 millis
#    sys time   11.27 millis  460.00 micros   10.80 milli
#
# 2) Dynamic programming
# Executed in   62.24 millis    fish           external
#    usr time   23.33 millis   76.00 micros   23.25 millis
#    sys time   10.96 millis  471.00 micros   10.49 millis

def canConstructTopDown01( target, wordBank, mem={} ):
   '''
   This solution is ok but it is very hard to extend to cover allConstructTopDown
   '''
   def split( string, delimiter ):
      tmp = string.split( delimiter )
      tmp = [ i for i in tmp if i != '' ]
      return tmp

   if target in mem:
      return mem[ target ]

   if target == '':
      return True

   for i in wordBank:
      if i not in target:
         continue

      x = split( target, i )
      canConstructSubString = True
      for j in x:
         if not canConstructTopDown01( j, wordBank, mem ):
            canConstructSubString = False
            break
      if not canConstructSubString:
         continue
      mem[ target ] = True
      return True

   mem[ target ] = False
   return False

def canConstructTopDown02( target, wordBank, mem={} ):
   if target in mem:
      return mem[ target ]

   if target == '':
      return True

   mem[ target ] = False
   for i in wordBank:
      if i not in target:
         continue

      if target.startswith( i ):
         newTarget = target[ len( i ) : ]
         if canConstructTopDown02( newTarget, wordBank, mem=mem ):
            mem[ target ] = True 
            break

   return mem[ target ] 

def canConstructBottomUp( target, wordBank ):
   size = len( target ) + 1
   result = [ False ] * size

   # The imaginary leading empty string before target
   result[ 0 ] = True

   for i in range( 0, size ):
      # target[ 0, i - 1 ] are not ok. No need to look ahead
      # target[ 0 ] means the imaginary leading empty string before target
      if not result[ i ]:
         continue
      for w in wordBank:
         wlen = len( w )
         if i + wlen > len( target ):
            continue
         if target[ i : i + wlen ] == w:
            result[ i + wlen ] = True

   return result[ size - 1 ]

if __name__ == '__main__':
   testCases = [
         {
            'target'   : 'abcdef',
            'wordBank' : [ 'ab', 'abc', 'cd', 'def', 'abcd' ],
            'answer'   : True,
         },
         {
            'target'   : 'abcdef',
            'wordBank' : [ 'g', 'h', 'ii' ],
            'answer'   : False,
         },
         {
            'target'   : 'skateboard',
            'wordBank' : [ 'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar' ],
            'answer'   : False,
         },
         {
            'target'   : 'enterapotentpot',
            'wordBank' : [ 'a', 'p', 'ent', 'enter', 'ot', 'o', 't' ],
            'answer'   : True,
         },
         {
            'target'   : 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
            'wordBank' : [ 'e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee' ],
            'answer'   : False,
         },
   ]

   for test in testCases:
      target = test[ 'target' ]
      wordBank = test[ 'wordBank' ]
      answer = test[ 'answer' ]
      assert( answer == canConstructTopDown01( target, wordBank, mem={} ) )
      assert( answer == canConstructTopDown02( target, wordBank, mem={} ) )
      assert( answer == canConstructBottomUp( target, wordBank ) )
