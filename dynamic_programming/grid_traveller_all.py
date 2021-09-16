#!/usr/bin/env python3

def grid_traveller( r, c, record={} ):
    '''Grid traveller

    Calculate how many paths from the upper-left corner to the lower-right corner
    of a r x c table using dynamic programming. Also gather all the paths.

    Args:
        r   row
        c   column
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
            ( dSum, dPath ) = grid_traveller( r - 1, c, record )
            ( rSum, rPath ) = grid_traveller( r, c - 1, record )
            num_paths = dSum + rSum

            paths = []
            rpaths = []
            if dSum >= 1:
                if dPath:
                    for p in dPath:
                        paths.append( [ 'Down'] + p )
                else:
                    paths.append( [ 'Down'] )
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

rol = 4
col = 4
( num_routes, routes ) = grid_traveller( rol, col )
print( 'grid_traveller( %d, %d ) = %s' % ( rol, col, num_routes ) )
if routes:
    for r in routes:
        print( ' '.join( r ) )
