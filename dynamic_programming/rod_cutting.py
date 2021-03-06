#!/usr/bin/env python3

def rod_cutting( length, profit, maxProfit={}, maxCut={} ):
    '''
    Cut the rod in such a way that achieves the maximum profit

    length      the length of the rod
    profit      the array containing the profit at each length
    '''
    if length in maxProfit:
        return maxProfit[ length ]

    if length in [ 0, 1 ]:
        return profit[ length ]
    else:
        curMax = profit[ length ]
        curCut = ( 0, length )
        for i in range( 1, int( length / 2 ) + 1 ):
            tmp = rod_cutting( i, profit, maxProfit, maxCut ) + \
                    rod_cutting( length - i, profit, maxProfit, maxCut )
            if tmp > curMax:
                curMax = tmp
                curResult = ( i, length - i )
        maxProfit[ length ] = curMax
        maxCut[ length ] = curCut
        return curMax

if __name__ == '__main__':
   testCases = [
         {
            'length' : 5,
            'cost'   : [ 0, 1, 3, 5, 5, 5 ],
            'answer' : 8,
         },
         {
            'length' : 4,
            'cost'   : [ 0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 ],
            'answer' : 6,
         },
   ]

   for test in testCases:
      length = test[ 'length' ]
      cost = test[ 'cost' ]
      answer = test[ 'answer' ]
      assert( answer == rod_cutting( length, cost ) )
