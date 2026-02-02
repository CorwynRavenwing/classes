class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        
        def min_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return min(L, default=None)

        n = len(nums)
        def DP(startIndex: int, K: int) -> int:
            print(f'DP({startIndex},{K})')
            if K == 0:
                print(f'  K==0 -> None')
                return None
            if K == 1:
                if (n - 1) - startIndex > dist:
                    print(f'  K==1, too big -> None')
                    return None
                print(f'  K==1 -> nums[i]')
                try:
                    return nums[startIndex]
                except IndexError:
                    print(f'    OOB -> None')
                    return None

            answers = [
                DP(nextStart, K-1)
                for nextStart in range(startIndex + 1, startIndex + dist)
            ]
            print(f'DP({startIndex},{K}) {answers=}')
            answer = min_not_none(answers)
            print(f'DP({startIndex},{K}) nums[i] + {answer}')
            if answer is None:
                return None
            return nums[startIndex] + answer

        return DP(0, k)

# NOTE: Acceptance Rate 31.5% (HARD)

# NOTE: wrong answer
