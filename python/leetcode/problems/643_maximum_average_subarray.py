class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        print(f"first group: {nums[:k]}")
        S = sum(nums[:k])
        max_sum = S
        for i in range(k, len(nums)):
            print(f"subtract n[{i - k}] {nums[i - k]}, add n[{i}] {nums[i]}")
            S += nums[i] - nums[i - k]
            if max_sum is None or max_sum < S:
                max_sum = S
        return max_sum / k

