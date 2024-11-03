class Solution:

    # we borrow some code from #1024:

    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        # sort intervals by end time, backwards:
        clips.sort(
            key=lambda x: x[1],
            reverse=True
        )

        INF = float('+inf')
        @cache
        def DP(index: int, limit: int) -> int:
            if limit <= 0:
                return 0
            try:
                (start, end) = clips[index]
            except IndexError:
                return INF
            if end < limit:
                return INF
            
            dont_take = DP(index + 1, limit)
            if start > limit:
                return dont_take

            take_this = 1 + DP(index + 1, start)
            return min(take_this, dont_take)

        answer = DP(0, time)

        return (
            -1
            if (answer == INF)
            else answer
        )

    def minTaps(self, n: int, ranges: List[int]) -> int:
        # same question with different variable names
        actual_ranges = [
            (index - width, index + width)
            for index, width in enumerate(ranges)
        ]
        return self.videoStitching(actual_ranges, n)

# NOTE: Acceptance Rate 50.7% (HARD)
# NOTE: re-used entire prior version, with wrapper code added
# NOTE: Accepted on second Run (first needed variable translation)
# NOTE: Accepted on first Submit
# NOTE: Runtime 996 ms Beats 5.69%
# NOTE: Memory 328.28 MB Beats 5.14%
