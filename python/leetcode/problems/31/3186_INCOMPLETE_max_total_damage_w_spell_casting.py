class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        # we borrow some code from #3180:
        # ... and it times out.
        # we borrow code from #3181 instead:

        power.sort()    # but don't make it unique using set() this time
        print(f'{len(power)=}')

        # set up bitstrings:

        BIT = lambda x: x.bit_length() - 1

        dp_current = 1        # bit #0 is set (zero points)

        dp_miss_data = []
        # contains a list of Tuple[int.int]:
        # [0] the numbers N, N+1, and N+2 which we need to miss
        # [1] the bitstrings matching those numbers
        # MISS = lambda x: (x[0], BIT(x[1]))
        MISS = lambda x: x[0]
        SHOW_MISS = lambda: print(f'miss_data = {tuple(map(MISS, dp_miss_data))}')

        for i, N in enumerate(power):
            # print(f'{i=} {N=} {BIT(dp_current)=}')
            print(f'{i=} {N=}')
            while dp_miss_data and dp_miss_data[0][0] < N - 2:
                # (old_N, old_D) = dp_miss_data.pop(0)
                (old_N, old_D) = dp_miss_data[0]
                dp_miss_data = dp_miss_data[1:]
                # print(f'  Merge data from {old_N=} < {N-2=}')
                dp_current |= old_D
                # print(f'    {BIT(dp_current)=}')
            if dp_miss_data and N == dp_miss_data[-1][0]:
                # we've seen this N before, which must have been at index -1
                miss_dp = dp_miss_data[-1][1]
                # add another copy of N to the "miss N" data
                dp_miss_data[-1] = (
                    N,
                    miss_dp << N
                )
            else:
                # new N we've never seen before
                dp_miss_data.append(
                    # add N to prior data, label it "miss N"
                    (
                        N,
                        dp_current << N
                    )
                )
            # print(f'  {BIT(dp_current)=}')
            # SHOW_MISS()

        while dp_miss_data:
            # (old_N, old_D) = dp_miss_data.pop(0)
            (old_N, old_D) = dp_miss_data[0]
            dp_miss_data = dp_miss_data[1:]
            # print(f'  Merge data from {old_N=} (done)')
            dp_current |= old_D

        # print(f'{dp_current=}')
        # ValueError: Exceeds the limit (4300 digits) for integer string conversion
        # print(f'{dp_current:b}')
        # Strangely, this succeeds, but is just an incomprehensible wall of 1's
        print(f'{BIT(dp_current)=}')
        
        return BIT(dp_current)



        return -99999

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

# NOTE: Timeout on large inputs
