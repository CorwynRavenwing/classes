class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        adjacent = {}
        for i in range(n):
            adjacent.setdefault((i, 'R'), set())
            adjacent.setdefault((i, 'B'), set())
        
        for Ai, Bi in redEdges:
            adjacent[(Ai, 'B')].add((Bi, 'R'))

        for Ai, Bi in blueEdges:
            adjacent[(Ai, 'R')].add((Bi, 'B'))

        # print(f'{adjacent=}')
        print(f'adjacent=')
        for node, neighbors in sorted(adjacent.items()):
            print(f'  {node}: {neighbors}')

        nodeDistance = {}

        def setDistances(nodes: List[int], distance: int):
            print(f'SD({nodes},{distance})')
            if not nodes:
                return
            
            next_nodes = set()
            for node in nodes:
                if node in nodeDistance:
                    continue
                else:
                    nodeDistance[node] = distance
                    next_nodes |= adjacent[node]
            
            setDistances(
                tuple(next_nodes),
                distance + 1
            )

            return

        zeroNodes = {(0, 'R'), (0, 'B')}
        setDistances(tuple(zeroNodes), 0)
        print(f'{nodeDistance=}')

        INF = 10 ** 5

        answers = [
            [
                (nodeDistance[(node, color)]
                if (node, color) in nodeDistance
                else INF
                )
                for color in ('R', 'B')
            ]
            for node in range(n)
        ]
        print(f'A: {answers=}')
        answers = tuple(map(min, answers))
        print(f'B: {answers=}')
        answers = tuple([
            -1 if (A == INF) else A
            for A in answers
        ])
        print(f'C: {answers=}')
        return answers

# NOTE: Started working once I combined the "get distances red" ands
#       "get distances blue" sections, because doing them separately
#       was interfering with the search being depth-first
# NOTE: Runtime 25 ms Beats 7.69%
# NOTE: Memory 18.32 MB Beats 6.15%
