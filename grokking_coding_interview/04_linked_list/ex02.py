#!/usr/bin/env python
#
# Start of LinkedList Cycle (medium)
#
# Given the head of a Singly LinkedList that contains a cycle, write a function to
# find the starting node of the cycle.

class Node:
   def __init__( self, value, next=None ):
      self.value = value
      self.next = next

   def print_list( self ):
      cur = self

      while cur:
         print( self.value, end='' )
         cur = cur.next
      print()

def calculate_cycle_length( head ):
   cur, length = head, 0

   while True:
      cur = cur.next
      length += 1
      if cur == head:
         break

   return length

def find_cycle_start( head ):
   length = 0

   slow = fast = head
   while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
         length = calculate_cycle_length( slow )
         break

   slow = fast = head
   while length > 0:
      slow = slow.next
      length -= 1

   while slow != fast:
      slow = slow.next
      fast = fast.next

   return slow

def main():
   head = Node(1)
   head.next = Node(2)
   head.next.next = Node(3)
   head.next.next.next = Node(4)
   head.next.next.next.next = Node(5)
   head.next.next.next.next.next = Node(6)

   head.next.next.next.next.next.next = head.next.next
   print("LinkedList cycle start: " + str(find_cycle_start(head).value))

   head.next.next.next.next.next.next = head.next.next.next
   print("LinkedList cycle start: " + str(find_cycle_start(head).value))

   head.next.next.next.next.next.next = head
   print("LinkedList cycle start: " + str(find_cycle_start(head).value))

main()
