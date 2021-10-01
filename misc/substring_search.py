#!/usr/bin/env python3

def isSubstringBruteForce( string, pattern ):
   # time = O( n * m ) where n = len( string ), m = len( pattern )

   size = len( string ) - len( pattern ) + 1
   # This is to handle the case of empty pattern.
   if len( pattern ) == 0:
      size = len( string )

   indexList = []
   for i in range( 0, size ):
      index = i
      # For empty pattern, we will match every character. This loop will not run. As
      # a result, index will be just added to indexList.
      for j in range( 0, len( pattern ) ):
         if string[ i + j ] != pattern[ j ]:
            index = None
            break
      if index != None:
         indexList.append( index )

   return indexList

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
            'string' : '',
            'pattern' : 'abc',
            'answer' : [],
         },
         {
            'string' : '',
            'pattern' : '',
            'answer' : [],
         },
         {
            'string' : 'abcdabcabcdf',
            'pattern' : '',
            'answer' : [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ],
         },
         {
            'string' : 'abcdabcabcdf',
            'pattern' : 'abcdf',
            'answer' : [ 7 ],
         },
         {
            'string' : 'abcdabcabcdf',
            'pattern' : 'xyz',
            'answer' : [],
         },
         {
            'string' : 'AAAAAAAAAAAAAAAAAB',
            'pattern' : 'AAAAB',
            'answer' : [ 13 ],
         },
         {
            'string' : 'ABABABCABABABCABABABC',
            'pattern' : 'ABABAC',
            'answer' : [],
         },
   ]

   for test in testCases:
      string = test[ 'string' ]
      pattern = test[ 'pattern' ]
      answer = test[ 'answer' ]
      assert( answer == isSubstringBruteForce( string, pattern ) )
      assert( answer == isSubstringKMP( string, pattern ) )

if __name__ == '__main__':
   testBuildKMPPrefixTable()
   testSubStringSearch()
