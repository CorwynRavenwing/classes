class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # Euclidian Algorithm for GCD, as described in Wikipedia
        @cache
        def GCD(A: int, B: int) -> int:
            # print(f'GCD({A},{B})')
            if B == 0:
                return A
            else:
                return GCD(B, A % B)
        
        def GCD_List(L: List[int]) -> int:
            LEN = len(L)
            if LEN == 0:
                return 1
            elif LEN == 1:
                return L[0]
            elif LEN == 2:
                return GCD(*L)
            else:
                return GCD(
                    L[0],
                    GCD_List(L[1:])
                )

        if 1 in nums:
            counts = Counter(nums)
            ones = counts[1]
            return len(nums) - ones
        
        for a, b in zip(nums, nums[1:]):
            answer = GCD(a,b)
            print(f'{a=} {b=} GCD={answer}')
            if answer == 1:
                return len(nums)

        min_length = None
        for i in range(len(nums)):
            for j in range(i + 2, len(nums)):
                length = j - i + 1
                frag = nums[i:j+1]
                answer = GCD_List(frag)
                print(f'[{i}..{j}] {length} {frag} GCD={answer}')
                if answer == 1:
                    if min_length is None or min_length > length:
                        min_length = length
                        # keep track of i and j here?
                    break
        print(f'{min_length=}')
        if min_length is None:
            return -1
        
        return (min_length - 1) + (len(nums) - 1)
# NOTE: Runtime 57 ms Beats 5.26%
# NOTE: Memory 16.88 MB Beats 7.89%
