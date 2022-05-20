#!/usr/bin/env python
# Given a string and a number ‘K’, find if the string can be rearranged such that the
# same characters are at least ‘K’ distance apart from each other.

testCases = [
      {
         'input' : "mmpp",
         'K' : 2,
         'output' : [ "mpmp", "pmpm" ]
      },
      {
         'input' : "Programming",
         'K' : 3,
         'output' : [ "rgmPrgmiano", "gmringmrPoa", "gmrPagimnor" ] # and a few more
      },
      {
         'input' : "aab",
         'K' : 2,
         'output' : "aba",
      },
      {
         'input: "aappa",
         'K' : 3,
         'output' : "",
      },
]
