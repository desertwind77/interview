#!/usr/bin/env python
#
# Palindrome LinkedList (medium)
#
# Given the head of a Singly LinkedList, write a method to check if the LinkedList is
# a palindrome or not.
#
# Your algorithm should use constant space and the input LinkedList should be in the
# original form once the algorithm is finished. The algorithm should have O(N)O(N)
# time complexity where ‘N’ is the number of nodes in the LinkedList.

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

def findMiddleElement( head ):
   slow = fast = head

   # None : None
   # 1 : 1
   # 1 2 : 2
   # 1 2 3 : 2
   # 1 2 3 4 : 3
   while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next

   return slow

def reverse( head, middle ):
   if head is None:
      return None

   beforeMiddle, cur = None, head
   while cur != middle:
      beforeMiddle = cur
      cur = cur.next

   # None
   # 1   : beforeMiddle = None
   # 1>2>3>4>5
   #   p m
   #   x<c n
   #     x<c n
   #       x<c
   #         x c
   # 1>2 3<4<5
   # 1>2>3>4
   #   p m
   prev, cur = None, middle
   while cur is not None:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next

   if beforeMiddle is not None:
      beforeMiddle.next = prev

   return head

def is_palindromic_linked_list( head ):
   if head is None:
      return False

   middle = findMiddleElement( head )
   head = reverse( head, middle )
   middle = findMiddleElement( head )

   # 1 2 3 2 1   >> 1 2 1 2 3
   # 1 2 2 1     >> 1 2 1 2
   # 1 2 2 1 1   >> 1 2 1 1 2
   # 1 2 3 2 1 1 >> 1 2 3 1 1 2
   first, second = head, middle
   result = True
   while first != middle:
      if first.value != second.value:
         result = False
      first = first.next
      second = second.next

   head = reverse( head, middle )

   return result

def main():
	head = Node(2)
	head.next = Node(4)
	head.next.next = Node(6)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(2)

	print("Is palindrome: " + str(is_palindromic_linked_list(head)))

	head.next.next.next.next.next = Node(2)
	print("Is palindrome: " + str(is_palindromic_linked_list(head)))

main()
