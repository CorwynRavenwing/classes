class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2:
            # "low is odd" -> "lower by 1" won't change the odd count
            low -= 1
        if high % 2:
            # "high is odd" -> "raise by 1" won't change the odd count
            high += 1
        # now, all of "low", "high", and "high - low" must be even
        return (high - low) // 2

