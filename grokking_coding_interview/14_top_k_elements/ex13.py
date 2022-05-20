#!/usr/bin/env python
# You are given a list of tasks that need to be run, in any order, on a server. Each
# task will take one CPU interval to execute but once a task has finished, it has a
# cooling period during which it can’t be run again. If the cooling period for all
# tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server
# needs to finish all tasks.
#
# If at any time the server can’t execute any task then it must stay idle.

testCases = [
      # a -> c -> b -> a -> c -> idle -> a
      {
         'input' : [a, a, a, b, c, c],
         'K' : 2,
         'output' : 7,
      },
      # a -> b -> idle -> idle -> a
      {
         'input' : [a, b, a],
         'K' : 3,
         'output' : 5,
      },
]
