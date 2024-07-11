class Solution:
    def numSub(self, s: str) -> int:

        groups = s.split('0')
        print(f'{groups=}')
        lengths = [len(G) for G in groups]
        print(f'{lengths=}')
        counts = Counter(lengths)
        print(f'{counts=}')
        answer = 0
        mod = 10 ** 9 + 7
        for N, count in counts.items():
            # each group of N 1's adds a triangle-number to the answer
            # 1, 3, 6, 10, 15, ...
            # = (N)(N+1)/2
            # and we have 'count' of them:
            triangle = N * (N + 1) // 2
            print(f'{count=} {N=} {triangle=}')
            answer += count * triangle
            print(f'  +{answer=}')
            answer %= mod
            print(f'  %{answer=}')
        return answer
# NOTE: 47 ms; Beats 81.88%
