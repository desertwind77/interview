#!/usr/bin/env python3
#
# Count the number of ways that the target can be constructed by concatenating
# elements of the wordBank array.

def countConstructTopDown( target, wordBank, mem={} ):
   if target in mem:
      return mem[ target ]

   if target == '':
      return 1

   mem[ target ] = 0
   for i in wordBank:
      if i not in target:
         continue

      if target.startswith( i ):
         newTarget = target[ len( i ) : ]
         if countConstructTopDown( newTarget, wordBank, mem=mem ):
            mem[ target ] += 1

   return mem[ target ]

def countConstructBottomUp( target, wordBank ):
   size = len( target ) + 1
   result = [ 0 ] * size

   # The imaginary leading empty string before target
   result[ 0 ] = 1

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
            if result[ i + wlen ] == 0:
               result[ i + wlen ] = result[ i ]
            else:
               result[ i + wlen ] += 1

   return result[ size - 1 ]

if __name__ == '__main__':
   testCases = [
         {
            'target' : 'abcdef',
            'wordBank' : [ 'ab', 'abc', 'cd', 'def', 'abcd' ],
            'answer' : 1,
         },
         {
            'target' : 'abc',
            'wordBank' : [ 'a', 'bc', 'abc' ],
            'answer' : 2,
         },
         {
            'target' : 'dogfood',
            'wordBank' : [ 'dog', 'g', 'food', 'do' ],
            'answer' : 2,
         },
         {
            'target' : 'skateboard',
            'wordBank' : [ 'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar' ],
            'answer' : 0,
         },
   ]

   for test in testCases:
      target = test[ 'target' ]
      wordBank = test[ 'wordBank' ]
      answer = test[ 'answer' ]
      assert( answer == countConstructTopDown( target, wordBank, mem={} ) )
      assert( answer == countConstructBottomUp( target, wordBank ) )
