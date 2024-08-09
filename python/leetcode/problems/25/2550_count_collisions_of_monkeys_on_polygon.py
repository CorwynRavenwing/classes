class Solution:
    def monkeyMove(self, n: int) -> int:

        mod = 10 ** 9 + 7

        def power_mod(base: int, power: int) -> int:
            print(f'power_mod({base},{power}):')
            if power > 10:
                # A^((B*C) + D) == A^(B*C) * A^D == (A^B)^C * A^D
                A = base
                B = 10
                C = power // 10
                D = power % 10
                print(f'  {A=} {B=} {C=} {D=}')
                AtoB = power_mod(A, B)
                AtoBC = power_mod(AtoB, C)
                AtoD = power_mod(A, D)
                answer = AtoBC * AtoD
                print(f'  A^B={AtoB}, ^C={AtoBC}, A^D={AtoD}')
                return answer % mod
            else:
                print(f'  simple')
                return (base ** power) % mod

        # SHORTCUT:
        # the number of ways the monkeys can move AT ALL is:
        #   each monkey chooses one of (clockwise, anticlockwise)
        #   therefore the grand total of possible moves is:
        #   2 ** (number of monkeys) === 2 ** n
        # monkeyMoves = 2 ** n      # times out for huge N
        monkeyMoves = power_mod(2, n)

        # the number of ways the monkeys can move WITHOUT colliding is:
        # 1: they all move clockwise
        # 2: they all move anticlockwise
        # therefore that number is exactly 2.
        monkeyNonCollides = 2

        # this leaves the MOVE WITH COLLIDING count as (2 ** n) - 2
        monkeyCollides = monkeyMoves - monkeyNonCollides

        # yes, this could easily be a one-liner:
        # return ((2 ** n) - 2) % (10 ** 9 + 7)
        # but "2 ** n" times out for ludicrously large values of "n"
        return monkeyCollides % mod
# NOTE: Runtime 39 ms Beats 30.09%
# NOTE: Memory 16.68 MB Beats 11.57%
