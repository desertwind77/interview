#!/usr/bin/env python
# Reverse alternating K-element Sub-list (medium)
#
# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’
# sized sub-list starting from the head.
#
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse
# it too.
class Node:
   def __init__(self, value, next=None):
      self.value = value
      self.next = next

   def print_list(self):
      temp = self
      while temp is not None:
         print(temp.value, end=" ")
         temp = temp.next
      print()

def reverse_alternate_k_elements( head, k ):
   beforeStart, start = None, head

   while start:
      prev, cur, next = None, start, None
      i = 0
      while start and i < k:
         next = cur.next
         cur.next = prev
         prev = cur
         cur = next
         i += 1
      if beforeStart is None:
         head = prev
      else:
         beforeStart.next = prev
      start.next = cur
      beforeStart = start
      start = cur

      j = 0
      while start and j < k:
         beforeStart = start
         start = start.next
         j += 1

   return head

def main():
   head = Node(1)
   head.next = Node(2)
   head.next.next = Node(3)
   head.next.next.next = Node(4)
   head.next.next.next.next = Node(5)
   head.next.next.next.next.next = Node(6)
   head.next.next.next.next.next.next = Node(7)
   head.next.next.next.next.next.next.next = Node(8)

   print("Nodes of original LinkedList are: ", end='')
   head.print_list()

   result = reverse_alternate_k_elements(head, 2)
   print("Nodes of reversed LinkedList are: ", end='')
   result.print_list()

main()
