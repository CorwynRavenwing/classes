class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adjacentRed = {}
        adjacentBlue = {}
        for i in range(n):
            adjacentRed.setdefault(i, set())
            adjacentBlue.setdefault(i, set())
        
        for Ai, Bi in redEdges:
            adjacentRed[Ai].add(Bi)

        for Ai, Bi in blueEdges:
            adjacentBlue[Ai].add(Bi)

        distanceBlue = {}   # dist to 0 starting Blue
        distanceRed = {}    # dist to 0 starting Red

        def setDistances(nodes: List[int], distance: int, red: bool):
            print(f'SD({nodes},{distance},{"red" if red else "blue"})')
            if not nodes:
                return
            
            if red:
                adjacentX = adjacentRed
                distanceX = distanceRed
            else:
                adjacentX = adjacentBlue
                distanceX = distanceBlue
            
            next_nodes = set()
            for node in nodes:
                if node in distanceX:
                    continue
                distanceX[node] = distance
                next_nodes |= adjacentX[node]
            
            setDistances(
                tuple(next_nodes),
                distance + 1,
                not red
            )

            return

        zeroNode = (0,)
        setDistances(zeroNode, 0, True)
        setDistances(zeroNode, 0, False)

        print(f'{distanceRed =}')
        print(f'{distanceBlue=}')

        INF = 10 ** 10

        answers = [
            (
                (distanceRed[node] if node in distanceRed else INF),
                (distanceBlue[node] if node in distanceBlue else INF),
            )
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

# NOTE: works for some inputs, fails for other inputs.
#       Trying a different way next.
