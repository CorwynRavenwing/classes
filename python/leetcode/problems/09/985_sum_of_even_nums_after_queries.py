class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        is_even = [
            (N % 2 == 0)
            for N in nums
        ]
        EvenTotal = sum([
            N
            for E, N in zip(is_even, nums)
            if E
        ])
        print(f'original {EvenTotal=}')

        def doQuery(Q: List[int]) -> int:
            nonlocal EvenTotal
            nonlocal is_even
            nonlocal nums
            print(f'{Q=}')
            (valI, indexI) = Q
            if is_even[indexI]:
                EvenTotal -= nums[indexI]
            nums[indexI] += valI
            is_even[indexI] = (nums[indexI] % 2 == 0)
            # ^^^ instead, could negate is_even only if valI is odd
            if is_even[indexI]:
                EvenTotal += nums[indexI]
            return EvenTotal

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 71 ms Beats 5.26%
# NOTE: Memory 21.86 MB Beats 86.73%
