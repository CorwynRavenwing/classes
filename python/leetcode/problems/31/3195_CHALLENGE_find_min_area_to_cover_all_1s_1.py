class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        INV = lambda G: tuple(zip(*G))
        # print(f'{INV(grid)=}')

        SUM = lambda G: tuple(map(sum, G))
        # print(f'{SUM(grid)=}')
        # print(f'{SUM(INV(grid))=}')

        NZ_raw = lambda L: [
            (
                index
                if value > 0
                else None
            )
            for index, value in enumerate(L)
        ]
        NZ = lambda L: [
            value
            for value in NZ_raw(L)
            if value is not None
        ]
        # print(f'{NZ(SUM(grid))=}')
        # print(f'{NZ(SUM(INV(grid)))=}')

        WIDTH = lambda L: (1 + max(L) - min(L))
        # print(f'{WIDTH(NZ(SUM(grid)))=}')
        # print(f'{WIDTH(NZ(SUM(INV(grid))))=}')

        width = WIDTH(NZ(SUM(grid)))
        height = WIDTH(NZ(SUM(INV(grid))))

        return width * height

# NOTE: Acceptance Rate 70.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 2556 ms Beats 97.12%
# NOTE: Memory 47.66 MB Beats 46.76%
