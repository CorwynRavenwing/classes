class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        emptyBottles = 0
        drunk = 0
        print(f'{drunk=} {numBottles=} {emptyBottles=}')
        while numBottles:
            print(f'  Drink {numBottles}')
            drunk += numBottles
            emptyBottles += numBottles
            numBottles -= numBottles
            
            print(f'{drunk=} {numBottles=} {emptyBottles=}')

            exchange = emptyBottles // numExchange
            if exchange:
                print(f'  Exchange {exchange * numExchange} -> {exchange}')
                emptyBottles -= exchange * numExchange
                numBottles += exchange
                print(f'{drunk=} {numBottles=} {emptyBottles=}')
        return drunk

