class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:

        values = [
            (nums[i] - nums[j]) * nums[k]
            for i in range(len(nums))
            for j in range(i+1, len(nums))
            for k in range(j+1, len(nums))
        ]
        values.append(0)    # so "all negative values" returns "0"
        print(f'{values=}')
        return max(values)

# NOTE: re-ran for challenge:
# NOTE: Runtime 156 ms Beats 29.92%
# NOTE: Memory 29.61 MB Beats 5.49%
