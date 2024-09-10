class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        # we borrow some code from #1518:

        emptyBottles = 0
        drunk = 0
        print(f'{drunk=} {numBottles=} {emptyBottles=} {numExchange=}')
        while numBottles:
            print(f'  Drink {numBottles}')
            drunk += numBottles
            emptyBottles += numBottles
            numBottles -= numBottles
            
            print(f'{drunk=} {numBottles=} {emptyBottles=}')

            # can only do 1 exchange at a time
            exchange = 1 if (emptyBottles >= numExchange) else 0
            if exchange:
                print(f'  Exchange {exchange * numExchange} -> {exchange}')
                emptyBottles -= exchange * numExchange
                numBottles += exchange
                numExchange += 1        # each exchange gets worse
                print(f'{drunk=} {numBottles=} {emptyBottles=} {numExchange=}')
        return drunk

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 42 ms Beats 19.75%
# NOTE: Memory 16.61 MB Beats 26.11%
