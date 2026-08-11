class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        precomputed_squares = set()
        for i in range(1, n + 1):
            SQ = i * i
            if SQ > n:
                break
            precomputed_squares.add(SQ)
        # print(f'{precomputed_squares=}')

        @cache
        def IsWinningState(n: int) -> bool:
            print(f'IWS({n}):')
            if not n:
                print(f'  NO: zero')
                return False
            if n in precomputed_squares:
                print(f'  YES: square')
                return True
            states = [
                n - move
                for move in precomputed_squares
                if move <= n
            ]
            # print(f'IWS({n}): {states=}')
            results = [
                IsWinningState(S)
                for S in states
            ]
            # print(f'IWS({n}): {results=}')
            otherGuyAlwaysLoses = (False in results)
            print(f'IWS({n}): answer={otherGuyAlwaysLoses}')
            return otherGuyAlwaysLoses
        
        return IsWinningState(n)

# NOTE: Acceptance Rate 59.9% (HARD)

# NOTE: Accepted on third Run (infinite loop; polarity reversed)
# NOTE: Accepted on third Submit (polarity reversed again; Output Exceeded)
# NOTE: Runtime 6302 ms Beats 5.16%
# NOTE: Memory 43.29 MB Beats 28.79%
