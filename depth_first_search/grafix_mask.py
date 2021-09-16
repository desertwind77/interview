#!/usr/bin/env python3

# https://community.topcoder.com/stat?c=problem_statement&pm=2998&rd=5857
#
# In one mode of the grafix software package, the user blocks off portions of
# a masking layer using opaque rectangles. The bitmap used as the masking
# layer is 400 pixels tall and 600 pixels wide. Once the rectangles have been
# blocked off, the user can perform painting actions through the remaining
# areas of the masking layer, known as holes. To be precise, each hole is a
# maximal collection of contiguous pixels that are not covered by any of the
# opaque rectangles. Two pixels are contiguous if they share an edge, and
# contiguity is transitive.
#
# You are given a String[] named rectangles, the elements of which specify
# the rectangles that have been blocked off in the masking layer. Each String
# in rectangles consists of four integers separated by single spaces, with no
# additional spaces in the string. The first two integers are the window
# coordinates of the top left pixel in the given rectangle, and the last two
# integers are the window coordinates of its bottom right pixel. The window
# coordinates of a pixel are a pair of integers specifying the row number and
# column number of the pixel, in that order. Rows are numbered from top to
# bottom, starting with 0 and ending with 399. Columns are numbered from left
# to right, starting with 0 and ending with 599. Every pixel within and along
# the border of the rectangle defined by these opposing corners is blocked
# off.
#
# Return a int[] containing the area, in pixels, of every hole in the
# resulting masking area, sorted from smallest area to greatest.
#
# Definition
# Class:             grafixMask
# Method:            sortedAreas
# Parameters:        String[]
# Returns:           int[]
# Method signature:  int[] sortedAreas(String[] rectangles)
# (be sure your method is public)
#
# Notes
# - Window coordinates are not the same as Cartesian
# coordinates. Follow the definition given in the second
# paragraph of the problem statement.
#
# Constraints
# - rectangles contains between 1 and 50 elements,inclusive
# - each element of rectangles has the form "ROW COL ROW
# COL", where: "ROW" is a placeholder for a non-zero-padded
# integer between 0 and 399, inclusive; "COL" is a placeholder
# for a non-zero-padded integer between 0 and 599, inclusive;
# the first row number is no greater than the second row
# number; the first column number is no greater than the
# second column number

class Point:
   def __init__( self, x, y ):
      self.x = x
      self.y = y

   def __repr__( self ):
      return "({},{})".format( self.x, self.y )

def getPoints( txt ):
   '''Convert a string into two points, topLeft and bottomRight'''
   nums = txt.split()
   assert( len( nums ) == 4 )
   topLeft = Point( int( nums[ 0 ] ), int( nums[ 1 ] ) )
   bottomRight = Point( int( nums[ 2 ] ), int( nums[ 3 ] ) )
   return ( topLeft, bottomRight )

def setRectangle( filled, rec ):
   '''Mask the area of a rectangle defined by rec'''
   ( topLeft, bottomRight ) = getPoints( rec )

   for i in range( topLeft.x, bottomRight.x + 1 ):
      for j in range( topLeft.y, bottomRight.y + 1 ):
         filled[ i ][ j ] = True

def init( rectangles, row, col ):
   # Note that [ [ False ] * COL ] ] * ROW doesn't work because it is equivalent to
   # the following:
   # a = [ False ] * COL
   # b = [ a, a, ..., a ]
   # When we update filled, like filled[ 0, 0 ] = True, column 0 of all rows will be
   # updated.
   filled = [ [ False for _ in range( 0, col ) ] for _ in range( 0, row ) ]

   # Mask the area defined by all the rectangles
   for rec in rectangles:
      setRectangle( filled, rec )

   return filled

def isFree( filled, row, col, p ):
   if p.x < 0 or p.x >= row or p.y < 0 or p.y >= col:
      return False
   elif filled[ p.x ][ p.y ]:
      return False
   return True

def leftPoint( p ):
   return Point( p.x - 1, p.y )

def rightPoint( p ):
   return Point( p.x + 1, p.y )

def upPoint( p ):
   return Point( p.x, p.y - 1 )

def downPoint( p ):
   return Point( p.x, p.y + 1 )

def doFillRecursive( filled, row, col, p ):
   if not isFree( filled, row, col, p ):
      return 0
   result = 1
   filled[ p.x ][ p.y ] = True
   result += doFillRecursive( filled, row, col, upPoint( p ) )
   result += doFillRecursive( filled, row, col, downPoint( p ) )
   result += doFillRecursive( filled, row, col, leftPoint( p ) )
   result += doFillRecursive( filled, row, col, rightPoint( p ) )

   return result

def doFillIterative( filled, row, col, p ):
   if not isFree( filled, row, col, p ):
      return

   stack = []
   result = 0
   stack.append( p )
   while len( stack ):
      top = stack.pop()
      if not isFree( filled, row, col, top ):
         continue
      result += 1
      filled[ top.x ][ top.y ] = True
      stack.append( upPoint( top ) )
      stack.append( downPoint( top ) )
      stack.append( leftPoint( top ) )
      stack.append( rightPoint( top ) )
   return result

