class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # given Hint 1, "ignore that crap about collisions, pretend they're ghosts":
        timeLeft = max(left, default=0)
        timeRight = n - min(right, default=n)
        return max(timeLeft, timeRight)

