#!/usr/bin/env python3

def isSubstringBruteForce1( string, pattern ):
   # time = O( n * m ) where n = len( string ), m = len( pattern )

   size = len( string ) - len( pattern ) + 1
   # This is to handle the case of empty pattern.
   if len( pattern ) == 0:
      size = len( string )

   indexList = []
   for i in range( 0, size ):
      index = i
      # For empty pattern, we will match every character. This loop will
      # not run. As a result, index will be just added to indexList.
      for j in range( 0, len( pattern ) ):
         if string[ i + j ] != pattern[ j ]:
            index = None
            break
      if index != None:
         indexList.append( index )

   return indexList

def isSubstringBruteForce2( string, pattern ):
   # time = O( n * m ) where n = len( string ), m = len( pattern )
   indexList = []
   for i in range( 0, len( string ) ):
      j = 0
      while j < len( pattern ) and i + j < len( string ):
         if string[ i + j ] != pattern[ j ]:
            break
         j += 1
      if j == len( pattern ):
         indexList.append( i )
   return indexList

def isSubstringRabinKarp( string, pattern ):
   pass

def buildKMPPrefixTable( pattern ):
   prefixTable = [ 0 ] * len( pattern )
   # This is to handle the case of empty pattern.
   if len( pattern ) > 0:
      prefixTable[ 0 ] = 0

   j = 0
   i = 1
   while i < len( pattern ):
      if pattern[ j ] == pattern[ i ]:
         prefixTable[ i ] = j + 1
         i += 1
         j += 1
      else:
         if j == 0:
            prefixTable[ i ] = 0
            i += 1
         else:
            j = prefixTable[ j - 1 ]

   return prefixTable

def isSubstringKMP( string, pattern ):
   # time = O( n + m ) where n = len( string ), m = len( pattern )
   t = buildKMPPrefixTable( pattern )

   indexList = []
   j = 0    # Starting index in string
   i = 0    # Current position in pattern
   while j + i < len( string ):
      # We have to be careful and handle the case of empty pattern.
      if len( pattern ) == 0 or string[ j + i ] == pattern[ i ]:
         if len( pattern ) == 0:
            # Handle empty pattern
            indexList.append( j )
            j += 1
         else:
            i += 1

            if i == len( pattern ):
               indexList.append( j )
               j = j + i - t[ i - 1 ]
               i = 0
      else:
         if i == 0:
            j += 1
         else:
            j = j + i - t[ i - 1 ]
            i = 0

   return indexList

# The size of the alphabet (total number of possible characters)
MAX_CHARS = 256

def buildFiniteAutomata( pattern ):
   # time = O( m^3 * MAX_CHARS ) where m = len( pattern ) and MAX_CHARS = size
   # of alphabets (the number of possible characters)
   #
   # Using similar techniques to prefix array in KMP algorithm,
   # O( m * MAX_CHARS ) is possible.
   def getNextState( pattern, curState, nextChar ):
      # nextChar is eqaul to the next character in the pattern
      if curState < len( pattern ) and chr( nextChar ) == pattern[ curState ]:
         return curState + 1

      # Find the longest possible suffix that is also a prefix in
      # pattern[ 0 : state ]c where c is nextChar
      #
      # index    : 0 1 2 3 4 5 6
      # pattern  : A C A C A G A
      #                    ^
      # curState : 5
      # nextChar : C
      #
      # From above, assume state 0 represents emptyt string, curState = 5 which
      # represents 'ACACA' and nextChar is C. The longest suffix that is also a
      # suffix = 'ACA'. So the currentState should be set to 3 which represents
      # 'ACA'. With nextChar = C, the next state should be 4 which represets
      # 'ACAC'.
      i = 0
      for nextState in range( curState, 0, -1 ):
         if chr( nextChar ) == pattern[ nextState - 1 ]:
            while i < nextState - 1:
               if pattern[ i ] != pattern[ state - nextState + 1 + i ]:
                  break
               i += 1
            if i == nextState - 1:
               return nextState

      return 0

   size = len( pattern )
   # Each column represents a character in the alphabets and each row represents
   # each state in the finite automata. We have size + 1 states because we need
   # an additional state for the initial state.
   finiteAutomata = \
           [ [ 0 for _ in range( MAX_CHARS ) ] for _ in range( size + 1 ) ]

   for state in range( size + 1 ):
      for char in range( MAX_CHARS ):
         finiteAutomata[ state ][ char ] = getNextState( pattern, state, char )
   return finiteAutomata

