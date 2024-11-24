class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        def factors_of(N: int) -> List[int]:
            if N == 1:
                return [1]

            answers = []
            for D in range(1, N // 2 + 1):
                if N % D == 0:
                    Q = N // D 
                    if D > Q:
                        break
                    answers.append(D)
                    if Q != D:
                        answers.append(Q)
            return sorted(answers)

        F = factors_of(n)
        print(f'{n=} {F=}')

        try:
            return F[k - 1]
        except IndexError:
            return -1

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.64 MB Beats 41.02%
