class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return (len(s) == len(goal)) and (s in (goal + goal))

# NOTE: ONE LINE ANSWER, but still understandable.
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: O(N)
# NOTE: Memory 16.67 MB Beats 9.22%
# NOTE: O(N)
