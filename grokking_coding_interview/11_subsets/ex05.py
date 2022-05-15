#!/usr/bin/env python
# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs
# of balanced parentheses.

def parentheses1( n ):
   result = [ ( '', 0, 0 ) ]

   num = 2 * n
   count = 0
   while count < num:
      curResult = []
      for curParen, numOpen, numClose in result:
         if numOpen < n:
            curResult.append( ( curParen + '(', numOpen + 1, numClose ) )
         if numClose < numOpen:
            curResult.append( ( curParen + ')', numOpen, numClose + 1 ) )
      result = curResult
      count += 1

   return [ i for i, _, _ in result ]

from collections import deque

class ParenthesesString:
   def __init__( self, string, openCount, closeCount ):
      self.string = string
      self.openCount = openCount
      self.closeCount = closeCount

def parentheses2( num ):
   result = []
   queue = deque()
   queue.append( ParenthesesString( "", 0, 0 ) )

   while queue:
      ps = queue.popleft()
      if ps.openCount == num and ps.closeCount == num:
         result.append( ps.string )
      else:
         if ps.openCount < num:
            queue.append( ParenthesesString( ps.string + '(', ps.openCount + 1,
                                             ps.closeCount ) )
         if ps.openCount > ps.closeCount:
            queue.append( ParenthesesString( ps.string + ')', ps.openCount,
                                             ps.closeCount + 1 ) )

   return result

testCases = [
      {
         'input' : 2,
         'output' : [ '(())', '()()' ],
      },
      {
         'input' : 3,
         'output' : [ '((()))', '(()())', '(())()', '()(())', '()()()' ],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( parentheses1( i ) == o )
   assert( parentheses2( i ) == o )
