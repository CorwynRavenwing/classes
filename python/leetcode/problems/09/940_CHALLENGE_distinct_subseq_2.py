class Solution:
    def distinctSubseqII(self, s: str) -> int:
        
        # as we parse S, think about all strings
        # that do contain this new character.
        # we get their count.

        # total strings (the answer) is the *sum*
        # of all such counts.

        # have we seen this char before?

        # if no, this partial count is:
        # (prior sum of all counts)
        #   [add this character to the end of all other strings]
        # + 1
        #   [just this character by itself]

        # if yes, do the previous, but then subtract off
        # one copy of the count from each time we saw this char.

        mod = 10 ** 9 + 7

        partial_sums_by_letter = Counter()
        this_partial = 0
        prior_sum = 0

        for L in s:
            print(f'{L=}')
            last_seen = partial_sums_by_letter[L]
            print(f'  {last_seen=}')
            this_partial = prior_sum + 1 - last_seen
            print(f'  {this_partial=}')
            partial_sums_by_letter[L] += this_partial
            print(f'  (store partial {L})')
            prior_sum += this_partial
            prior_sum %= mod
        
        return prior_sum

# NOTE: Acceptance Rate 44.8% (HARD)

# NOTE: Accepted on second Run (needed to subtract *all* prior matches)
# NOTE: Accepted on first Submit
# NOTE: Runtime 75 ms Beats 8.85%
# NOTE: Memory 19.36 MB Beats 46.35%
