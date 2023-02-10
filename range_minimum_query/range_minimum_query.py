#!/usr/bin/env python3
'''
Various ways to solve the range mimimum query and the lowest common ancestry problem
'''
# pylint: disable=too-few-public-methods
#
class RMQ:
    def __init__( self, array ):
        self.array = array
        self.row = len( array )
        self.matrix = [ [ 0 for _ in range( self.row ) ]
                        for _ in range( self.row ) ]

    def query( self, i, j ):
        '''Return the position of the minimum element between [i, j]'''
        if i > j:
            i, j = j, i
        return self.matrix[ i ][ j ]

class TrivialRMQ(RMQ):
    '''
    complexity = < O( n^3 ), O( 1 ) >
    space = O( n^2 )
    '''
    def __init__( self, array ):
        super().__init__( array )

        for i in range( self.row ):
            self.matrix[ i ][ i ] = i
        for i in range( self.row ):
            for j in range( i + 1, self.row ):
                min_value = self.array[ i ]
                min_pos = i
                for k in range( i, j + 1 ):
                    if self.array[ k ] < min_value:
                        min_value = self.array[ k ]
                        min_pos = k
                self.matrix[ i ][ j ] = min_pos

class DynamicProgrammingRMQ(RMQ):
    '''
    complexity = < O( n^2 ), O( 1 ) >
    space = O( n^2 )
    '''
    def __init__( self, array ):
        super().__init__( array )

        for i in range( self.row ):
            self.matrix[ i ][ i ] = i
        for i in range( self.row ):
            for j in range( i + 1, self.row ):
                if self.array[ j ] < self.matrix[ i ][ j - 1 ]:
                    self.matrix[ i ][ j ] = j
                else:
                    self.matrix[ i ][ j ] = self.matrix[ i ][ j - 1 ]

def test():
    '''Test function'''
    array = [ 2, 4, 3, 1, 6, 7, 8, 9, 1, 7 ]
    trivial_rmq = TrivialRMQ( array )
    dynamic_rmq = DynamicProgrammingRMQ( array )

    from pprint import pprint
    assert trivial_rmq.query( 2, 7 ) == 3
    assert dynamic_rmq.query( 2, 7 ) == 3

if __name__ == '__main__':
    test()
