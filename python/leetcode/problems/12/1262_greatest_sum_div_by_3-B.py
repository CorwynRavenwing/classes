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

        def GSD3_three_1(index1: int, index2: int) -> int:
            # take groups of 3 with mod 1:
            answer = 0
            for i in [1]:
                if index1 >= 3:
                    answer += sum(nums_by_mod3[i][index1 - 3:index1])
                    index1 -= 3
            
            if not answer:
                return 0
            else:
                return answer + GSD3(index1, index2)

        def GSD3_three_2(index1: int, index2: int) -> int:
            # take groups of 3 with mod 2:
            answer = 0
            for i in [2]:
                if index2 >= 3:
                    answer += sum(nums_by_mod3[i][index2 - 3:index2])
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
        
        index1 = len(nums_by_mod3[1])
        index2 = len(nums_by_mod3[2])

        return answer + GSD3(index1, index2)

# NOTE: version 2, also a memory limit exceeded for large inputs
