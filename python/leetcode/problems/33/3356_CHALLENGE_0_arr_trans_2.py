class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        N = len(nums)
        Q = len(queries)
        Sum = 0
        K = 0
        diffs = [0] * (N + 1)

        # print(f'{nums=}')

        for i in range(N):
            # print(f'[{i}][{K}]: {Sum}')
            while Sum + diffs[i] < nums[i]:
                # print(f'  {diffs=}')
                # print(f'  +[{K}]: {Sum=} + {diffs[i]=} < {nums[i]=}')
                K += 1

                if K > Q:
                    return -1
                
                query = queries[K - 1]
                (Li, Ri, Vali) = query
                # print(f'  {K}: Q[{K-1}] = {query}')
                if Ri >= i:
                    diffs[max(Li, i)] += Vali
                    diffs[Ri + 1] -= Vali
                    # print(f'  {diffs=}')
                # else:
                #     # print(f'  (diffs unchanged)')
            # print(f'  =[{K}]: {Sum=} + {diffs[i]=} >= {nums[i]=}')

            Sum += diffs[i]
        
        # print(f'(done) [{i}][{K}]: {Sum}')
        return K

# NOTE: Acceptance Rate 38.0% (medium)

# NOTE: third version: Line Sweep
# NOTE: Runtime 152 ms Beats 73.48%
# NOTE: Memory 62.98 MB Beats 92.20%
