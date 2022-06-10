#!/usr/bin/env python
#
# Cycle in a Circular Array (hard)
#
# We are given an array containing positive and negative numbers. Suppose the array
# contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move
# forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should
# assume that the array is circular which means two things:
#
# 1) If, while moving forward, we reach the end of the array, we will jump to the first
#    element to continue the movement.
# 2) If, while moving backward, we reach the beginning of the array, we will jump to the
#    last element to continue the movement.
#
# Write a method to determine if the array has a cycle. The cycle should have more
# than one element and should follow one direction which means the cycle should not
# contain both forward and backward movements.

def find_next_index( arr, is_forward, current_index ):
   direction = arr[ current_index ] >= 0

   if is_forward != direction:
      # direction change
      return -1

   next_index = ( current_index + arr[ current_index ] ) % len( arr )
   if next_index == current_index:
      # one-element cycle
      next_index = -1

   return next_index

def circular_array_loop_exists( arr ):
   for i in range( len( arr ) ):
      is_forward = arr[ i ] >= 0
      slow = fast = i

      while True:
         slow = find_next_index( arr, is_forward, slow )
         fast = find_next_index( arr, is_forward, fast )
         if fast != -1:
            fast = find_next_index( arr, is_forward, fast )
         if slow == -1 or fast == -1 or slow == fast:
            break

      if slow != -1 and slow == fast:
         return True

   return False

def main():
   print( circular_array_loop_exists( [ 1, 2, -1, 2, 2 ] ) )
   print( circular_array_loop_exists( [ 2, 2, -1, 2 ] ) )
   print( circular_array_loop_exists( [ 2, 1, -1, -2 ] ) )

main()
