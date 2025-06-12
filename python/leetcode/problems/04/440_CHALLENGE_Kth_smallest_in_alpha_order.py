class Solution:

    # we borrow some code from #386:

    def count_beginning_with(self, begin: int, maximum: int) -> int:
        print(f'CBW({begin},{maximum}):')
        beginDigits = len(str(begin))
        maxDigits = len(str(maximum))
        diffDigits = maxDigits - beginDigits
        endpoints = [
            (
                begin * (10 ** digits),             # 42,3 -> 42000
                (begin + 1) * (10 ** digits) - 1,   # 42,3 -> 43 -> 43000 -> 42999
            )
            for digits in range(0, diffDigits + 1)
        ]
        # print(f'CBW() {endpoints=}')
        endpoints = [
            (
                lowest,
                min(highest, maximum)
            )
            for (lowest, highest) in endpoints
        ]
        print(f'CBW() {endpoints=}')
        totals = [
            highest - lowest + 1
            for (lowest, highest) in endpoints
            if lowest <= highest
        ]
        # totals = [
        #     (
        #         highest - lowest + 1
        #         if lowest <= highest
        #         else 0
        #     )
        #     for (lowest, highest) in endpoints
        # ]
        print(f'CBW() {totals=}')
        return sum(totals)

    def findKthNumber(self, n: int, k: int) -> int:
        trial = 1
        while True:
            assert k >= 0
            if k == 1:
                return trial
            countBeginWithTrial = self.count_beginning_with(trial, n)
            if countBeginWithTrial < k:
                # remove ALL numbers beginning with "trial"
                k -= countBeginWithTrial
                trial += 1      # 2 -> 3
            else:
                # remove "trial" itself
                k -= 1
                trial *= 10     # 2 -> 20

        raise Exception('Logic error: escaped from while(True) loop')

# NOTE: About my fourth attempted algorithm.
# NOTE: Runtime 44 ms Beats 6.43%
# NOTE: Memory 16.60 MB Beats 10.29%

# NOTE: Acceptance Rate 42.3% (HARD)

# NOTE: re-ran for challenge:
# NOTE: Runtime 7 ms Beats 0.50%
# NOTE: Memory 17.72 MB Beats 64.68%
# NOTE: much better time, much worse percentage
# NOTE: same size, much better percentage
