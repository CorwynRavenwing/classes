class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:

        max_score = -1
        max_divisor = None

        for D in sorted(divisors):
            print(f'{D=}')
            divisible = [
                N
                for N in nums
                if N % D == 0
            ]
            print(f'  {divisible=}')
            score = len(divisible)
            if score > max_score:
                print(f'    new max {score} {D}')
                max_score = score
                max_divisor = D
        return max_divisor

