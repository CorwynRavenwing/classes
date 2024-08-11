class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        
        array_size = len(nums)

        nums.sort()
        partialSums = (0,) + tuple(accumulate(nums))
        
        def doQuery(Q: int) -> int:
            # This answer is O(#Nums * #Queries), basically O(N^2)
            # return sum([
            #     abs(Q - N)
            #     for N in nums
            # ])
            # instead, let's make this O(#Queries), approx O(N)
            Q_index = bisect_left(nums, Q)
            # print(f'{Q=} {Q_index=} {array_size=}')
            leftCount = Q_index
            leftSum = partialSums[Q_index] - partialSums[0]
            rightCount = array_size - Q_index
            rightSum = partialSums[array_size] - partialSums[Q_index]
            # print(f'   {leftCount=}  {leftSum=}')
            # print(f'  {rightCount=} {rightSum=}')

            return (
                rightSum - leftSum + Q * (leftCount - rightCount)
            )
        
        return [
            doQuery(Q)
            for Q in queries
        ]
# NOTE: Runtime 694 ms Beats 73.39%
# NOTE: Memory 43.92 MB Beats 64.00%
