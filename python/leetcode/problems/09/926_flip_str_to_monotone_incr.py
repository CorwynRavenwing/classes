class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        REV = lambda x: tuple(reversed(tuple(x)))
        ACC = lambda x: (0,) + tuple(accumulate(tuple(x)))

        zeros = [
            (1 if c == '0' else 0)
            for c in s
        ]
        ones = [
            (1 if c == '1' else 0)
            for c in s
        ]
        zerosFromRight = REV(ACC(REV(zeros)))
        onesFromLeft = ACC(ones)
        totals = tuple(map(sum, zip(zerosFromRight, onesFromLeft)))
        return min(totals)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 166 ms Beats 44.42%
# NOTE: O(N)
# NOTE: Memory 30.59 MB Beats 14.14%
# NOTE: O(N)
