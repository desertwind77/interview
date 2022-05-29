/*
 * Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
 *
 * Example 1:
 *
 * Input: c = 5
 * Output: true
 * Explanation: 1 * 1 + 2 * 2 = 5
 * Example 2:
 *
 * Input: c = 3
 * Output: false
 * Example 3:
 *
 * Input: c = 4
 * Output: true
 * Example 4:
 *
 * Input: c = 2
 * Output: true
 * Example 5:
 *
 * Input: c = 1
 * Output: true
 */
#include <iostream>
#include <stdlib.h>

using namespace std;

bool judgeSquareSum( int c ) {
   bool *isSqrtable = (bool *) malloc( sizeof( bool ) * ( c + 1 ) );

   int i = 0;
   while( i < c + 1 ) {
      isSqrtable[ i ] = false;
      i++;
   }

   long j = 0;
   while( j * j <= c ) {
      isSqrtable[ j * j ] = true;
      j++;
   }

   int k = c;
   while( k >= 0 ) {
      int l = c - k; 
      if( isSqrtable[ k ] && isSqrtable[ l ] ) return true;
      k--;
   }

   return false;
}

int main() {
   cout << judgeSquareSum( 10000000 ) << endl;
   return 0;
}
