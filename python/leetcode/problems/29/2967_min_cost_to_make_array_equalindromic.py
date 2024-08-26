class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        nums.sort()
        count = len(nums)
        evenCount = (count % 2 == 0)
        if evenCount:
            center = count // 2
            print(f'DEBUG: sum({nums[center - 1:center + 1]}) / {2}')
            median = sum(nums[center - 1:center + 1]) / 2
            print(f'  {median=}')
        else:
            center = count // 2
            median = nums[center]
            print(f'  {median=}')
        # might do something with median to save time

        REV = lambda x: tuple(reversed(tuple(x)))
        REVSTR = lambda x: ''.join(REV(x))

        def allPalindromesAfter(N: int) -> List[int]:
            if N < 10:
                for X in range(N, 10):
                    yield X
                N = 10
            nStr = str(N)
            nLen = len(nStr)
            even = (nLen % 2 == 0)
            halfL = nLen // 2 + (0 if even else 1)
            firstHalf = nStr[:halfL]
            baseHalf = int(firstHalf)
            while True:
                if even:
                    nStr = firstHalf + REVSTR(firstHalf)
                else:
                    nStr = firstHalf + REVSTR(firstHalf[:-1])
                yield int(nStr)
                baseHalf += 1
                firstHalf = str(baseHalf)
                if len(firstHalf) > halfL:
                    if even:
                        even = False
                        halfL = len(firstHalf)
                    else:
                        even = True
                        firstHalf = firstHalf[:-1]
                        # 999xx -> 1000xx -> 100xxx
                        halfL = len(firstHalf)
                        baseHalf = int(firstHalf)

        def score(X: int) -> int:
            return sum([
                abs(N - X)
                for N in nums
            ])
        
        median_minus_a_bit = int(median * 99 // 100)
        median_plus_a_bit = int(median * 101 // 100)

        N = median_minus_a_bit
        # print(f'{N=}')
        answers = []
        for X in allPalindromesAfter(N):
            # print(f'{X}')
            S = score(X)
            # print(f'  {S}')
            answers.append(S)
            if X > median_plus_a_bit:
                # print(f'  > max')
                break
        return min(answers)

# NOTE: Runtime 5827 ms Beats 5.74%
# NOTE: Memory 30.14 MB Beats 72.95%
