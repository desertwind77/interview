#!/usr/bin/env python3

from buble_sort import buble_sort
from heap_sort import heap_sort
from insertion_sort import insertion_sort
#import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort

testCases = [
      [],
      [ 1 ],
      [ 2, 3 ],
      [ 9, 7, 9 ],
      [ 9, 9, 9 ],
      [ 12, 11, 13, 5, 6, 7 ],
      [ 518, 446, 909, 464, 212, 735, 681, 738, 344, 546, 150, 516, 642,
        190, 797, 753, 732, 529, 576, 396, 376, 606, 614, 662, 777, 678, 248,
        133, 384, 11, 456 ],
]

for test in testCases:
   assert( sorted( test ) == buble_sort( test.copy() ) )
   assert( sorted( test ) == heap_sort( test.copy() ) )
   assert( sorted( test ) == insertion_sort( test.copy() ) )
   print( quick_sort( test.copy() ) )
   assert( sorted( test ) == quick_sort( test.copy() ) )
   assert( sorted( test ) == selection_sort( test.copy() ) )
