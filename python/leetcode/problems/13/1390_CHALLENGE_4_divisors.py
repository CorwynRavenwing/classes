class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def divisorsOf(N: int) -> List[int]:
            answers = []
            for D in range(1, int(sqrt(N)) + 1):
                if N % D == 0:
                    Q = N // D
                    # print(f'{N} / {D} = {Q}')
                    answers.append(D)
                    if D != Q:
                        answers.append(Q)
            return sorted(answers)
        
        answer = 0
        for N in nums:
            DN = divisorsOf(N)
            print(f'{N} -> {DN} ({len(DN)})')
            if len(DN) == 4:
                answer += sum(DN)

        return answer

# NOTE: Acceptance Rate 46.4% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 475 ms Beats 11.15%
# NOTE: Memory 18.68 MB Beats 87.80%
