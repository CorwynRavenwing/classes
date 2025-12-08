class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        numMods = [
            N % p
            for N in nums
        ]
        print(f'{numMods=}')
        sums = list(itertools.accumulate(nums))
        print(f'{sums=}')
        sumMods = [
            S % p
            for S in sums
        ]
        print(f'{sumMods=}')
        
        K = sumMods[-1]
        if K == 0:
            print(f'Already divisible')
            return 0
        
        if K in nums:
            print(f'Just delete the number {K}')
            return 1
        
        if K in numMods:
            index = numMods.index(K)
            print(f'Just delete the number {nums[index]} (%{p} = {K}')
            return 1
        
        ## this case is subsumed by the general case below
        # if 0 in sumMods:
        #     answer = 0
        #     SM = sumMods.copy()
        #     while SM[-1] != 0:
        #         answer += 1
        #         del SM[-1]
        #     print(f'Delete the last {answer} numbers')
        #     return answer

        sumMods_indexes = {}
        for index, SM in enumerate(sumMods):
            sumMods_indexes.setdefault(SM, [])
            sumMods_indexes[SM].append(index)
        # Also, add { 0: [-1] } to the indexes, because these numbers
        # signify "the sum of numbers up to and including index X",
        # so sumMods[0] is the sum of just index 0.  Adding this -1
        # signifies "the sum of NO numbers at all (before the array), is zero"
        # Without this, we miss finding ranges that begin at nums[0]
        sumMods_indexes.setdefault(0, [])
        sumMods_indexes[0].append(-1)
        print(f'{sumMods_indexes=}')

        answers = []
        for L, indexesL in sumMods_indexes.items():
            R = (L + K) % p
            if R in sumMods_indexes:
                indexesR = sumMods_indexes[R]
                print(f'  {L=} {indexesL=} -> {R=} {indexesR=}')
                for Li in indexesL:
                    for Ri in indexesR:
                        if Li < Ri:
                            diff = Ri - Li
                            print(f'    Try deleting {diff} [{Li + 1}..{Ri}]?')
                            if diff == len(nums):
                                print(f'      Nope, cannot delete entire array')
                                continue
                            answers.append(diff)
            # else:
            #     print(f'  {L=} {indexesL=} -> {R=} NOT FOUND')
        print(f'{answers=}')
        if answers:
            print(f'Best idea is {min(answers)}')
            return min(answers)

        print(f'Impossible')
        return -1

# NOTE: Acceptance Rate 42.6% (medium)

# NOTE: Runtime 475 ms Beats 5.06%
# NOTE: Memory 55.57 MB Beats 5.06%
