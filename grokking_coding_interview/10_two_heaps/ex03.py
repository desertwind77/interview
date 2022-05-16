#!/usr/bin/env python
# Given a set of investment projects with their respective profits, we need to find
# the most profitable projects. We are given an initial capital and are allowed to
# invest only in a fixed number of projects. Our goal is to choose projects that give
# us the maximum profit. Write a function that returns the maximum total capital
# after selecting the most profitable projects.
#
# We can start an investment project only when we have the required capital. Once a
# project is selected, we can assume that its profit has become our capital.
#
# Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5], Initial Capital=0,
# Number of Projects=3
# Output: 8
# Explanation:
# With ‘0’ capital, we can only select the first project, bringing out capital to 1.
# Next, we will select the second project, which will bring our capital to 3.
# Next, we will select the fourth project, giving us a profit of 5.
# After selecting the three projects, our total capital will be 8 (1+2+5).

from heapq import *

def selectProject( capitals, profits, initCapital, numProjects ):
   minHeapCapitals = []
   maxHeapProfits = []
   selected = []
   totalProfit = initCapital

   for i in range( len( capitals ) ):
      heappush( minHeapCapitals, ( capitals[ i ], i ) )

   while len( selected ) < numProjects:
      while minHeapCapitals and minHeapCapitals[ 0 ][ 0 ] <= totalProfit:
         _, i = heappop( minHeapCapitals )
         heappush( maxHeapProfits, ( -profits[ i ], i ) )

      if not maxHeapProfits:
         break
      profit, i = heappop( maxHeapProfits )
      selected.append( i )
      totalProfit += -1 * profit

   return totalProfit

testCases = [
      {
         'capitals' : [ 0, 1, 2 ],
         'profits' : [ 1, 2, 3 ],
         'initialCapital' : 1,
         'numProjects' : 2,
         'output' : 6,
      },
      {
         'capitals' : [ 0, 1, 2, 3 ],
         'profits' : [ 1, 2, 3, 5 ],
         'initialCapital' : 0,
         'numProjects' : 3,
         'output' : 8,
      }
]

for test in testCases:
   c = test[ 'capitals' ]
   p = test[ 'profits' ]
   i = test[ 'initialCapital' ]
   n = test[ 'numProjects' ]
   o = test[ 'output' ]
   assert( selectProject( c, p, i, n ) == o )
