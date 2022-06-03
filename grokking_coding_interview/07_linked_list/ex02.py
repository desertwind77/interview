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
   start = pPtr = qPtr = head

   count = 1
   while count < q:
      if count < p:
         start = pPtr
         pPtr = pPtr.next
      qPtr = qPtr.next
      count += 1
   # print( start.val if start is not None else None,
   #        pPtr.val, qPtr.val )

   prev, cur, next, end = None, pPtr, None, qPtr.next
   while cur != end:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next

   if start == pPtr:
      head = prev
   else:
      start.next = qPtr
   pPtr.next = end

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

   # head = reverse_sub_list(head, 1, 7)
   # print("Nodes of reversed LinkedList are: ", end='')
   # head.print_list()
   #
   # head = reverse_sub_list(head, 2, 9)
   # print("Nodes of reversed LinkedList are: ", end='')
   # head.print_list()
   #
   # head = reverse_sub_list(head, 2, 9)
   # print("Nodes of reversed LinkedList are: ", end='')
   # head.print_list()

main()
