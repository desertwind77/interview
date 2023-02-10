#!/usr/bin/env python3
'''
Example of Segment tree to find the minimum number in a range
'''
#pylint: disable=too-many-arguments

import sys

class SegmentTree:
    '''Segment tree to store the minimum value'''
    def __init__( self, array ):
        self.size = len( array )
        self.seg_tree = [ 0 for _ in range( 2 * self.size ) ]
        self.build( array, 0, 0, self.size - 1 )

    def build( self, array, root, low, high ):
        '''Build a segment tree from array[ low, high ]'''
        if low == high:
            self.seg_tree[ root ] = array[ low ]
            return

        left_child = 2 * root + 1
        right_child = 2 * root + 2
        mid = int( ( low + high ) / 2 )

        self.build( array, left_child, low, mid )
        self.build( array, right_child, mid + 1, high )
        self.seg_tree[ root ] = \
                min( self.seg_tree[ left_child ],
                     self.seg_tree[ right_child ] )

    def do_update( self, pos, new_val, low, high, root ):
        '''Recursively call the update operation'''
        if low == high:
            self.seg_tree[ root ] = new_val
        else:
            left_child = 2 * root + 1
            right_child = 2 * root + 2
            mid = int( ( low + high ) / 2 )

            if pos <= mid:
                self.do_update( pos, new_val, low, mid, left_child )
            else:
                self.do_update( pos, new_val, mid + 1, high, right_child )
            self.seg_tree[ root ] = \
                    min( self.seg_tree[ left_child ],
                         self.seg_tree[ right_child ] )

    def update( self, pos, new_val ):
        '''Front end for the update operation'''
        self.do_update( pos, new_val, 0, self.size - 1, 0 )

    def do_range_query( self, range_low, range_high, low, high, root ):
        '''Recursive range query for the range [ range_low, range_high ]'''
        if range_low <= low and range_high >= high:
            return self.seg_tree[ root ]
        if range_low > high or range_high < low:
            return sys.maxsize

        mid = int( ( low + high ) / 2 )
        left_child = 2 * root + 1
        right_child = 2 * root + 2

        left_min = self.do_range_query( range_low, range_high,
                                        low, mid, left_child )
        right_min = self.do_range_query( range_low, range_high,
                                         mid + 1, high, right_child )
        return min( left_min, right_min )

    def range_query( self, range_low, range_high ):
        '''Front end for the range query operation'''
        return self.do_range_query( range_low, range_high,
                                    0, self.size - 1, 0 )

def test():
    '''Test function'''
    array = [ -1, 2, 4, 6 ]
    seg_tree = [ -1, -1, 4, -1, 2, 4, 6, 0 ]
    min_tree = SegmentTree( array )
    assert min_tree.seg_tree == seg_tree
    assert min_tree.range_query( 1, 3 ) == 2

    seg_tree = [ -1, -1, 4, -1, 2, 1, 6, 0 ]
    min_tree.update( 2, 1 )
    assert min_tree.range_query( 1, 3 ) == 1

if __name__ == '__main__':
    test()
