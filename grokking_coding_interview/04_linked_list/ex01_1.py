#!/usr/bin/env python
# Given the head of a LinkedList with a cycle, find the length of the cycle.

class Node:
   def __init__( self, value, next=None ):
      self.value = value
      self.next = next

def find_cycle_length( head ):
   def calculate_cycle_length( head ):
      cur, length = head, 0

      while True:
         cur = cur.next
         length += 1
         if cur == head:
            break

      return length

   slow = fast = head

   while fast is not None and fast.next is not None:
      fast = fast.next.next
      slow = slow.next

      if fast == slow:
         return calculate_cycle_length( slow )
   return 0

def main():
   head = Node(1)
   head.next = Node(2)
   head.next.next = Node(3)
   head.next.next.next = Node(4)
   head.next.next.next.next = Node(5)
   head.next.next.next.next.next = Node(6)
   head.next.next.next.next.next.next = head.next.next
   print("LinkedList cycle length: " + str(find_cycle_length(head)))

   head.next.next.next.next.next.next = head.next.next.next
   print("LinkedList cycle length: " + str(find_cycle_length(head)))

main()
