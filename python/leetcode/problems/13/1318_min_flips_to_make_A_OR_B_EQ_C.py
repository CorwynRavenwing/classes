class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        maxNum = max(a, b, c)
        size = len(f'{maxNum:b}')
        
        BIN = lambda X: f'{X:0{size}b}'
        (A, B, C) = map(BIN, (a, b, c))
        print(f'{A=} {a=}')
        print(f'{B=} {b=}')
        print(f'{C=} {c=}')

        # INTS = lambda X: tuple(map(int, tuple(X)))

        translation = {
            '000': 0,
            '001': 1,
            '010': 1,
            '011': 0,
            '100': 1,
            '101': 0,
            '110': 2,
            '111': 0,
        }

        Z = [
            translation[''.join(AiBiCi)]
            for AiBiCi in zip(A, B, C)
            # for AiBiCi in zip(INTS(A), INTS(B), INTS(C))
        ]
        print(f'{Z=}')

        return sum(Z)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 26 ms Beats 95.16%
# NOTE: Memory 16.82 MB Beats 6.44%
