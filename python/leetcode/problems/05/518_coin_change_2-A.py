class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # we borrow some code from #322:

        cache = {}
        coins = tuple(sorted(coins, reverse=True))

        def coinRecursive(amount: int, coinIndex: int, depth=0) -> int:
            nonlocal cache
            margin = " " * depth
            # print(f'{margin}coinRecursive(${amount},{coinIndex})')
            key = (amount, coinIndex)
            if key in cache:
                retval = cache[key]
                # print(f'{margin} cache hit {key} -> {retval}')
                return retval
            
            if not amount:
                return 1    # there is 1 way to make $0: []
            if coinIndex >= len(coins):
                return 0    # there is no way to make change without coins
            
            coinFound = False
            while not coinFound:
                thisCoin = coins[coinIndex]
                coinIndex += 1
                if thisCoin <= amount:
                    # this coin is fine
                    coinFound = True
                elif coinIndex < len(coins):
                    # there are other coins: use those instead
                    coinFound = False
                else:
                    # no more coins, use this one anyways
                    coinFound = True
            maxCountOfThisCoin = amount // thisCoin
            # if maxCountOfThisCoin:
            #     # print(f'{margin} R({amount}): ${thisCoin} * [{maxCountOfThisCoin} .. 0]')
            # else:
            #     # print(f'{margin} R({amount}): ${thisCoin} * [0]')
            answers = []
            for count in reversed(range(maxCountOfThisCoin + 1)):
                newAmount = amount - (count * thisCoin)
                # shortcut some obvious answers rather than recusing:
                thisAnswer = (
                    1 if not newAmount
                    else
                    0 if coinIndex >= len(coins)
                    else
                    coinRecursive(newAmount, coinIndex, depth+1)
                )
                answers.append(thisAnswer)
            # print(f'{margin} {answers=}')
            retval = sum(answers)
            # print(f'{margin} cache set {key} -> {retval}')
            cache[key] = retval
            return retval

        return coinRecursive(amount, 0)

# NOTE: works for small inputs, Time Limit Exceeded for large inputs.
