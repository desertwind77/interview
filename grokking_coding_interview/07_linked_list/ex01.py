#!/usr/bin/env python
# Reverse a LinkedList (easy)
#
# Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to
# return the new head of the reversed LinkedList.

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

def reverse( head ):
   # time = O(N)
   # space = O(1)
   #
   # N 2 4 6 8 10 N
   # p<c n
   #   p<c n
   #     p<c n
   #       p<c n
   #         p<c  n
   #           p  c
   prev, cur, next = None, head, None
   while cur:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
   head = prev
   return head

def main():
   head = Node(2)
   head.next = Node(4)
   head.next.next = Node(6)
   head.next.next.next = Node(8)
   head.next.next.next.next = Node(10)

   print("Nodes of original LinkedList are: ", end='')
   head.print_list()

   result = reverse(head)
   print("Nodes of reversed LinkedList are: ", end='')
   result.print_list()

main()
