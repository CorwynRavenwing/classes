class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {
            0: 0    # it always takes 0 coins to make $0
        }
        coins.sort(reverse=True)

        def coinRecursive(amount: int, depth=0) -> int:
            nonlocal cache
            margin = " " * depth
            if amount in cache:
                retval = cache[amount]
                # print(margin + f' cache hit {amount} -> {retval}')
                return retval
            # print(margin + f'R({amount})')
            answers = []
            for C in coins:
                if C > amount:
                    # print(margin + f'  too large')
                    continue
                # print(margin + f' ${C}')
                newAmount = amount - C
                recurseCoins = coinRecursive(newAmount, depth+1)
                if recurseCoins is None:
                    # print(margin + f'  {recurseCoins=}')
                    continue
                thisAnswer = 1 + recurseCoins
                # print(margin + f' {amount}: {1}+{recurseCoins}={thisAnswer}')
                answers.append(thisAnswer)
                
            retval = min(answers) if answers else None
            # if answers:
            #     print(margin + f' {answers}: {retval}')
            cache[amount] = retval
            return retval

        answer = coinRecursive(amount)
        if answer is None:
            return -1
        else:
            return answer

# NOTE: Runtime 1095 ms Beats 20.21%
# NOTE: Memory 71.48 MB Beats 5.00%
