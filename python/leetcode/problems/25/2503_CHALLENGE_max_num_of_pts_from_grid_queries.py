class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        M = len(grid)
        N = len(grid[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        directions = (
            (-1, 0),
            (+1, 0),
            (0, -1),
            (0, +1),
        )
        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            Neighbors = (
                (X + I, Y + J)
                for (I, J) in directions
            )
            return tuple([
                C
                for C in Neighbors
                if legalPos(C)
            ])

        def getValue(cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return grid[X][Y]

        queries_sorted = tuple(sorted(set(queries)))
        answer_cache = {}

        # precompute answer_cache[X] for all Q in queries_sorted:

        reachable = set()
        origin = (0, 0)
        border = {origin}
        for Q in queries_sorted:
            print(f'{Q=} {len(reachable)=} {len(border)=}:')
            queue = border
            border = set()
            while queue:
                cell = queue.pop()
                if cell in reachable:
                    # print(f'  {cell=} (seen: inside)')
                    continue
                if cell in border:
                    # print(f'  {cell=} (seen: border)')
                    continue

                value = getValue(cell)
                if value >= Q:
                    # print(f'  {cell=} {value=} outside')
                    border.add(cell)
                    continue

                # print(f'  {cell=} {value=} INSIDE')
                reachable.add(cell)
                for neighbor in neighborsOf(cell):
                    if neighbor in reachable:
                        # print(f'    {neighbor} already inside')
                        continue
                    if neighbor in border:
                        # print(f'    {neighbor} already border')
                        continue
                    if neighbor in queue:
                        # print(f'    {neighbor} already queue')
                        continue
                    queue.add(neighbor)
                    print(f'    -> {neighbor}')

            print(f'{Q=} {len(reachable)=} {len(border)=}\n')
            answer_cache[Q] = len(reachable)

        def doQuery(Q: int) -> int:
            print(f'{Q=}')
            return answer_cache[Q]

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 58.5% (HARD)

# NOTE: Accepted on second Run (needed to prime the cache)
# NOTE: Accepted on first Submit
# NOTE: Runtime 6392 ms Beats 5.23%
# NOTE: Memory 40.80 MB Beats 38.56%
