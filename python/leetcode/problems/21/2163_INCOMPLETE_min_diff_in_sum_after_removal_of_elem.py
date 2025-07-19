class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        NEG = lambda L: tuple([(None if X is None else -X) for X in L])
        REV = lambda L: tuple(reversed(L))

        # print(f'{NEG(nums)=}')
        # print(f'{REV(nums)=}')

        def sum_of_max_n_left(n: int, nums: List[int]) -> List[int]:
            answer = []
            max_n = []
            total = 0
            for val in nums:
                bisect.insort(max_n, val)
                total += val
                if len(max_n) < n:
                    answer.append(None)
                    continue
                if len(max_n) > n:
                    total -= max_n.pop(0)
                if len(max_n) == n:
                    answer.append(total)
            return answer
        
        n = len(nums) // 3
        print(f'{n=}')
        # print(f'{sum_of_max_n_left(n, nums)=}')

        prefix_sweep = NEG(sum_of_max_n_left(n, NEG(nums)))
        suffix_sweep = REV(sum_of_max_n_left(n, REV(nums)))
        
        # print(f'{prefix_sweep=}')
        # print(f'{suffix_sweep=}')

        pairs = tuple(zip(prefix_sweep, suffix_sweep[1:]))
        # print(f'{pairs=}')

        answers = [
            A - B
            for A, B in pairs
            if A is not None and B is not None
        ]
        # print(f'{answers=}')

        return min(answers)

        # From user6403Hl's suggestion:

        # two-phase heap trick:

        #     Prefix phase: Sweep from left to right, maintaining a max-heap of size n (or a min-heap storing negatives) so you always keep the smallest n elements seen so far. Record at each index i the sum of those n.

        #     Suffix phase: Sweep from right to left, maintaining a min-heap of size n so you keep the largest n elements from the tail onward. Record at each index i the sum of those n.

        # Finally, for every possible split between index i and i+1 (where the left block ends at i and the right block begins at i+1), take prefixSum[i] -  suffixSum[i+1] and choose the minimum.

        return -99999

# NOTE: Acceptance Rate 54.1% (HARD)

# NOTE: Time Limit Exceeded for large inputs
