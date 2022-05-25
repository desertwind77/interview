#!/usr/bin/env python3
# Leetcode 4 : Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
   pass

testCases = [
      {
         'num1'   : [ 1, 3 ],
         'num2'   : [ 2 ],
         'output' : 2.0,
      },
      {
         'num1'   : [ 1, 2 ],
         'num2'   : [ 3, 4 ],
         'output' : 2.5,
      },
      {
         'num1'   : [ 0, 0 ],
         'num2'   : [ 0, 0 ],
         'output' : 0.0,
      },
      {
         'num1'   : [],
         'num2'   : [ 1 ],
         'output' : 1.0,
      },
      {
         'num1'   : [ 2 ],
         'num2'   : [],
         'output' : 2.0,
      },
]
