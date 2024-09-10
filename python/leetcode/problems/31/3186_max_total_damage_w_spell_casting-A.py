class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        # we borrow some code from #3180:

        power.sort()    # but don't make it unique using set() this time

        GT_N = lambda y: y >= N
        FILTER_GT_N = lambda x: frozenset(filter(GT_N, x))

        possibles = {(0, frozenset())}     # choose nothing, no recent casting powers to miss
        print(f'^ {max(possibles)=}')
        for N in power:
            new_possibles = set()
            for (P, prev_powers) in possibles:
                clean_powers = FILTER_GT_N(prev_powers)
                new_possibles.add(
                    (
                        P,
                        frozenset(clean_powers)
                    )
                )
                if N not in prev_powers:
                    new_possibles.add(
                        (
                            P + N,
                            frozenset(clean_powers | {N + 1, N + 2})
                        )
                    )
            possibles = new_possibles
            print(f'{N} {max(possibles)=}')

        (answer, recent_casts) = max(possibles)
        return answer

# NOTE: Timeout for large inputs.
