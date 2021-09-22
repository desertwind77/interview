#!/usr/bin/env python3

def lengthOfLongestSubstring( s: str) -> int:
   '''
   Given a string s, find the length of the longest substring without repeating
   characters.
   '''
   maxCount = 0

   for i in range( 0, len( s ) ):
      if i == 0:
         start = 0
         stop = 0
         maxCount = 1
      else:
         pos = s[ 0 : i ].rfind( s[ i ] )
         if pos != -1 and pos >= start:
            start = pos + 1
         stop = i

         count = stop - start + 1
         if count > maxCount:
            maxCount = count

   return maxCount

if __name__ == '__main__':
   testCases = [
         {
            'string' : 'abcabcbb',
            'answer' : 3,
         },
         {
            'string' : 'bbbbb',
            'answer' : 1,
         },
         {
            'string' : 'pwwkew',
            'answer' : 3,
         },
         {
            'string' : '',
            'answer' : 0,
         },
         {
            'string' : 'abba',
            'answer' : 2,
         },
   ]

   for test in testCases:
      string = test[ 'string' ]
      answer = test[ 'answer' ]
      print( lengthOfLongestSubstring( string ) )
      assert( answer == lengthOfLongestSubstring( string ) )
