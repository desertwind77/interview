#!/usr/bin/env python
#
# Kth Smallest Number (hard)
#
# Given an unsorted array of numbers, find Kth smallest number in it.
#
# Please note that it is the Kth smallest number in the sorted order, not the Kth
# distinct element.
#
# A few other similar problems are:
# - Find the Kth largest number in an unsorted array.
# - Find the median of an unsorted array.
# - Find the ‘K’ smallest or largest numbers in an unsorted array.

import math
import random

#######################################################################################

def kth_smallest_number1( arr, k ):
   # Brute force:
   # time = O( n ^ 2 )
   # space = O( 1 )

   prevMin = -math.inf
   prevIndex = -1
   for i in range( k ):
      minNum = math.inf
      minIndex = -1
      for j in range( len( arr ) ):
         # the "j != prevIndex" condition is incorrect if we have 3 duplicate numbers
         #if arr[ j ] >= prevMin and j != prevIndex and arr[ j ] < minNum:
         if arr[ j ] > prevMin and arr[ j ] < minNum:
            minIndex = j
            minNum = arr[ j ]
         elif arr[ j ] == prevMin and j > prevIndex:
            minIndex = j
            minNum = arr[ j ]
            break
      prevMin = minNum
      prevIndex = minIndex
   return prevMin

#######################################################################################

def kth_smallest_number2( arr, k ):
   # Brute force using sorting
   # time = O( n log n )
   # space = O( 1 ) for in-place sort e.g. heapsort or O( n ) for non-in-place sort
   return sorted( arr )[ k - 1 ]

#######################################################################################

import heapq

def kth_smallest_number3_1( arr, k ):
   # Using maxHeap
   # time = O( N * log K + ( N - K ) * log K )
   # space = O( K )
   # Note that heapq is based on minHeap so the content of the heap will be
   # -5 -2 -1
   maxHeap = []
   for a in arr:
      heapq.heappush( maxHeap, -a )
      if len( maxHeap ) > k:
         heapq.heappop( maxHeap )

   return -maxHeap[ 0 ]

def kth_smallest_number3_2( arr, k ):
   # Using maxHeap
   # time = O( K * log K + ( N - K ) * log K )
   #      = O( N log K ) asymptotically
   # space = O( K )
   # Note that heapq is based on minHeap so the content of the heap will be
   # -5 -2 -1
   maxHeap = []

   for i in range( k ):
      heapq.heappush( maxHeap, -arr[ i ] )

   for j in range( k, len( arr ) ):
      if -arr[ j ] > maxHeap[ 0 ]:
         heapq.heappop( maxHeap )
         heapq.heappush( maxHeap, -arr[ j ] )

   return -maxHeap[ 0 ]

#######################################################################################

def kth_smallest_number4( arr, k ):
   # Using minHeap
   # time = O( N ) for building the heap + O( K log N ) for removing K numbers
   #      = O( N + K log N )
   # space = O( N )
   minHeap = []

   for a in arr:
      heapq.heappush( minHeap, a )
   result = None

   for _ in range( k ):
      result = heapq.heappop( minHeap )

   return result

#######################################################################################

def partition( arr, start, end ):
   # index : 0 1 2  3 4  5
   # pivot               *
   # array : 1 5 12 2 11 6
   # i       *
   # left    *
   #
   # array : 1 5 12 2 11 6
   # i         *
   # left      *
   #
   # array : 1 5 12 2 11 6
   # i           *
   # left        *
   #
   # array : 1 5 2 12 11 6
   # i             *
   # left          *
   #
   # array : 1 5 2 12 11 6
   # i                *
   # left          *
   #
   # array : 1 5 2 6 11 12
   # i                *
   # left          *
   #
   if start == end:
      return start

   left = start
   for i in range( start, end ):
      if arr[ i ] <= arr[ end ]:
         arr[ i ], arr[ left ] = arr[ left ], arr[ i ]
         left += 1

   arr[ left ], arr[ end ] = arr[ end ], arr[ left ]

   return left

def quickSelect( arr, k, start, end ):
   # arr : 0 1 2 *3* 4 5 6
   # k : 4
   # pivot 3 -> return arr[ 3 ]
   # pivot 5 -> quickSelect( arr, k, 0, 4 )
   # pivot 1 -> quickSelect( arr, 4, 2, 4 )
   pivot = partition( arr, start, end )
   if pivot == k - 1:
      return arr[ pivot ]
   elif pivot > k - 1:
      return quickSelect( arr, k, start, pivot - 1 )
   else:
      return quickSelect( arr, k, pivot + 1, end )

def kth_smallest_number5( arr, k ):
   if start == end:
      return start

   left = 0
   for i in range( start, end ):
      if arr[ i ] <= arr[ end ]:
         arr[ i ], arr[ left ] = arr[ left ], arr[ i ]
         left += 1

   arr[ left ], arr[ end ] = arr[ end ], arr[ left ]

   return left + 1

def quickSelect( arr, k, start, end ):
   # arr : 0 1 2 *3* 4 5 6
   # k : 4
   # pivot 3 -> return arr[ 3 ]
   # pivot 5 -> quickSelect( arr, k, 0, 4 )
   # pivot 1 -> quickSelect( arr, 4, 2, 4 )
   pivot = partition( arr, start, end )
   if pivot == k - 1:
      return arr[ pivot ]
   elif pivot > k - 1:
      return quickSelect( arr, k, start, pivot - 1 )
   else:
      return quickSelect( arr, k, pivot + 1, end )

