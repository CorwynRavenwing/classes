class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        def Triangle(N: int) -> int:
            return (N) * (N + 1) // 2

        descents = ''.join([
            (
                'D' if (A == B + 1)
                else '.'
            )
            for (A, B) in pairwise(prices)
        ])
        print(f'{descents=}')
        
        descent_groups = descents.split('.')
        while '' in descent_groups:
            descent_groups.remove('')
        print(f'{descent_groups=}')

        lengths = tuple(map(len, descent_groups))
        print(f'{lengths=}')

        triangles = tuple(map(Triangle, lengths))
        print(f'{triangles=}')

        return len(prices) + sum(triangles)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 6175 ms Beats 5.34%
# NOTE: Memory 30.10 MB Beats 30.96%
