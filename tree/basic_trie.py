#!/usr/bin/env python3
'''Trie Data Structure'''

class Trie:
    '''A Trie data structure'''
    def __init__( self ):
        # The number of occurrences of word ending at this node
        self.word = 0
        # The number of occurrences of prefix ending at this node
        self.prefixes = 0

        lowercase_alphabet = \
                list( map( chr, range( ord( 'a' ), ord( 'z' ) + 1 ) ) )
        self.children = { c: None for c in lowercase_alphabet }

    def add_word( self, word ):
        '''Add a word to the trie'''
        if word == '':
            # Keep track of the number of occurrences of the word
            self.word += 1
        else:
            self.prefixes += 1

            if not self.children[ word[ 0 ] ]:
                self.children[ word[ 0 ] ] = Trie()
            self.children[ word[ 0 ] ].add_word( word[ 1: ] )

    def count_word( self, word ):
        '''Count the number of occurrences of word in the Trie'''
        if word == '':
            return self.word
        if not self.children[ word[ 0 ] ]:
            return 0
        return self.children[ word[ 0 ] ].count_word( word[ 1: ] )

    def count_prefix( self, prefix ):
        '''Count the number of occurrences of prefix in the Trie'''
        if prefix == '':
            return self.prefixes
        if not self.children[ prefix[ 0 ] ]:
            return 0
        return self.children[ prefix[ 0 ] ].count_prefix( prefix[ 1: ] )

    def count_word_missing( self, word, missing_letters ):
        '''Find a word in the Trie but a single letter was deleted from the word'''
        print( 'missing', word, missing_letters )
        if word == '':
            return self.word

        if not self.children[ word[ 0 ] ]:
            if missing_letters == 0:
                return 0
            return self.count_word_missing( word[ 1: ], missing_letters - 1 )

        result = 0
        # case 1 : word[ 0 ] is the one missing
        if missing_letters > 0:
            result += self.count_word_missing( word, missing_letters -1 )
        # case 2 :  word[ 0 ] is present
        result += self.children[ word[ 0 ] ].count_word_missing(
                word[ 1: ] , missing_letters )
        return result

def test():
    '''Test routine'''
    #  root
    #  |
    #  b----c----r
    #  |    |    |
    #  a-e  a    a
    #  |    |    |
    #  l-t  t-p  t
    #  |
    #  l
    words = [ 'cat', 'bat', 'ball', 'rat', 'cap', 'be' ]

    trie = Trie()
    for word in words:
        trie.add_word( word )
    for word in words:
        assert trie.count_word( word ) == 1

    prefix_count = {
            'b' : 3,
            'ba' : 2,
            'bal' : 1,
            'c' : 2,
            'ca' : 2,
            'r' : 1,
            'ra' : 1,
    }

    for prefix, count in prefix_count.items():
        assert trie.count_prefix( prefix ) == count

    assert trie.count_word_missing( 'acat', 1 ) == 1

    for word in words:
        trie.add_word( word )
    for word in words:
        assert trie.count_word( word ) == 2

if __name__ == '__main__':
    test()
