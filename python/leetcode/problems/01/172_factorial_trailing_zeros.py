class Solution:
    def trailingZeroes(self, n: int) -> int:

        # shortcut 1:
        # "zeros in N!" === "count of multiples of 10"
        #    + min(
        #       "count multiples of 2 (but not 10)",
        #       "count multiples of 5 (but not 10)"
        #    )

        # shortcut 2:
        # there are always more multiples of 2 than of 5 in this range,
        # so the "2" clause of that min disappears
        
        # shortcut 3:
        # "multiples of 10" + "multiples of 5 but not 10" === "all multiples of 5"
        
        # shortcut 4:
        # "count multiples of 5 in (1 .. N)" == "N // 5"
        # + N // 5^2 + N // 5^3 ... etc.

        # shortcut 5:
        # "N // 5^2" == "(N // 5) // 5", etc.

        answer = []
        powers = n
        while powers > 0:
            powers = powers // 5
            answer.append(powers)
        return sum(answer)

# NOTE: 28 ms; Beats 94.32% of users with Python3
