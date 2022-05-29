#!/usr/bin/env python3

# Given a dictionary, a method to do lookup in dictionary and a M x N board where
# every cell has one character. Find all possible words that can be formed by a
# sequence of adjacent characters. Note that we can move to any of 8 adjacent
# characters, but a word should not have multiple instances of same cell.
#
# Example:
# Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
#        boggle[][]   = {{'G', 'I', 'Z'},
#                        {'U', 'E', 'K'},
#                        {'Q', 'S', 'E'}};
#       isWord(str): returns true if str is present in dictionary else false.
#
# Output:  Following words of dictionary are present
#          GEEKS
#          QUIZ
#
# https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
# https://www.geeksforgeeks.org/boggle-set-2-using-trie/

def boggle_dfs( dictionary, boggle ):
   row = len( boggle )
   col = len( boggle[ 0 ] )

   for i in range( row ):
      for j in range( col ):
         root = boggle[ i ][ j ]

def bogge_trie():
   pass

if __name__ == '__main__':
   testCases = [
         {
            'dict'   : [ 'GEEKS', 'FOR', 'QUIZ', 'GO' ],
            'boggle' : [
               [ 'G', 'I', 'Z' ],
               [ 'U', 'E', 'K' ],
               [ 'Q', 'S', 'E' ],
            ],
            'answer' : [ 'GEEKS', 'QUIZ' ],
         }
   ]

   for test in testCases:
      dictionary = test[ 'dict' ]
      boggle = test[ 'boggle' ]
      answer = test[ 'answer' ]

      print( boggle_dfs( dictionary, boggle ) )
