class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        # variable-rename "heights" to "grid"

        M = len(grid)
        N = len(grid[0])

        if M == N == 1:
            # a one-cell island can flow to both oceans
            return {(0,0)}

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

        def setValue(cell: Tuple[int,int], value: int) -> bool:
            (X, Y) = cell
            if OOB(cell):
                return False
            grid[X][Y] = value
            return True

        @cache
        def sameLevelAs(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            # print(f'SLA({cell}):')
            answer = set()
            level = getValue(cell)
            queue = {cell}
            while queue:
                C = queue.pop()
                # print(f'  {C=}')
                answer.add(C)
                for N in neighborsOf(C):
                    # print(f'    {N=}')
                    value = getValue(N)
                    if value != level:
                        # print(f'      {value}!={level}')
                        continue
                    if N not in answer:
                        queue.add(N)
                    # else:
                    #     # print(f'      (seen)')
            return answer
        # print(f'TEST: {sameLevelAs((0,0))=}')
        # print(f'TEST: {sameLevelAs((0,1))=}')
        # print(f'TEST: {sameLevelAs((2,2))=}')
        # print(f'TEST: {sameLevelAs((3,4))=}')

        @cache
        def uphillAdjacent(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            # print(f'UA({cell}):')
            level = getValue(cell)
            return {
                N
                for N in neighborsOf(cell)
                if getValue(N) > level
            }
        # print(f'TEST: {uphillAdjacent((0,0))=}')
        # print(f'TEST: {uphillAdjacent((0,1))=}')
        # print(f'TEST: {uphillAdjacent((2,2))=}')
        # print(f'TEST: {uphillAdjacent((3,4))=}')

        @cache
        def flowToCellFrom(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            # print(f'F2CF({cell}):')
            levelWith = sameLevelAs(cell)
            # print(f'  {cell}:{levelWith=}')
            uphillOf = {
                U
                for L in levelWith
                for U in uphillAdjacent(L)
            }
            # print(f'  {cell}:{uphillOf=}')
            recurse = {
                F
                for U in uphillOf
                for F in flowToCellFrom(U)
            }
            # print(f'  {cell}:{recurse=}')
            answer = levelWith | uphillOf | recurse
            # print(f'  {cell}:{answer=}')
            return answer
        # print(f'TEST: {flowToCellFrom((0,0))=}')
        # print(f'TEST: {flowToCellFrom((0,1))=}')
        # print(f'TEST: {flowToCellFrom((2,2))=}')
        # print(f'TEST: {flowToCellFrom((3,4))=}')

        # start with each border cell in the appropriate group(s):
        FlowsTo = {}
        for X in range(M):
            for Y in range(N):
                FlowsTo[(X, Y)] = set()
        # print(f'zero: {FlowsTo=}')
        for X in range(M):
            FlowsTo[(X,0)].add('P')
            FlowsTo[(X, N - 1)].add('A')
        for Y in range(N):
            FlowsTo[(0, Y)].add('P')
            FlowsTo[(M - 1, Y)].add('A')
        # print(f'init: {FlowsTo =}')
        queue = {
            cell
            for (cell, oceans) in FlowsTo.items()
            if len(oceans)
        }
        seen = set()
        # print(f'{queue=}')
        while queue:
            newQ = set()
            for Q in queue:
                if Q in seen:
                    # print(f'  {Q=} (seen)')
                    continue
                else:
                    seen.add(Q)
                oceans = FlowsTo[Q]
                print(f'  {Q=} {oceans=}')
                flowsFrom = flowToCellFrom(Q)
                # print(f'    from={flowsFrom}')
                for FF in flowsFrom:
                    FlowsTo[FF] |= oceans
                    # if FF not in seen:    # <-- actually slows the code down!
                    newQ.add(FF)
            queue = newQ
        # print(f'done: {FlowsTo =}')
        BothOceans = {
            cell
            for (cell, oceans) in FlowsTo.items()
            if len(oceans) == 2
        }
        # print(f'{BothOceans=}')

        return sorted(BothOceans)

# NOTE: Runtime 1308 ms Beats 6.88%
# NOTE: Memory 182.76 MB Beats 5.64%
