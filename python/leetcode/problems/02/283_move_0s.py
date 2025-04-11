<pre>class Solution:
    def moveZeroes(self, nums: List[int]) -&gt; None:

        # we borrow some code from #26:
        L = 0
        for R, value in enumerate(nums):
            # print(f'{nums=}')
            print(f'[{L},{R}] {value}')
            if value == 0:
                print(f'  skip')
            elif L == R:
                print(f'  (same)')
                L += 1
            else:
                print(f'  COPY')
                nums[L] = value
                nums[R] = 0
                L += 1
        # print(f'{nums=}')
        &quot;&quot;&quot;
        Do not return anything, modify nums in-place instead.
        &quot;&quot;&quot;
        return

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on third Submit (edge case, Output Exceeded)
# NOTE: Runtime	51 ms Beats 13.24%
# NOTE: Memory 18.91 MB Beats 30.92%</pre>