def sortedAreasRecursive( rectangles, row, col ):
   filled = init( rectangles, row, col )

   result = []
   for i in range( 0, row ):
      for j in range( 0, col ):
         p = Point( i, j )
         if not isFree( filled, row, col, p ):
            continue
         r = doFillRecursive( filled, row, col, p )
         if r:
            result.append( r )
   return sorted( result )

def sortedAreasIterative( rectangles, row, col ):
   filled = init( rectangles, row, col )

   result = []
   for i in range( 0, row ):
      for j in range( 0, col ):
         p = Point( i, j )
         if not isFree( filled, row, col, p ):
            continue
         r = doFillIterative( filled, row, col, p )
         if r:
            result.append( r )
   return sorted( result )

if __name__ == '__main__':
   testCases = [
         { 'input'  : [ "0 2 4 2" ],
           'output' : [ 10, 10 ],
           'row'    : 5,
           'col'    : 5,
           'function' : sortedAreasRecursive,
         },
         { 'input'  : [ "0 2 4 2" ],
           'output' : [ 10, 10 ],
           'row'    : 5,
           'col'    : 5,
           'function' : sortedAreasIterative,
         },
         { 'input'  : [ "0 292 399 307" ],
           'output' : [ 116800,  116800 ],
           'row'    : 400,
           'col'    : 600,
           'function' : sortedAreasIterative,
         },
         { 'input'  : [ "48 192 351 207", "48 392 351 407", "120 52 135 547",
                        "260 52 275 547" ],
           'output' : [ 22816,  192608 ],
           'row'    : 400,
           'col'    : 600,
           'function' : sortedAreasIterative,
         },
         { 'input'  : [ "0 192 399 207", "0 392 399 407", "120 0 135 599",
                        "260 0 275 599" ],
           'output' : [ 22080,  22816,  22816,  23040,  23040,  23808,
                        23808,  23808,  23808 ],
           'row'    : 400,
           'col'    : 600,
           'function' : sortedAreasIterative,
         },
         { 'input'  : [ "50 300 199 300", "201 300 350 300", "200 50 200 299",
                        "200 301 200 550" ],
           'output' : [ 1,  239199 ],
           'row'    : 400,
           'col'    : 600,
           'function' : sortedAreasIterative,
         },
         { 'input'  : [ "0 20 399 20", "0 44 399 44", "0 68 399 68", "0 92 399 92",
                        "0 116 399 116", "0 140 399 140", "0 164 399 164", "0 188 399 188",
                        "0 212 399 212", "0 236 399 236", "0 260 399 260", "0 284 399 284",
                        "0 308 399 308", "0 332 399 332", "0 356 399 356", "0 380 399 380",
                        "0 404 399 404", "0 428 399 428", "0 452 399 452", "0 476 399 476",
                        "0 500 399 500", "0 524 399 524", "0 548 399 548", "0 572 399 572",
                        "0 596 399 596", "5 0 5 599", "21 0 21 599", "37 0 37 599",
                        "53 0 53 599", "69 0 69 599", "85 0 85 599", "101 0 101 599",
                        "117 0 117 599", "133 0 133 599", "149 0 149 599", "165 0 165 599",
                        "181 0 181 599", "197 0 197 599", "213 0 213 599", "229 0 229 599",
                        "245 0 245 599", "261 0 261 599", "277 0 277 599", "293 0 293 599",
                        "309 0 309 599", "325 0 325 599", "341 0 341 599", "357 0 357 599",
                        "373 0 373 599", "389 0 389 599" ],
           'output' : [ 15,  30,  45,  45,  45, 45,  45,  45,  45,  45,  45,
                        45,  45,  45,  45,  45,  45, 45,  45,  45,  45,  45,
                        45, 45,  45,  45,  100,  115, 115,  115,  115,  115,
                        115, 115,  115,  115,  115,  115, 115,  115,  115,
                        115,  115, 115,  115,  115,  115,  115, 115,  115,
                        115,  200,  230, 230,  230,  230,  230,  230, 230,
                        230,  230,  230,  230, 230,  230,  230,  230,  230,
                        230,  230,  230,  230,  230, 230,  230,  230,  300,  300,
                        300,  300,  300,  300,  300, 300,  300,  300,  300,  300,
                        300,  300,  300,  300,  300, 300,  300,  300,  300,  300,
                        300,  300,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345,  345,  345,
                        345,  345,  345,  345,  345, 345,  345,  345 ],
           'row'    : 400,
           'col'    : 600,
           'function' : sortedAreasIterative,
         },
   ]

   for test in testCases:
      fn = test[ 'function' ]
      inp = test[ 'input' ]
      outp = test[ 'output' ]
      row = test[ 'row' ]
      col = test[ 'col' ]
      result = fn( inp, row, col )
      assert( sorted( test[ 'output' ] ) == result )
      print( 'Passed' )