def kth_smallest_number5( arr, k ):
   # QuickSelect which uses the partition scheme of quicksort
   # time = O( N )         for best and average case
   #      = O( N ^ 2 )     for a worst case
   #
   # The worst-case occurs when, at every step, the partition procedure splits the
   # N-length array into arrays of size ‘1’ and ‘N−1’. This can only happen when the
   # input array is sorted or if all of its elements are the same. This “unlucky”
   # selection of pivot elements requires O(N) recursive calls, leading to an
   # O(N^2) worst-case.
   return quickSelect( arr, k, 0, len( arr ) - 1 )

#######################################################################################

def randomizedPartition( arr, start, end ):
   if start == end:
      return start

   # inclusive randomize
   pivotIndex = random.randint( start, end )
   arr[ pivotIndex ], arr[ end ] = arr[ end ], arr[ pivotIndex ]

   left = start
   for i in range( start, end ):
      if arr[ i ] <= arr[ end ]:
         arr[ i ], arr[ left ] = arr[ left ], arr[ i ]
         left += 1

   arr[ left ], arr[ end ] = arr[ end ], arr[ left ]

   return left

def randomizedQuickSelect( arr, k, start, end ):
   # arr : 0 1 2 *3* 4 5 6
   # k : 4
   # pivot 3 -> return arr[ 3 ]
   # pivot 5 -> quickSelect( arr, k, 0, 4 )
   # pivot 1 -> quickSelect( arr, 4, 2, 4 )
   pivot = randomizedPartition( arr, start, end )
   if pivot == k - 1:
      return arr[ pivot ]
   elif pivot > k - 1:
      return randomizedQuickSelect( arr, k, start, pivot - 1 )
   else:
      return randomizedQuickSelect( arr, k, pivot + 1, end )

def kth_smallest_number6( arr, k ):
   # Using Quicksort's Randomized Partitioning Scheme
   #
   # As mentioned above, the worst case for Quicksort occurs when the partition
   # procedure splits the N-length array into arrays of size ‘1’ and ‘N−1’. To
   # mitigate this, instead of always picking a fixed index for pivot (e.g., in the
   # above algorithm we always pick nums[high] as the pivot), we can randomly select
   # an element as pivot. After randomly choosing the pivot element, we expect the
   # split of the input array to be reasonably well balanced on average
   #
   # time = O( N )         for best and average case
   #      = O( N ^ 2 )     for a worst case
   return randomizedQuickSelect( arr, k, 0, len( arr ) - 1 )

#######################################################################################

def median_of_medians( nums, low, high ):
   n = high - low + 1

   # if we have less than 5 elements, ignore the partitioning algorithm
   if n < 5:
      return nums[ low ]

   # partition the give array into chunks of 5 elements
   partitions = [ nums[ j : j + 5 ] for j in range( low, high + 1, 5 ) ]

   # For simplicity, lets ignore any partition with less than 5 elements
   fullPartitions = [ partition for partition in partitions if len( partition ) == 5 ]

   # sort all partitions
   sortedPartitions = [ sorted( partition ) for partition in fullPartitions ]

   # find median of all partations ; the median of each partition is at index '2'
   medians = [ partition[ 2 ] for partition in sortedPartitions ]

   return median_partition( medians, 0, len( medians ) - 1 )

def median_partition( nums, low, high ):
   if low == high:
      return low

   # Note that the returned median is an element of the array, not an index
   median = median_of_medians( nums, low, high )

   # find median in the array and swap it with 'nums[high]' which will become our pivot
   for i in range( low, high ):
      if nums[ i ] == median:
         nums[ i ], nums[ high ] = nums[ high ], nums[ i ]
         break

   pivot = nums[ high ]
   for i in range( low, high ):
      if nums[ i ] < pivot:
         nums[ i ], nums[ low ] = nums[ low ], nums[ i ]
         low += 1

   nums[ low ], nums[ high ] = nums[ high ], nums[ low ]

   return low


def find_Kth_smallest_number_rec( nums, k, start, end ):
   p = median_partition( nums, start, end )
   if p == k - 1:
      return nums[ p ]

   if p > k - 1:
      return find_Kth_smallest_number_rec( nums, k, start, p - 1 )

   return find_Kth_smallest_number_rec( nums, k, p + 1, end )

def kth_smallest_number7( arr, k ):
   # Using the Median of Medians
   # time = O( N )         even for a worst case
   return find_Kth_smallest_number_rec( arr, k, 0, len( arr ) - 1 )

testCases = [
      {
         'input' : [1, 5, 12, 2, 11, 5],
         'K' : 3,
         'output' : 5,
      },
      {
         'input' : [1, 5, 12, 2, 11, 5],
         'K' : 4,
         'output' : 5,
      },
      {
         'input' : [5, 12, 11, -1, 12],
         'K' : 3,
         'output' : 11,
      },
]

for test in testCases:
   i = test[ 'input' ]
   k = test[ 'K' ]
   o = test[ 'output' ]
   assert( kth_smallest_number1( i, k ) == o )
   assert( kth_smallest_number2( i, k ) == o )
   assert( kth_smallest_number3_1( i, k ) == o )
   assert( kth_smallest_number3_2( i, k ) == o )
   assert( kth_smallest_number4( i, k ) == o )
   assert( kth_smallest_number5( i, k ) == o )
   assert( kth_smallest_number6( i, k ) == o )
   assert( kth_smallest_number7( i, k ) == o )
