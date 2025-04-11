<pre>class Solution:
    def removeDuplicates(self, nums: List[int]) -&gt; int:
        
        L = 0
        prev_value = None
        for R, value in enumerate(nums):
            print(f'[{L},{R}] {value}')
            if prev_value is None:
                print(f'  first')
                prev_value = value
                L += 1
                continue
            elif prev_value == value:
                print(f'  skip')
                continue
            else:
                print(f'  COPY')
                nums[L] = value
                L += 1
                prev_value = value
        return L

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 30 ms Beats 11.36%
# NOTE: Memory 19.30 MB Beats 8.98%</pre>