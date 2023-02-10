#!/usr/bin/env python3
'''Prefix Tree or Trie'''

class PrefixTree:
    '''Prefix Tree or Trie'''
    def __init__( self ):
        self.children = {}
        self.end_of_word = False

    def insert( self, word ):
        '''Insert a word into the prefix tree'''
        if not word:
            return

        first_char = word[ 0 ]
        if first_char not in self.children:
            self.children[ first_char ] = PrefixTree()

        if len( word ) == 1:
            self.children[ first_char ].end_of_word = True
            return
        self.children[ first_char ].insert( word[ 1: ] )

    def delete( self, word ):
        ''' Delete word from the prefix tree'''
        if not word or word[ 0 ] not in self.children:
            # This string is not in the prefix tree
            return False

        node = self.children[ word[ 0 ] ]
        if len( word ) == 1:
            end_of_word = node.end_of_word
            node.end_of_word = False
            return end_of_word

        if node.delete( word[ 1: ] ) and len( node.children ) == 0:
            # One of the children contains word[ 1: ] and we already
            # deleted word[ 1: ] from that child successfully. That
            # node doesn't have any child. So this node can delete
            # that child from its list of children. Also return True
            # so that the caller of this node can do the same.
            del self.children[ word[ 0 ] ]
            return True
        return False

    def prefix_search( self, prefix='' ):
        '''Search for the node whose prefix matches prefix'''
        if not prefix or prefix[ 0 ] not in self.children:
            return None
        if len( prefix ) == 1:
            return self.children[ prefix[ 0 ] ]
        return self.children[ prefix[ 0 ] ].prefix_search( prefix[ 1: ] )

    def search( self, word ):
        '''Search if an exact word is in the tree'''
        node = self.prefix_search( prefix=word )
        # We found the node whose prefix is equal ot word and that node
        # is also the end of the word.
        return node and node.end_of_word

    def display( self, prefix='' ):
        '''Retrieve the sorted list of words contained in this node and its children'''
        # If this node is the root fo the prefix tree, it will return the sorted
        # array of words in the prefix tree.
        result = []
        if self.end_of_word:
            # The current node is the end of a word.
            result.append( prefix )
        for key in sorted( self.children.keys() ):
            # Recursively display words contained in the children
            result += self.children[ key ].display( prefix=prefix+key )
        return result

    def auto_complete( self, prefix='' ):
        '''Return the list of words starting with the prefix.'''
        if not prefix:
            # If the prefix is empty, return all the words in the prefix tree.
            return self.display()
        # Find the node of which prefix is equal to the argument prefix
        node = self.prefix_search( prefix )
        if node:
            return node.display( prefix=prefix )
        return []

def test():
    '''Test function'''
    present_list = [ 'the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their' ]
    non_present_list = [ 'hello', 'world', 'x', 'c' ]
    autocomplete_dict = {
        'a' : ['a', 'answer', 'any'],
        'b' : ['by', 'bye'],
        'th' : ['the', 'their', 'there'],
    }

    tree = PrefixTree()
    # Insert words into the prefix tree
    for i in present_list:
        tree.insert( i )
    # Verify that word is in the prefix tree
    for i in present_list:
        assert tree.search( i )
    # Verify that word is not in the prefix tree
    for i in non_present_list:
        assert not tree.search( i )
        assert tree.auto_complete( prefix=i ) == []

    assert tree.display() == sorted( present_list )
    assert tree.auto_complete() == sorted( present_list )

    # Verify the autocomplete feature
    for prefix, result in autocomplete_dict.items():
        assert tree.auto_complete( prefix=prefix ) == result

    # Delete words that are not in the tree
    for i in non_present_list:
        tree.delete( i )
        assert tree.display() == sorted( present_list )

    # Delete words that are in the tree
    deleted = []
    for i in present_list:
        tree.delete( i )
        deleted.append( i )
        cur_content = sorted( [ word for word in present_list
                                if word not in deleted ] )
        assert tree.display() == cur_content

if __name__ == '__main__':
    test()
