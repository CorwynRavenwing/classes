class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        counts = Counter(nums)
        while True:
            maxNum = max(counts)
            maxCount = counts[maxNum]
            if k <= maxCount:
                print(f'Found {maxNum} ({k} <= {maxCount})')
                return maxNum
            else:
                print(f'  Skip {maxNum} ({k} > {maxCount})')
                k -= maxCount
                del counts[maxNum]
        
        raise Exception('Logic error: escaped from infinite loop!')

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 9704 ms Beats 5.00%
# NOTE: Memory 30.09 MB Beats 16.09%
