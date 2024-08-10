class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:

        # SHORTCUT: if you already know all powers of 2 up to 2**X
        # are in the nums array, then from them you can compose
        # any other number up to (2**(X+1)-1), e.g. 1, 2, 4 can compose
        # all numbers up to 7 but not 8.
        # Therefore we are looking for the first power of 2 that is not in nums.

        answer = 1
        print(f'{answer=}')
        while answer in nums:
            answer *= 2
            print(f'{answer=}')
        return answer
# NOTE: Runtime 417 ms Beats 5.56%
# NOTE: Memory 30.60 MB Beats 65.74%
