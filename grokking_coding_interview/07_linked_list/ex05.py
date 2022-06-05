#!/usr/bin/env python
# Rotate a LinkedList (medium)
#
# Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to
# the right by ‘k’ nodes.

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

def rotate( head, k ):
   # Calculation
   cur, size = head, 0
   while cur:
      cur, size = cur.next, size + 1

   numMove = 0
   if k < size:
      numMove = k
   else:
      numMove = k % size
   numStart = size - numMove

   #print( size, numMove, numStart )

   prev, cur, i = None, head, 0
   while i < numStart:
      prev = cur
      cur = cur.next
      i += 1

   newHead, last, j = cur, cur, 0
   while j < numMove - 1:
      last = last.next
      j += 1

   prev.next = last.next
   last.next = head
   head = newHead

   return head

def main():
   head = Node(1)
   head.next = Node(2)
   head.next.next = Node(3)
   head.next.next.next = Node(4)
   head.next.next.next.next = Node(5)
   #head.next.next.next.next.next = Node(6)

   print("Nodes of original LinkedList are: ", end='')
   head.print_list()

   #result = rotate(head, 3)
   result = rotate(head, 8)
   print("Nodes of rotated LinkedList are : ", end='')
   result.print_list()

main()
