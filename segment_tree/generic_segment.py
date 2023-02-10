#!/usr/bin/env python3
'''An implementation of a generic Segment tree'''
#pylint: disable=too-many-arguments
#pylint: disable=unused-argument

import sys

class SegmentTree:
    '''An implementation of a generic Segment tree'''
    def __init__( self, array ):
        self.size = len( array )
        self.seg_tree = [ 0 for _ in range( 2 * self.size - 1 ) ]
        self.build( array, 0, 0, self.size - 1 )

    def build( self, array, root, low, high ):
        '''Build a segment tree from array[ low, high ]'''
        if low == high:
            self.seg_tree[ root ] = self.leaf_node( array, root, low, high )
            return

        left_child = 2 * root + 1
        right_child = 2 * root + 2
        mid = int( ( low + high ) / 2 )

        self.build( array, left_child, low, mid )
        self.build( array, right_child, mid + 1, high )
        self.seg_tree[ root ] = \
                self.merge( self.seg_tree[ left_child ],
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
                    self.merge( self.seg_tree[ left_child ],
                                self.seg_tree[ right_child ] )

    def update( self, pos, new_val ):
        '''Front end for the update operation'''
        self.do_update( pos, new_val, 0, self.size - 1, 0 )

    def do_range_query( self, range_low, range_high, low, high, root ):
        '''Recursive range query for the range [ range_low, range_high ]'''
        if range_low <= low and range_high >= high:
            return self.seg_tree[ root ]
        if range_low > high or range_high < low:
            return self.invalid_query_result()

        mid = int( ( low + high ) / 2 )
        left_child = 2 * root + 1
        right_child = 2 * root + 2

        left_min = self.do_range_query( range_low, range_high,
                                        low, mid, left_child )
        right_min = self.do_range_query( range_low, range_high,
                                         mid + 1, high, right_child )
        return self.merge( left_min, right_min )

    def range_query( self, range_low, range_high ):
        '''Front end for the range query operation'''
        return self.do_range_query( range_low, range_high,
                                    0, self.size - 1, 0 )

    def invalid_query_result( self ):
        '''The return value for the range query with invalid range'''
        return 0

    def leaf_node( self, array, root, low, high ):
        '''The value to store at the leaf nodes'''
        return 0

    def merge( self, val1, val2 ):
        '''Merge the value from the left child and the right child'''
        return 0

class MinSegmentTree( SegmentTree ):
    '''Segment Tree for storing the minimum value of each segment'''
    def invalid_query_result( self ):
        return sys.maxsize

    def leaf_node( self, array, root, low, high ):
        return array[ low ]

    def merge( self, val1, val2 ):
        return min( val1, val2 )

class MinCountSegmentTree( SegmentTree ):
    '''Segment Tree for answering the minimum value and the numbers
    of its appearances in the array'''
    def invalid_query_result( self ):
        return ( sys.maxsize, 0 )

    def leaf_node( self, array, root, low, high ):
        return ( array[ low ], 1 )

    def merge( self, val1, val2 ):
        if val1[ 0 ] < val2[ 0 ]:
            return val1
        if val1[ 0 ] > val2[ 0 ]:
            return val2
        return ( val1[ 0 ], val1[ 1 ] + val2[ 1 ] )

class GcdSegmentTree( SegmentTree ):
    '''Segment Tree for answering the greatest common divisor'''
    def gcd( self, val1, val2 ):
        '''Compute the greatest common diviser'''
        if val2 == 0:
            return val1
        return self.gcd( val2, val1 % val2 )

    def lcm( self, val1, val2 ):
        '''Compute the least common multiplier'''
        return int( val2 * val1 / self.gcd( val1, val2 ) )

    def invalid_query_result( self ):
        return None

    def leaf_node( self, array, root, low, high ):
        return array[ low ]

    def merge( self, val1, val2 ):
        if not val1 and not val2:
            return None
        if not val1:
            return val2
        if not val2:
            return val1
        return self.gcd( val1, val2 )

class LcmSegmentTree( GcdSegmentTree ):
    '''Segment Tree for answering the least common multiplier'''
    def merge( self, val1, val2 ):
        if not val1 and not val2:
            return None
        if not val1:
            return val2
        if not val2:
            return val1
        return self.lcm( val1, val2 )

def test_min_segment_tree():
    '''Test function for Min Segment Tree'''
    array = [ -1, 2, 4, 6 ]
    seg_tree = [ -1, -1, 4, -1, 2, 4, 6 ]
    min_tree = MinSegmentTree( array )
    assert min_tree.seg_tree == seg_tree
    assert min_tree.range_query( 1, 3 ) == 2

    seg_tree = [ -1, -1, 4, -1, 2, 1, 6 ]
    min_tree.update( 2, 1 )
    assert min_tree.range_query( 1, 3 ) == 1

def test_min_count_segment_tree():
    '''Test function for Min Segment Tree'''
    array = [ -1, 2, 4, -1, -1, 3, 5, 7 ]
    seg_tree = [ (-1, 3), (-1, 2), (-1, 1), (-1, 1),
                 (-1, 1), (-1, 1), (5, 1), (-1, 1),
                 (2, 1), (4, 1), (-1, 1), (-1, 1),
                 (3, 1), (5, 1), (7, 1) ]
    min_count_tree = MinCountSegmentTree( array )
    assert min_count_tree.seg_tree == seg_tree
    assert min_count_tree.range_query( 1, 4 ) == ( -1, 2 )

    seg_tree = [ (-1, 2), (-1, 1), (-1, 1), (-1, 1),
                 (4, 1), (-1, 1), (5, 1), (-1, 1),
                 (2, 1), (4, 1), (5, 1), (-1, 1),
                 (3, 1), (5, 1), (7, 1)]
    min_count_tree.update( 3, ( 5, 1 ) )
    assert min_count_tree.seg_tree == seg_tree
    assert min_count_tree.range_query( 1, 4 ) == ( -1, 1 )

def test_gcd_segment_tree():
    '''Test function for GCD Segment Tree'''
    array = [ 20, 10, 4, 8, 6, 9, 7, 21 ]
    seg_tree = [ 1, 2, 1, 10, 4, 3, 7, 20, 10, 4, 8, 6, 9, 7, 21 ]
    gcd_tree = GcdSegmentTree( array )
    assert gcd_tree.seg_tree == seg_tree
    assert gcd_tree.range_query( 1, 4 ) == 2

    gcd_tree.update( 1, 8 )
    gcd_tree.update( 4, 20 )
    gcd_tree.update( 5, 40 )
    gcd_tree.update( 6, 80 )
    gcd_tree.update( 7, 100 )
    seg_tree = [ 4, 4, 20, 4, 4, 20, 20, 20,
                 8, 4, 8, 20, 40, 80, 100 ]
    assert gcd_tree.seg_tree == seg_tree
    assert gcd_tree.range_query( 5, 6 ) == 40

def test():
    '''Test function'''
    test_min_segment_tree()
    test_min_count_segment_tree()
    test_gcd_segment_tree()

if __name__ == '__main__':
    test()
