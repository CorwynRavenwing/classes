class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:

        nums.sort()

        index = len(nums) // 2
        quote_median_unquote = nums[index]
        print(f'[{index=}] {quote_median_unquote=}')

        if quote_median_unquote == k:
            print(f'"median" == k')
            return 0
        elif quote_median_unquote > k:
            print(f'"median" > k')
            answer = [
                N - k
                for N in nums[:index+1]
                if N > k
            ]
        elif quote_median_unquote < k:
            print(f'"median" < k')
            answer = [
                k - N
                for N in nums[index:]
                if N < k
            ]
        else:
            raise Exception(f'error, cannot compare {quote_median_unquote=} <=> {k=}')
        
        print(f'{answer=}')
        return sum(answer)

# NOTE: Accepted on first Run; Accepted on first Submit
# NOTE: Runtime 621 ms Beats 76.67%
# NOTE: Memory 38.12 MB Beats 10.00%
