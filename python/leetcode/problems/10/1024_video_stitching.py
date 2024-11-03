class Solution:
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

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was TLE: added @cache)
# NOTE: Runtime 3 ms Beats 11.65%
# NOTE: Memory 17.41 MB Beats 5.29%
