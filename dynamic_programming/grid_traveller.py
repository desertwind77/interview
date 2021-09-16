#!/usr/bin/env python3

#def grid_traveller( r, c, record={} ):
#    if r == 0 or c == 0:
#        return 0
#    elif r == 1 and c == 1:
#        return 1
#    else:
#        return grid_traveller( r - 1, c ) + grid_traveller( r, c - 1 )

def grid_traveller( r, c, record={} ):
    '''Grid traveller

    Calculate how many paths from the upper-left corner to the lower-right corner
    of a r x c table using dynamic programming.

    Args:
        r   row
        c   column
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
            result = grid_traveller( r - 1, c, record ) + grid_traveller( r, c - 1, record )
            record[ key1 ] = record[ key2 ] = result
            return result

rol = 4
col = 4
print( 'grid_traveller( %d, %d ) = %d' % ( rol, col, grid_traveller( rol, col ) ) )
