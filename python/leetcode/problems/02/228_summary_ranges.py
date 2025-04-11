<pre>class Solution:
    def summaryRanges(self, nums: List[int]) -&gt; List[str]:
        
        ranges = []
        this_range = None
        for N in nums:
            if this_range is None:
                this_range = [N, N]
            elif this_range[1] + 1 == N:
                # N is part of current range
                this_range[1] += 1
            else:
                ranges.append(this_range)
                this_range = [N, N]
            print(f'{N}: {this_range}')
        if this_range is None:
            return []
        ranges.append(this_range)
        print(f'{ranges=}')

        answer = [
            (
                f'{A}'
                if A == B
                else
                f'{A}-&gt;{B}'
            )
            for A, B in ranges
        ]
        return answer

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on second Submit (edge case with no values)
# NOTE: Runtime	0 ms Beats 100.00%
# NOTE: Memory 17.93 MB Beats 12.42%</pre>