def buildFiniteAutomataFast( pattern ):
   # time = O( m * MAX_CHARS )
   size = len( pattern )
   finiteAutomata = \
           [ [ 0 for _ in range( MAX_CHARS ) ] for _ in range( size + 1 ) ]

   # Init the first row to 0
   for i in range( MAX_CHARS ):
      finiteAutomata[ 0 ][ i ] = 0
   if len( pattern ) > 0:
      finiteAutomata[ 0 ][ ord( pattern[ 0 ] ) ] = 1

   # lps = longest suffix that is also a suffix
   lps = 0
   for i in range( 1, len( pattern ) + 1 ):
      for j in range( MAX_CHARS ):
         # Copy values from row at index = lps
         finiteAutomata[ i ][ j ] = finiteAutomata[ lps ][ j ]
      if i < len( pattern ):
         # Update the entry corresponding to this character
         finiteAutomata[ i ][ ord( pattern[ i  ] ) ] = i + 1
         # Update lps for next row to be filled
         lps = finiteAutomata[ lps ][ ord( pattern[ i ] ) ]

   return finiteAutomata

def isSubstringFiniteAutomata( string, pattern, fast=False ):
   automata = None
   if fast:
      automata = buildFiniteAutomataFast( pattern )
   else:
      automata = buildFiniteAutomata( pattern )

   indexList = []
   state = 0
   for i in range( len( string ) ):
      # I am at the state 'state'. What state will string[ i ] bring me to?
      state = automata[ state ][ ord(string[ i ] ) ]
      if state == len( pattern ):
         # We reach the terminal state
         if pattern:
            indexList.append( i - len( pattern ) + 1 )
         else:
            # TODO: find out the reason for this
            indexList.append( i )


   return indexList

def testBuildKMPPrefixTable():
   testCases = [
         {
            'pattern' : 'acacabacacabacacac',
            'table' : [ 0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 4 ],
         },
   ]

   for test in testCases:
      pattern = test[ 'pattern' ]
      table = test[ 'table' ]
      assert( table == buildKMPPrefixTable( pattern ) )

def testSubStringSearch():
   testCases = [
         {
            'testId' : 1,
            'string' : 'abcdabcabcdf',
            'pattern' : 'abcdf',
            'answer' : [ 7 ],
            'enable' : True,
         },
         {
            'testId' : 2,
            'string' : 'abcdabcabcdf',
            'pattern' : 'xyz',
            'answer' : [],
            'enable' : True,
         },
         {
            'testId' : 3,
            'string' : 'AAAAAAAAAAAAAAAAAB',
            'pattern' : 'AAAAB',
            'answer' : [ 13 ],
            'enable' : True,
         },
         {
            'testId' : 4,
            'string' : 'ABABABCABABABCABABABC',
            'pattern' : 'ABABAC',
            'answer' : [],
            'enable' : True,
         },
         {
            'testId' : 5,
            'string' : '',
            'pattern' : 'abc',
            'answer' : [],
            'enable' : True,
         },
         {
            'testId' : 6,
            'string' : '',
            'pattern' : '',
            'answer' : [],
            'enable' : True,
         },
         {
            'testId' : 7,
            'string' : 'abcdabcabcdf',
            'pattern' : '',
            'answer' : [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ],
            'enable' : True,
         },
   ]

   for test in testCases:
      if not test[ 'enable' ]:
          continue
      testId = test[ 'testId' ]
      string = test[ 'string' ]
      pattern = test[ 'pattern' ]
      answer = test[ 'answer' ]
      assert( answer == isSubstringBruteForce1( string, pattern ) )
      assert( answer == isSubstringBruteForce2( string, pattern ) )
      assert( answer == isSubstringKMP( string, pattern ) )
      assert( answer == isSubstringFiniteAutomata( string, pattern ) )
      assert( answer == isSubstringFiniteAutomata( string, pattern, fast=True ) )
      print( testId, 'passed' )

if __name__ == '__main__':
   testBuildKMPPrefixTable()
   testSubStringSearch()
