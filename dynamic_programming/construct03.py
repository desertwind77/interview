#!/usr/bin/env python3
#
# the function should return a 2D array containing all of the ways that the target can
# be constructed by concatenating elements of the wordBank array. Each element of the
# 2D array should represent one combination that construct the target.

def allConstructTopDown( target, wordBank, mem={} ):
   if target in mem:
      return mem[ target ]

   if target == '':
      return []

   mem[ target ] = []
   for i in wordBank:
      if i not in target:
         continue

      if target.startswith( i ):
         newTarget = target[ len( i ) : ]
         if newTarget == '':
            mem[ target ].append( [ i ] )
         else:
            subConstruct = allConstructTopDown( newTarget, wordBank, mem=mem )
            if not subConstruct:
               continue
            for s in subConstruct:
               mem[ target ].append( [ i ] + s )

   return mem[ target ]

def allConstructBottomUp( target, wordBank ):
   size = len( target ) + 1
   # Beware! the following will not work.
   #     result = [ [] ] * size
   # This is because
   #     a = [ [] ] * 3
   #     a[ 0 ].append( 3 )
   #     print( a )
   # We will get the following:
   #     [[3], [3], [3]]
   result = []
   for i in range( 0, size ):
      result.append( [] )

   for i in range( 0, size ):
      # target[ 0, i - 1 ] are not ok. No need to look ahead
      # target[ 0 ] means the imaginary leading empty string before target
      if i > 0 and not result[ i ]:
         continue
      for w in wordBank:
         wlen = len( w )
         if i + wlen > len( target ):
            continue
         if target[ i : i + wlen ] == w:
            if result[ i ]:
               for res in result[ i ]:
                  newRes = res[:]
                  newRes.append( w )
                  result[ i + wlen ].append( newRes )
            else:
               result[ i + wlen ].append( [ w ] )

   return result[ size - 1 ]


if __name__ == '__main__':
   testCases = [
         {
            'target' : 'abcdef',
            'wordBank' : [ 'ab', 'abc', 'cd', 'def', 'abcd' ],
            'answer' : [ [ 'abc', 'def' ] ],
         },
         {
            'target' : 'abc',
            'wordBank' : [ 'a', 'bc', 'abc' ],
            'answer' : [ [ 'a', 'bc' ], [ 'abc' ] ]
         },
         {
            'target' : 'skateboard',
            'wordBank' : [ 'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar' ],
            'answer' : [],
         },
   ]

   for test in testCases:
      target = test[ 'target' ]
      wordBank = test[ 'wordBank' ]
      answer = sorted( test[ 'answer' ] )
      assert( answer == sorted( allConstructTopDown( target, wordBank, mem={} ) ) )
      assert( answer == sorted( allConstructBottomUp( target, wordBank ) ) )
