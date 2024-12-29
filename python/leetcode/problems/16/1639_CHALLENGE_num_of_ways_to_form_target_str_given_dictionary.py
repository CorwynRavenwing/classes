class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        mod = 10 ** 9 + 7

        counters = [
            Counter(letters)
            for letters in zip(*words)
        ]
        # print(f'{counters=}')

        def DP_skip(target_index, counters_index) -> int:
            return DP(target_index, counters_index + 1)
        
        def DP_take(target_index, counters_index) -> int:
            target_letter = target[target_index]
            counter = counters[counters_index]
            count = counter[target_letter]
            if not count:
                # print(f'  Cannot take: count[{target_letter}] == {count}')
                return 0
            remainder = DP(target_index + 1, counters_index + 1)
            return count * remainder
        
        @cache
        def DP(target_index, counters_index) -> int:
            # print(f'DP({target_index}, {counters_index})')
            try:
                check1 = target[target_index]
            except IndexError:
                # ran out of Target: 1 way to match string "" using no counters
                return 1
            try:
                check2 = counters[counters_index]
            except IndexError:
                # ran out of Counters: no way to match any string
                return 0
            return sum([
                DP_skip(target_index, counters_index),
                DP_take(target_index, counters_index),
            ])
        
        answer = DP(0, 0)

        return answer % mod

# NOTE: Acceptance Rate 52.3% (HARD)
# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded twice)
# NOTE: Runtime 2033 ms Beats 17.48%
# NOTE: Memory 192.00 MB Beats 29.60%
