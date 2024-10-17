class Solution:
    def numTilings(self, n: int) -> int:
        
        mod = 10 ** 9 + 7

        # PROCESS:
        # we are dividing up the space by vertical breaks, at which we
        # can separate the question into smaller sub-questions.

        # (A) beginning and ending (0 and N) are vertical break,
        # but we can't divide the field there.

        # (B) If a domino is placed vertically at a break, there
        # is ONE way to do this, and it produces a new break at position 1.

        # (C) If a domino is placed horizontally at a break, there
        # is ONE way to do this, we MUST place a second horizontal domino
        # below it, and it produces a new break at position 2.

        # (D) If a Tromino is placed at a break, there are TWO ways
        # to do this; a second Tromino MUST be placed somewhere after it,
        # creating a new break at position (3+X), where X is the number
        # of dominos we choose to place between the two Trominos,
        # and (having chosen X) there is ONE way of putting the final
        # Tromino and ONE way of putting each domino.

        # Let's define ID[N] as the count of INDIVISBLE tilings of length N,
        # that is, tilings without a break.
        # ID[1] = 1     one vertical domino
        # ID[2] = 1     two horizontal dominos
        # ID[3] = 2     two adjacent Trominos, either way up
        # ID[N] = 2     two adjacent Trominos, either way up,
        #               connected by N-3 horizontal dominos

        # THEREFORE, DP[N] === ID[X1] + ID[X2] + ID[X3] + ... where sum(Xi) == N
        # but since DP[P] also equals a sum of ID[Xi] for sum(Xi) == P,
        # that means:
        # DP[N] = sum(ID[K] * DP[N-K]) for all K in [1 .. N]
        # DP[N] = (ID[1] * DP[N-1])
        #       + (ID[2] * DP[N-2])
        #    + sum(ID[K] * DP[N-K]) for K in [3 .. N]
        # but since ID[1] == ID[2] == 1 and ID[K] == 2 for K >= 3,
        # DP[N] = (1 * DP[N-1])
        #       + (1 * DP[N-2])
        #    + sum(2 * DP[N-K]) for K in [3 .. N]
        # ... after which we don't need ID[X] anymore.
        # DP[N] = DP[N-1]
        #       + DP[N-2]
        # + 2*sum(DP[N-K]) for K in [3 .. N]
        # so, if we keep a running total ACC[A] == sum(DP[B]) for B in [0..A],
        # DP[N] = DP[N-1]
        #       + DP[N-2]
        #  + 2 * ACC[N-3]
        # ( N-3 because "N-K for K in [3..N]" === [N-3 .. N-N] === [0..N-3] )
        # We count ACC[0] as "1" because it's entirely possible that the block
        # we are adding is the *only* block, and that the break we are creating
        # is at zero. This happens when K == N.

        ACC = [1] + [None] * (n + 1)
        DP = [0] + [None] * (n + 1)
        i = 0
        print(f'{i=} {DP[i]=} {ACC[i]=}')
        for i in range(1, n + 1):
            if i == 1:
                DP[i] = 1
            elif i == 2:
                DP[i] = 1 + DP[i - 1]
            else:
                DP[i] = DP[i - 1] + DP[i - 2] + 2 * ACC[i-3]

            DP[i] %= mod
            ACC[i] = DP[i] + ACC[i - 1]
            ACC[i] %= mod
            print(f'{i=} {DP[i]=} {ACC[i]=}')

        return DP[n] % mod

# NOTE: Accepted on first Submit
# NOTE: Runtime 44 ms Beats 23.28%
# NOTE: Memory 16.84 MB Beats 25.40%
