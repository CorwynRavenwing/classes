class Solution:
    def climbStairs(self, n: int) -> int:
        answers = {
            0: 1,
            1: 1,
        }

        for i in range(2, n+1):
            answers[i] = answers[i-1] + answers[i-2]
        
        return answers[n]

