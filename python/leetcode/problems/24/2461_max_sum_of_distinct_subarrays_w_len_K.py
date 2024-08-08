class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        def noDups(counts: Counter) -> bool:
            # return max(counts.values()) > 1
            # return any([
            #     count > 1
            #     for count in counts.values()
            # ])
            # suggested by someone in the comments
            return len(counts.values()) == k
        
        subarray = nums[:k]
        subarray_sum = sum(subarray)
        subarray_counts = Counter(subarray)
        answer = 0
        for i in range(k, len(nums) + 1):
            # subarray === the K numbers left of i: [i-k:i]
            # print(f'{i=} {subarray_sum=} counts={Counter(subarray_counts.values())}')
            if noDups(subarray_counts):
                answer = max(answer, subarray_sum)
            ToDelete = nums[i - k]
            if i >= len(nums):
                break
            ToAdd = nums[i]
            subarray_sum -= ToDelete
            subarray_sum += ToAdd
            subarray_counts[ToDelete] -= 1
            subarray_counts[ToAdd] += 1
            if not subarray_counts[ToDelete]:
                del subarray_counts[ToDelete]
        return answer
# NOTE: Runtime 652 ms Beats 11.43%
# NOTE: Memory 34.65 MB Beats 29.73%
