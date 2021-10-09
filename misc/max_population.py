#!/usr/bin/env python3

# https://www.youtube.com/watch?v=4UWDyJq8jZg&t=612s
# Given a set of birth year and death year of people, find the year with maximum
# population.

# Observation:
# 1) birth year will increase the populaiton and death year will decrease the
#    population. Therefore, the year with the max population will be one of the birth
#    year.
# 2) When the birth year is equal to the death year, we assume that the person was
#    born at the beginning of the year and died at the end of the year. So the
#    population will decrease at the beginning of the next year. Therefore, we will
#    assume that every death year causes the next year population to decrease by 1.
#
# Assume that
#  n = no. of people in the data
#  y = the length from min birth year to max birth year

from collections import defaultdict

def find_min_max_birth_year( data ):
   # time = O( n )
   minBirthYear = maxBirthYear = None
   for ( birth, _ ) in data:
      if minBirthYear == None or birth < minBirthYear:
         minBirthYear = birth
      if maxBirthYear == None or birth > maxBirthYear:
         maxBirthYear = birth

   return ( minBirthYear, maxBirthYear )

def find_max_death_year( data ):
   # time = O( n )
   maxDeathYear = None
   for ( _, death ) in data:
      if maxDeathYear == None or death > maxDeathYear:
         maxDeathYear = death
   return maxDeathYear

def max_population_naive1( data ):
   minBirth, _ = find_min_max_birth_year( data )
   maxDeath = find_max_death_year( data )
   size = maxDeath - minBirth + 1
   population = [ 0 ] * size

   for ( birth, death ) in data:
      bindex = birth - minBirth
      dindex = death - minBirth + 1

      for i in range( bindex, dindex ):
         population[ i ] += 1

   maxYear = 0
   for i in range( len( population ) ):
      if population[ i ] > population[ maxYear ]:
         maxYear = i

   return ( maxYear + minBirth, population[ maxYear ] )

def max_population( data ):
   minBirth, maxBirth = find_min_max_birth_year( data )
   size = maxBirth - minBirth + 1
   years = [ 0 ] * size                # time = O( y )
   population = [ 0 ] * size

   for ( birth, death ) in data:       #  time = O( n )
      bindex = birth - minBirth
      dindex = death - minBirth + 1
      years[ bindex ] += 1
      if dindex < size:
         years[ dindex ] -= 1

   maxYear = 0
   for i in range( len( years ) ):     # time = O( y )
      prevYear = 0
      if i != 0:
         prevYear = population[ i - 1 ]
      population[ i ] = prevYear + years[ i ]

      if population[ i ] > population[ maxYear ]:
         maxYear = i

   return ( maxYear + minBirth, population[ maxYear ] )

if __name__ == '__main__':
   testCases = [
         {
            'data' : [ ( 2000, 2010 ), ( 1975, 2005 ), ( 1975, 2003 ),
                       ( 1803, 1809 ), ( 1750, 1869 ), ( 1840, 1935 ),
                       ( 1803, 1921 ), ( 1894, 1921 ), ( 1900, 1900 ) ],
            'answer' : ( 1900, 4 ),
         },
   ]

   for test in testCases:
      data = test[ 'data' ]
      answer = test[ 'answer' ]
      # time = O( n * y )
      assert( answer == max_population_naive1( data ) )
      # time = O( y + n )
      assert( answer == max_population( data ) )
