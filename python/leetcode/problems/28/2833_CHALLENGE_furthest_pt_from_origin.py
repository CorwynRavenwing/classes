class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        # def dp_L(index: int, pos: int) -> int:
        #     pass
        
        # def dp_R(index: int, pos: int) -> int:
        #     pass
        
        # def dp(index: int, pos: int) -> int:
        #     M = moves[index]
        #     print(f'dp({index}[{M}],{pos})')

        # return dp(0, 0)

        # we could do the above, yes, but there's an easier answer:

        counts = Counter(moves)
        print(f'{counts=}')
        L = counts['L']
        R = counts['R']
        X = counts['_']

        return max(L + X - R, R + X - L)

# NOTE: Acceptance Rate 65.7% (easy)

# NOTE: Accepted on second Run (need to subtract off moves in the opposite direction)
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 3.27%
# NOTE: Memory 19.33 MB Beats 18.15%
