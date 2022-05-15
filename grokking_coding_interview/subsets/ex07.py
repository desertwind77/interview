#!/usr/bin/env python
# Given an expression containing digits and operations (+, -, *), find all possible
# ways in which the expression can be evaluated by grouping the numbers and operators
# using parentheses.

def expression( string ):
   result = []

   if ( '+' not in string ) and \
         ( '-' not in string ) and \
         ( '*' not in string ):
      result.append( int( string ) )
   else:
      for i in range( len( string ) ):
         char = string[ i ]
         if not char.isdigit():
            lval = expression( string[ 0:i ] )
            rval = expression( string[ i+1: ] )
            for l in lval:
               for r in rval:
                  if char == '+':
                     result.append( l + r )
                  elif char == '-':
                     result.append( l - r )
                  elif char == '*':
                     result.append( l * r )

   return result

testCases = [
      {
         'input' : '1+2*3',
         'output' : [ 7, 9 ],
      },
      {
         'input' : '2*3-4-5',
         'output' : [ 8, -12, 7, -7, -3 ],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   assert( sorted( expression(i ) ) == sorted( o ) )
