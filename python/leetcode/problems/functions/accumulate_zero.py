
    # sums adjacent 1's; starts over at any 0's.
    # [1 1 1 0 1 1] -> [1 2 3 0 1 2]
    # do-each-row-of-matrix version.

        ACCZERO = lambda a, b: (a + 1 if b else b)
        partialSumArray = [
            tuple(accumulate(col, ACCZERO))
            for col in matrix
        ]

