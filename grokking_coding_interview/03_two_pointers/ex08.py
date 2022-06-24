#!/usr/bin/env python
# Dutch National Flag Problem (medium)
#
# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat
# numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate
# the array.
#
# The flag of the Netherlands consists of three colors: red, white and blue; and
# since our input array also consists of three different numbers that is why it is
# called Dutch National Flag problem.

def dutch( arr ):
   cur, zero, two = 0, 0, len( arr ) - 1

   while cur <= two:
      if arr[ cur ] == 0:
         if cur == zero:
            zero += 1
            cur += 1
            continue

         arr[ zero ], arr[ cur ] = arr[ cur ], arr[ zero ]
         zero += 1
      elif arr[ cur ] == 2:
         if cur >= two:
            break

         arr[ two ], arr[ cur ] = arr[ cur ], arr[ two ]
         two -= 1
      else:
         cur += 1

testCases = [
      #  0  1  2  3  4
      #  1  0  2  1  0
      #  zc          t
      #  z  c        t
      #  0  1  2  1  0
      #     zc       t
      #  0  1  2  1  0
      #     z  c
      #  0  1  0  1  2
      #     z  c  t
      #  0  0  1  1  2
      #        zc t
      {
         'input' : [1, 0, 2, 1, 0],
         'output' : [0, 0, 1, 1, 2],
      },
      #  0  1  2  3  4  5
      #  2  2  0  1  2  0
      #  zc             t
      #  0  2  0  1  2  2
      #     zc       t
      #  0  2  0  1  2  2
      #     zc    t
      #  0  1  0  2  2  2
      #     zc t
      #  0  1  0  2  2  2
      #     z  ct
      #  0  0  1  2  2  2
      #        ztc
      #  0  0  1  2  2  2
      #        zt c
      {
         'input' : [2, 2, 0, 1, 2, 0],
         'output' : [0, 0, 1, 2, 2, 2 ],
      },
]

for test in testCases:
   i = test[ 'input' ]
   o = test[ 'output' ]
   dutch( i )
   assert( o == i )
