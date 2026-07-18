class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        # Euclidian Algorithm for GCD, as described in Wikipedia
        def GCD(A: int, B: int) -> int:
            # print(f'GCD({A},{B})')
            if B == 0:
                return A
            else:
                return GCD(B, A % B)

        prefixMax = tuple(accumulate(nums, max))
        # print(f'{prefixMax=}')

        prefixGCD = [
            GCD(N, Max)
            for N, Max in zip(nums, prefixMax)
        ]
        # print(f'raw: {prefixGCD=}')
        prefixGCD.sort()
        # print(f'sort {prefixGCD=}')

        answer = 0
        while prefixGCD:
            A = prefixGCD.pop(0)
            if not prefixGCD:
                # print(f'{A=} STOP')
                break
            B = prefixGCD.pop(-1)
            value = GCD(A, B)
            # print(f'{A=} {B=} {value=}')
            answer += value

        return answer

# NOTE: Acceptance Rate 68.7% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3622 ms Beats 5.11%
# NOTE: Runtime 3622 ms Beats 5.11%
