#!/usr/bin/env python3
'''
Fenwick tree or Binary Indexed Tree
'''
from tabulate import tabulate

class Fenwick:
    '''
    Basic Fenwick tree that supports the following operations
        prefix_sum( i )
            get the cumulative frequency up to the index i-th
            O( log n )
        point update( i )
            update the frequency at the index i-th
            O( log n )
        range query( i, j )
            find the cumulative frequency from the index i-th to j-th
            O( log n )
    '''
    def __init__( self, length, array = None ):
        '''
        class constructor

        self.tree and self.array are one-based indexing arrays
        The element 0th of these arrays are zeroed and unused.
        '''
        self.length = length + 1
        self.array = [ 0 for _ in range( self.length ) ]
        self.tree = [ 0 for _ in range( self.length ) ]

        if not array:
            return

        # Initialize the internal arrays
        self.array = [ 0 ] + array
        for i in range( 1, self.length ):
            self.tree[ i ] = self.array[ i ]

        for child in range( 1, self.length ):
            parent = child + self.get_rsb( child )
            if parent < self.length:
                self.tree[ parent ] += self.tree[ child ]

    def print( self ):
        '''
        Print the fenwick tree in a human-readable format
        '''
        data = [
            [ 'index' ] + list( range( self.length - 1 ) ),
            [ 'array' ] + self.array[ 1: ],
            [ 'tree' ] + self.tree[ 1: ],
        ]
        print( tabulate( data ) )

    def verify( self, cumulative_sums ):
        '''
        Verify the correctness of the tree
        '''
        for i, value in enumerate( cumulative_sums ):
            assert self.prefix_sum( i ) == value

    def get_rsb( self, i ):
        '''Extract the rightmost set bit (RSB)'''
        return i & -i

    def prefix_sum( self, index ):
        '''Calculate the prefix sum or cumulative frequency of an index
        O( log n )
        Note: the argument is zero-based
        '''
        index += 1
        result = 0
        while index != 0:
            result += self.tree[ index ]
            index -= self.get_rsb( index )
        return result

    def point_update( self, index, new_val ):
        '''
        Update value of arr[index] to new_val
        O( log n )
        Note: the argument is zero-based
        '''
        internal_index = index + 1
        delta = new_val - self.array[ internal_index ]
        self.point_increment( index, delta )

    def point_increment( self, index, delta ):
        '''
        Increase the value of arr[index] by delta
        O( log n )
        Note: the argument is zero-based
        '''
        # Convert the zero-based indexing in the argument
        # to the one-based indexing used in the array
        index += 1
        self.array[ index ] += delta

        pos = index
        while pos < self.length:
            self.tree[ pos ] += delta
            pos += self.get_rsb( pos )

    def range_query( self, left=None, right=None ):
        '''
        Query the inclusive cumulative frequency between left and right
        O( log n )
        Note: the argument is zero-based
        '''
        left = 0 if left is None else left
        right = self.length - 1 if right is None else right
        return self.prefix_sum( right ) - self.prefix_sum( left - 1 )

class FenwickPointQueryRangeUpdate:
    '''
    Fenwick tree that supports point query and range update in O( log n )
        point_query( i )
            find the exact value at the index i-th, NOT the cumulative value
            O( log n )
        range_update( i, j, delta )
            add the value from the index i-th to j-th by delta
            O( log n )
    '''
    def __init__( self, length, array = None ):
        self.ftree = Fenwick( length )
        self.length = length

        for i in range( self.length ):
            self.range_update( i, i, array[ i ] )

    def print( self ):
        '''
        Print the fenwick tree in a human-readable format
        '''
        self.ftree.print()

    def verify( self, point_array ):
        '''
        Verify the correctness of the tree
        '''
        for i, value in enumerate( point_array ):
            assert self.point_query( i ) == value

    def point_query( self, index ):
        '''
        Retrive the array value at the index
        O( log n )
        Note: the argument is zero-based
        '''
        return self.ftree.prefix_sum( index )

    def range_update( self, left, right, delta ):
        '''
        Update the array value from the left-th index to the right-index by delta
        O( log n )
        Note: the argument is zero-based
        '''
        self.ftree.point_increment( left, delta )
        if right + 1 < self.length:
            self.ftree.point_increment( right + 1, -delta )

class FenwickRangeQueryRangeUpdate:
    '''
    Fenwick tree that supports range query and range update in O( log n )
        range_query( i, j )
            find the cumulative sum from the index i-th to j-th
            O( log n )
        range_update( i, j, delta )
            add the value from the index i-th to j-th by delta
            O( log n )
    '''
    def __init__( self, length, array = None ):
        self.ftree1 = Fenwick( length )
        self.ftree2 = Fenwick( length )
        self.length = length

        if not array:
            return

        for i in range( self.length ):
            self.range_update( i, i, array[ i ] )

    def range_update( self, left, right, delta ):
        '''
        Update the value from the index left to right by delta
        O( log n )
        '''
        self.ftree1.point_increment( left, delta )
        if right + 1 < self.length:
            self.ftree1.point_increment( right + 1, -delta )
        self.ftree2.point_increment( left, delta * ( left - 1 ) )
        if right + 1 < self.length:
            self.ftree2.point_increment( right + 1, -delta * right )

    def range_query( self, left, right ):
        '''
        get the cumulative sum from left-th to right-th
        O( log n )
        '''
        return self.prefix_sum( right ) - self.prefix_sum( left - 1 )

    def prefix_sum( self, index ):
        '''
        get the cumulative sum from 0-th to index-th
        O( log n )
        '''
        return self.ftree1.prefix_sum( index ) * index - self.ftree2.prefix_sum( index )

    def print( self ):
        '''
        Print the fenwick tree in a human-readable format
        '''
        self.ftree1.print()
        self.ftree2.print()

    def verify( self, cumulative_sums ):
        '''
        Verify the correctness of the tree
        '''
        for i, value in enumerate( cumulative_sums ):
            assert self.prefix_sum( i ) == value

def main():
    '''Test funciton'''
    test_array = [ 1, 0, 2, 1, 1, 3, 0, 4, 2, 5, 2, 2, 3, 1, 0, 2 ]
    cumulative_sums1 = [ 1, 1, 3, 4, 5, 8, 8, 12, 14, 19, 21, 23, 26, 27, 27, 29 ]
    cumulative_sums2 = [ 1, 4, 6, 7, 8, 11, 11, 15, 17, 22, 24, 26, 29, 30, 30, 32 ]

    fenwick = Fenwick( len( test_array ), test_array )
    fenwick.verify( cumulative_sums1 )
    fenwick.print()

    # Update the 1st element in the zero-based test_array from 0 to 3.
    fenwick.point_update( 1, 3 )
    fenwick.verify( cumulative_sums2 )
    fenwick.print()

    assert fenwick.range_query( 10, 13 ) == 8

    fenwick_pqru = FenwickPointQueryRangeUpdate( len( test_array ), test_array )
    #fenwick_pqru.print()
    for i, value in enumerate( test_array ):
        assert fenwick_pqru.point_query( i ) == value

    fenwick_rqru = FenwickRangeQueryRangeUpdate( len( test_array ), test_array )
    fenwick_rqru.verify( cumulative_sums1 )
    #fenwick_rqru.print()

if __name__ == '__main__':
    main()
