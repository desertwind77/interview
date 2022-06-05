#!/usr/bin/env python
# Reverse a Sub-list (medium)
#
# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the
# LinkedList from position ‘p’ to ‘q’.

class Node:
   def __init__( self, val, next=None ):
      self.val = val
      self.next = next

   def print_list( self ):
      cur = self

      while cur is not None:
         print( cur.val, end=' ' )
         cur = cur.next
      print()

def reverse_sub_list( head, p, q ):
   # locate the starting position
   beforeStart, count, start = None, 1, head
   while count < p:
      beforeStart = start
      start = start.next
      count += 1

   #     s   e
   # N 1 2 3 4 5
   #   p c
   # 0  <c n
   #     p c
   # 1    <c n
   #       p c
   # 2      <c n
   #         p c

   prev, cur, next = None, start, None
   i = 0
   while cur is not None and i < q - p + 1:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
      i += 1
   start.next = cur

   if start == head:
      head = prev
   else:
      beforeStart.next = prev

   return head

def main():
   count = 1
   head = Node( count )
   cur = head
   for _ in range( 10 ):
      count += 1
      cur.next = Node( count )
      cur = cur.next

   print("Nodes of original LinkedList are: ", end='')
   head.print_list()

   head = reverse_sub_list(head, 1, 7)
   print("Nodes of reversed LinkedList are: ", end='')
   head.print_list()

   head = reverse_sub_list(head, 1, 7)
   print("Nodes of reversed LinkedList are: ", end='')
   head.print_list()

   head = reverse_sub_list(head, 2, 9)
   print("Nodes of reversed LinkedList are: ", end='')
   head.print_list()

   head = reverse_sub_list(head, 2, 9)
   print("Nodes of reversed LinkedList are: ", end='')
   head.print_list()

main()
