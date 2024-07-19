class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        reachableFrom = {}
        for (A, B, W) in edges:
            reachableFrom.setdefault(A, [])
            reachableFrom[A].append((B, W))

            reachableFrom.setdefault(B, [])
            reachableFrom[B].append((A, W))
        # print(f'{reachableFrom=}')

        distanceToLastNode = {}
        distanceToLastNode[n] = 0
        check = [(0, n)]
        while check:
            # print(f'L={len(check)}')
            check.sort()     # pick the shortest distance
            (distanceA, nodeA) = check.pop(0)
            # print(f'  check {(distanceA, nodeA)=}')
            for (nodeB, weightAB) in reachableFrom[nodeA]:
                distanceAB = distanceA + weightAB
                # print(f'    {(nodeB, weightAB)=} {distanceAB=}')
                if nodeB in distanceToLastNode:
                    oldDistanceB = distanceToLastNode[nodeB]
                    if oldDistanceB <= distanceAB:
                        # print(f'      Already a shorter distance: {oldDistanceB} <= {distanceAB}')
                        continue
                distanceToLastNode[nodeB] = distanceAB
                check.append((distanceAB, nodeB))
                # print(f'      Set new {distanceAB=}, re-check {nodeB=}')
        # print(f'{distanceToLastNode=}')

        restrictedPathsToNode = Counter()   # Dict, numeric values, auto-default=0
        restrictedPathsToNode[1] = 1        # only way to get here == we start here
        done = set()

        check = [
            (distanceToLastNode[1], 1)
        ]
        while check:
            # print(f'L={len(check)}')
            check.sort(reverse=True)     # pick the largest distance
            (distanceA, nodeA) = check.pop(0)
            pathsA = restrictedPathsToNode[nodeA]
            # print(f'  {nodeA=}: ({pathsA=}) {distanceA=}')
            if nodeA in done:
                # print(f'    Done already.')
                continue
            else:
                done.add(nodeA)
            for (nodeB, weightAB) in reachableFrom[nodeA]:
                pathsB = restrictedPathsToNode[nodeB]
                distanceB = distanceToLastNode[nodeB]
                # print(f'    {nodeB=}: ({pathsB=}) {distanceB=}')
                if distanceA < distanceB:
                    # print(f'      Uphill')
                    continue
                elif distanceA == distanceB:
                    # print(f'      Flat counts as uphill')
                    continue
                # print(f'    paths B:{pathsB} += A:{pathsA}, check {nodeB=}')
                restrictedPathsToNode[nodeB] += pathsA
                check.append(
                    (distanceB, nodeB)
                )
        # print(f'{restrictedPathsToNode=}')
        print(f'{restrictedPathsToNode[n]=}')

        mod = 10 ** 9 + 7
        return restrictedPathsToNode[n] % mod

