class Solution:

    def checkAnswer(self, nums: List[int]):
        for i, A in enumerate(nums):
            for j, B in enumerate(nums):
                if not (i < j):
                    continue
                if not (A % 2) == (B % 2):
                    continue
                for k, C in enumerate(nums):
                    if not (i < k < j):
                        continue
                    if C+C == A+B:
                        print(f'ERROR: [{i},{k},{j}] ({A}+{B}=2*{C})')

    def beautifulArrangement(self, S: Set[int]) -> List[int]:
        if len(S) <= 2:
            return tuple(sorted(S))
        
        possibles = [((), S)]
        while possibles:
            (so_far, to_go) = possibles.pop()
            # print(f'({so_far},{to_go})')
            # print(f'L={len(possibles)}')
            if not to_go:
                return so_far
            for N in to_go:
                remaining = to_go - {N}
                # print(f'    {so_far} | {N} | {remaining}')
                # print(f'    {len(so_far)} | {N=} | {len(remaining)}')
                PASS_N = lambda A: max(0, 2 * N - A)
                PASS_N_SET = lambda L: set(map(PASS_N, tuple(L))) - {0}
                if so_far:
                    query = PASS_N_SET(so_far)
                    if query:
                        # print(f'    {query=}')
                        intersect = remaining & query
                        if intersect:
                            # print(f'      nope={len(intersect)}')
                            continue

                possibles.append(
                    (so_far + (N,), remaining)
                )

        return tuple([42,69,404])

    def beautifulArray(self, n: int) -> List[int]:

        # PROCESS:
        # the constraint that 2*nums[k] must not equal nums[i]+nums[j]
        # can only occur if nums[i]+nums[j] is even, which can only
        # happen when nums[i] and nums[j] are either both even or both odd.
        # Also, the nums[k] that will cause this problem will be the number
        # that is the average of nums[i] and nums[j]: that is, the number
        # halfway between them (i.e. halfway between odd numbers 3 and 7
        # is the number 5)
        # Therefore, any permutation of [1,n] with all the odd numbers
        # together and all the even numbers together, ordered such that
        # the central number avg(i,j) (as above) is either before or after
        # nums[i] and nums[j], not between them, is a beautiful array.

        # 8:
        # 2-even or 2-odd pairs that have an even or odd average:
        # 1,5: 3    2,6: 4
        # 3,7: 5    4,8: 6
        # 5, 1, 7, 3, 6, 2, 8, 4

        nums = set(range(1, n+1))

        even = {N for N in nums if N % 2 == 0}
        odds = {N for N in nums if N % 2 == 1}

        answer = self.beautifulArrangement(odds) + self.beautifulArrangement(even)
        self.checkAnswer(answer)
        return answer

# NOTE: Time Limit Exceeded for large n (>= 93)
