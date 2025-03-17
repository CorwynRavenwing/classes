class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        # we borrow some code from #3355:
 
        first = nums[0]
        last = nums[-1]
        diffs = [first] + [
            B - A
            for (A, B) in pairwise(nums)
        ] + [-last]
        # print(f'[start] {diffs=}')

        def is_zero_array(diff_array: List[int]) -> bool:
            partialSum = tuple(accumulate(diff_array))
            # print(f'    {partialSum=}')
            return (max(partialSum) <= 0)

        if is_zero_array(diffs):
            return 0
        
        answer = 0
        for (Li, Ri, Vali) in queries:
            answer += 1
            print(f'check {answer}')
            diffs[Li] -= Vali
            diffs[Ri + 1] += Vali
            if is_zero_array(diffs):
                return answer
        
        return -1

# NOTE: Acceptance Rate 38.0% (medium)o

# NOTE: time limit exceeded
