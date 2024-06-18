from collections import Counter

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        sorted_dominoes = tuple(map(tuple, map(sorted, dominoes)))
        print(f"{sorted_dominoes}")
        counted_dominoes = Counter(sorted_dominoes)
        print(f"{counted_dominoes}")
        counts = tuple(
            V
            for V in counted_dominoes.values()
            if V > 1
        )
        print(f"{counts}")

        def N_choose_2(N):
            return (N) * (N - 1) // 2

        pairs = [
            N_choose_2(N)
            for N in counts
        ]
        print(f"{pairs=}")

        return sum(pairs)

