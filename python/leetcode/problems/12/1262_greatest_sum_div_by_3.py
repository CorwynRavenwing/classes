class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        nums_by_mod3 = {}
        for i in range(3):
            nums_by_mod3[i] = []
        for N in nums:
            i = N % 3
            nums_by_mod3[i].append(N)
        for i in range(3):
            nums_by_mod3[i].sort()
        print(f'initial: {nums_by_mod3=}')

        # take all values with mod 0:
        answer = sum(nums_by_mod3[0])
        del nums_by_mod3[0]

        index1 = len(nums_by_mod3[1])
        index2 = len(nums_by_mod3[2])

        # SHORTCUT: we can safely take almost all the possible moves,
        # since it's only the last few moves (if the indexes are at
        # either "three + one" or "three + two", which we might want
        # to take as a three, or as either one or two pairs)
        # that actually require a decision to be made.

        while index1 > 6:
            # take groups of 3 with mod 1:
            # stop when there's at most 2 groups left
            answer += sum(nums_by_mod3[1][index1 - 3:index1])
            index1 -= 3

        while index2 > 6:
            # take groups of 3 with mod 2:
            # stop when there's at most 2 groups left
            if index2 >= 3:
                answer += sum(nums_by_mod3[2][index2 - 3:index2])
                index2 -= 3

        def GSD3_three_1(index1: int, index2: int) -> int:
            # take groups of 3 with mod 1:
            answer = 0
            if index1 >= 3:
                answer += sum(nums_by_mod3[1][index1 - 3:index1])
                index1 -= 3
            
            if not answer:
                return 0
            else:
                return answer + GSD3(index1, index2)

        def GSD3_three_2(index1: int, index2: int) -> int:
            # take groups of 3 with mod 2:
            answer = 0
            if index2 >= 3:
                answer += sum(nums_by_mod3[2][index2 - 3:index2])
                index2 -= 3
            
            if not answer:
                return 0
            else:
                return answer + GSD3(index1, index2)

        def GSD3_pair(index1: int, index2: int) -> int:
            # take pairs from mod=1 and mod=2 together:
            answer = 0
            if index1 and index2:
                answer += nums_by_mod3[1][index1 - 1]
                answer += nums_by_mod3[2][index2 - 1]
                index1 -= 1
                index2 -= 1

            if not answer:
                return 0
            else:
                return answer + GSD3(index1, index2)

        @cache
        def GSD3(index1: int, index2: int) -> int:
            return max([
                GSD3_three_1(index1, index2),
                GSD3_three_2(index1, index2),
                GSD3_pair(index1, index2),
            ])
        
        return answer + GSD3(index1, index2)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Time Limit Exceeded)
# NOTE: Runtime 41 ms Beats 61.85%
# NOTE: Memory 25.14 MB Beats 24.02%
