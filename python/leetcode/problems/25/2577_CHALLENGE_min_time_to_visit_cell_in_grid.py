class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        
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

        origin = (0, 0)
        target = (M - 1, N - 1)

        origin_neighbors = neighborsOf(origin)
        origin_neighbor_values = [getValue(cell) for cell in origin_neighbors]
        if min(origin_neighbor_values) > 1:
            print(f'NO PATH FROM ORIGIN')
            return -1
        
        seen = set()
        queue = [(0, origin)]
        queue_set = set(queue)
        while queue:
            Q = queue.pop(0)
            (time, cell) = Q
            queue_set.remove(Q)
            if cell in seen:
                continue
            else:
                seen.add(cell)
            # print(f'{time}:{cell}')
            if cell == target:
                # print(f'  FOUND')
                return time
            for neighbor in neighborsOf(cell):
                new_time = time + 1
                if neighbor in seen:
                    continue
                value = getValue(neighbor)
                if value > new_time:
                    value_parity = (value % 2)
                    new_time_parity = (new_time % 2)
                    same_parity = (value_parity == new_time_parity)
                    new_time = value + (0 if same_parity else 1)
                # print(f'  -> {new_time}:{neighbor}')
                newQ = (new_time, neighbor)
                if newQ in queue_set:
                    continue
                # # This actually makes it slower:
                # betterQ = (new_time - 1, neighbor)
                # if betterQ in queue_set:
                #     continue
                bisect.insort(queue, newQ)
                queue_set.add(newQ)
        
        raise Exception(f'Never found the target corner!')

# NOTE: Acceptance Rate 38.5% (HARD)
# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded, Time Limit Exceeded)
# NOTE: Runtime 3970 ms Beats 5.31%
# NOTE: Memory 42.73 MB Beats 33.21%
