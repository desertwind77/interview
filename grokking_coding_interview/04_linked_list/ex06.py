#!/usr/bin/env python
#
# Rearrange a LinkedList (medium)
#
# Given the head of a Singly LinkedList, write a method to modify the LinkedList such
# that the nodes from the second half of the LinkedList are inserted alternately to
# the nodes from the first half in reverse order. So if the LinkedList has nodes 1 ->
# 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return
# 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
#
# Your algorithm should not use any extra space and the input LinkedList should be
# modified in-place.

class Node:
   def __init__( self, value, next=None ):
      self.value = value
      self.next = next

   def print_list( self ):
      cur = self

      while cur is not None:
         print( cur.value, end=' ' )
         cur = cur.next
      print()


def reverse( head ):
   # 1>2>3*>4>5
   # 1>2>3>None
   # 5>4>3>None
   prev = None
   cur = head
   while cur is not None:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
   return prev

def reorder( head ):
   if head is None or head.next is None:
      return

   # Find middle
   slow = fast = head
   while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next
   middle = slow

   first, second = head, reverse( middle )
   first.print_list()
   second.print_list()
   # 2 4 6 8 10 12
   # middle = 8
   # first list  :  2  4 6 8
   # second list : 12 10 8
   #
   # first:second
   # 2:12   2>12>4
   # 4:10   2>12>4>10>6
   # 6:8    2>12>4>10>6>8>8
   # 8:N
   #
   # 2 4 6 8 10
   # middle = 6
   # first list  :   2 4 6
   # second list :  10 8 6
   #
   # first:second
   # 2:10   2>10>4
   # 4:8    2>10>4>8>6
   # 6:6    2>10>4>8>6>6   first = None
   #        2>10>4>8>6>None
   while first is not None and second is not None:
      tmp = first.next
      first.next = second
      first = tmp

      tmp = second.next
      second.next = first
      second = tmp

   if first is not None:
      first.next = None

def main():
   head = Node(2)
   head.next = Node(4)
   head.next.next = Node(6)
   head.next.next.next = Node(8)
   head.next.next.next.next = Node(10)
   head.next.next.next.next.next = Node(12)
   reorder(head)
   head.print_list()

main()
