class Solution:
    def countHousePlacements(self, n: int) -> int:

        # options for, say, N=5 spots on street:
        # (A) we do not put a house here.  This gives us
        #   "options for N-1 spots"
        # (B) we DO put a house here, and then must skip the next spot.
        # This can happen "options for N-2 spots" ways
        # Therefore we are doing fibonacci.
        # base case, N=1, options = 2: "a house" or "not a house";
        # base case, N=0, options = 1, because on a 0-length street
        # there is only the one option, "0 houses"

        @cache
        def options_for_one_side(n: int) -> int:
            print(f'options({n})')
            if n == 0:
                return 1
            elif n == 1:
                return 2
            else:
                return sum([
                    options_for_one_side(n - 1),
                    options_for_one_side(n - 2),
                ])

        options = options_for_one_side(n)

        # This was all for the north side.  The south side is identical,
        # but independent, so we square the one-side answer.
        
        answer = options * options

        # ... modulo the magic number

        mod = 10 ** 9 + 7
        return answer % mod
# NOTE: Accepted on first run
# NOTE: Accepted on first submission
# NOTE: Runtime 609 ms Beats 12.68%
# NOTE: Memory 168.04 MB Beats 11.71%
