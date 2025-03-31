class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        # SHORTCUTS:
        # 1) W[0] and W[N] always appear in the score.
        # 2) Subtracting two scores, these values cancel out.
        # 3) Adding a split between a pair of marbles adds
        #    W[I] and W[I + 1] to the score.
        # 4) K bags means K - 1 splits.
        # 5) We need (sum of K-1 max splits) - (sum of K-1 min splits)

        # 6) 1 bag === only one possible score === difference zero
        if k == 1:
            return 0

        scores = tuple(sorted(map(sum, pairwise(weights))))
        print(f'{scores=}')

        cuts = k - 1

        worst = scores[:cuts]
        best = scores[-cuts:]
        print(f'{worst=}')
        print(f'{best =}')

        return sum(best) - sum(worst)

# NOTE: Acceptance Rate 66.4% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case with 1 bag)
# NOTE: Runtime 220 ms Beats 15.70%
# NOTE: Memory 31.67 MB Beats 16.12%
