class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        # PROCESS:
        # We start doing a sliding window of varying length.
        # If the number of distinct elements in the window is
        # less than that of the entire array, we expand right.
        # If the number is equal to the entire array, we add
        # (number of elements from R to end-of-array inclusive)
        # to the answer, and start over with L being one further
        # to the right.
        # If we are expanding R to the right and reach the end
        # of the array, we STOP because no other, smaller window
        # will succeed either.
        target = len(Counter(nums))
        LEN = len(nums)
        answer = 0
        L = 0
        R = 0
        count = Counter()
        count[nums[R]] += 1
        while 0 <= L <= R <= LEN:
            # print(f'[{L}..{R}]: {answer=} {count=}')
            if len(count) == target:
                answer += LEN - R
                L += 1
                R = L
                count = Counter()   # clear prior window's data
            else:
                R += 1
            
            try:
                count[nums[R]] += 1
            except IndexError:
                break

        return answer

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 55 ms Beats 99.23%
# NOTE: Memory 16.80 MB Beats 71.58%

# NOTE: re-ran for challenge:
# NOTE: Runtime 60 ms Beats 33.08%
# NOTE: Memory 18.04 MB Beats 47.22%
