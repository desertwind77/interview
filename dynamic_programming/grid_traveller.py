#!/usr/bin/env python3

def grid_traveller_recursive( r, c ):
   '''
   Calculate how many paths from the upper-left corner to the lower-right corner
   of a r x c table
   '''

   if r == 0 or c == 0:
      return 0
   elif r == 1 and c == 1:
      return 1
   else:
      return grid_traveller_recursive( r - 1, c ) + \
             grid_traveller_recursive( r, c - 1 )

def grid_traveller_top_down( r, c, record={} ):
   '''
   Calculate how many paths from the upper-left corner to the lower-right corner
   of a r x c table using top-down dynamic programming.
   '''

   key = '(%d,%d)' % ( r, c )
   if key in record:
      return record[ key ]
   else:
      if r == 0 or c == 0:
         return 0
      elif r == 1 and c == 1:
         return 1
      else:
         key1 = '(%d,%d)' % ( r, c )
         key2 = '(%d,%d)' % ( c, r )
         result = grid_traveller_top_down( r - 1, c, record ) + \
                  grid_traveller_top_down( r, c - 1, record )
         record[ key1 ] = record[ key2 ] = result
         return result

def grid_traveller_top_down_all( r, c, record={} ):
   '''
   Calculate how many paths from the upper-left corner to the lower-right corner
   of a r x c table using top-down dynamic programming.
   '''

   key = '(%d,%d)' % ( r, c )
   if key in record:
      return record[ key ]
   else:
      if r == 0 or c == 0:
         return ( 0, None )
      elif r == 1 and c == 1:
         return ( 1, None )
      else:
         ( dSum, dPath ) = grid_traveller_top_down_all( r - 1, c, record )
         ( rSum, rPath ) = grid_traveller_top_down_all( r, c - 1, record )
         num_paths = dSum + rSum

         paths = []
         rpaths = []
         if dSum >= 1:
            if dPath:
               for p in dPath:
                  paths.append( [ 'Down'] + p )
            else:
                aths.append( [ 'Down'] )
         if rSum >= 1:
            if rPath:
               for p in rPath:
                  paths.append( [ 'Right' ] + p )
            else:
               paths.append( [ 'Right' ] )
         for p in paths:
            # Why is p[::-1] reverse of p?
            rp = [ 'Right' if s == 'Down' else 'Down' for s in p ]
            rpaths.append( rp )

         key1 = '(%d,%d)' % ( r, c )
         record[ key1 ] = ( num_paths, paths )
         key2 = '(%d,%d)' % ( c, r )
         record[ key2 ] = ( num_paths, rpaths )
         return record[ key1 ]

if __name__ == '__main__':
   testCases = [
         {
            'rol'    : 4,
            'col'    : 4,
            'answer' : 20,
         },
   ]

   for test in testCases:
      rol = test[ 'rol' ]
      col = test[ 'col' ]
      answer = test[ 'answer' ]
      assert( answer == grid_traveller_top_down( rol, col ) )

      ( num_routes, routes ) = grid_traveller_top_down_all( rol, col )
      assert( answer == num_routes )
      if routes:
         for r in routes:
            print( ' '.join( r ) )
