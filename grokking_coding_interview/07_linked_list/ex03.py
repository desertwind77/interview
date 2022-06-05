#!/usr/bin/env python
# Reverse every K-element Sub-list (medium)
#
# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list
# starting from the head.
#
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse
# it too.

from __future__ import print_function

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

def reverse_every_k_elements( head, k ):
   beforeStart, start = None, head 
   while start:
      # Reverse k elements
      # h
      # 1>2>3>4>5>6>7>8>N
      # s
      # beforeStart = None, i = 0
      #<c n
      # P c i = 1
      #<1 2>3>4>5>6>7>8>N
      # P<c n
      #   p c i = 2
      #<1<2 3>4>5>6>7>8>N
      #   p<c n
      #     p c i = 3
      #<1<2<3 4>5>6>7>8>N
      #     h
      # b
      # 3>2>1>4>5>6>7>8>N
      # h   b s
      #     P c
      prev, cur = None, start
      i = 0
      while cur and i < k:
         next = cur.next
         cur.next = prev
         prev = cur
         cur = next
         i += 1
      if beforeStart is None:
         head = prev
      else:
         beforeStart.next = prev
      beforeStart = start
      start.next = cur

      # Forward the start pointer by k
      start = cur

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
   result = reverse_every_k_elements(head, 3)
   print("Nodes of reversed LinkedList are: ", end='')
   result.print_list()

main()
