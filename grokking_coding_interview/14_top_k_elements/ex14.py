#!/usr/bin/env python
# Design a class that simulates a Stack data structure, implementing the following
# two operations:
#
# 1) push(int num): Pushes the number ‘num’ on the stack.
# 2) pop(): Returns the most frequent number in the stack. If there is a tie,
#    return the number which was pushed later.
#
# Example:
#
# After following push operations:
# push(1), push(2), push(3), push(2), push(1), push(2), push(5)
#
# 1. pop() should return 2, as it is the most frequent number
# 2. Next pop() should return 1
# 3. Next pop() should return 2

from collections import defaultdict
from heapq import *

class Element:
   def __init__( self, val, freq, seq ):
      self.freq = freq
      self.seq = seq
      self.val = val

   def __lt__( self, other ):
      # This logic to compare both frequency and sequence number
      # is invert of the traditional less-than  comparison
      # because it will be inserted into a maxHeap
      if self.freq != other.freq:
         return self.freq > other.freq
      return self.seq > other.seq

class Stack:
   def __init__( self ):
      self.seqNum = 0
      self.maxHeap = []
      self.hashMap = defaultdict( int )

   def push( self, val ):
      self.hashMap[ val ] += 1
      freq = self.hashMap[ val ]

      elem = Element( val, freq, self.seqNum )
      self.seqNum += 1
      heappush( self.maxHeap, elem )

   def pop( self ):
      topElem = heappop( self.maxHeap )

      if topElem.freq > 1:
         self.hashMap[ topElem.val ] -= 1
      else:
         del self.hashMap[ topElem.val ]

      return topElem.val

def main():
   fStack = Stack()
   fStack.push( 1 )
   fStack.push( 2 )
   fStack.push( 3 )
   fStack.push( 2 )
   fStack.push( 1 )
   fStack.push( 2 )
   fStack.push( 5 )
   print( fStack.pop() )
   print( fStack.pop() )
   print( fStack.pop() )

main()
