class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        # NOTE: because we're looking for the *minimum*
        #   difference, any correct answer will be
        #   adjacent values (after sorting), because any
        #   non-adjacent values will have a larger difference
        #   than the diff from each endpoint to the skipped value.

        arr.sort()
        pairs = tuple(pairwise(arr))
        print(f'{pairs=}')
        diffs = tuple([(B - A) for (A, B) in pairs])
        print(f'{diffs=}')
        min_diff = min(diffs)
        print(f'{min_diff=}')
        
        matches = [
            pair
            for (diff, pair) in zip(diffs, pairs)
            if diff == min_diff
        ]

        return matches

# NOTE: Acceptance Rate 71.6% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 99 ms Beats 8.64%
# NOTE: Memory 41.12 MB Beats 5.32%
