class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        mod = 10 ** 9 + 7

        # Note: if path A -> B -> C -> B -> C -> D takes a certain amount of time,
        # then the path A -> B -> C -> D is SHORTER, and therefore the path ABCBCD
        # can neither be, nor tie with, the shortest path, and is therefore irrelevant.
        # We will therefore IGNORE any paths that include the same node more than once.

        roadsFrom = {}  # fromId: {set, of, toId, values}
        roadTimes = {}  # (fromId, toId): time
        for uI in range(n):
            roadsFrom.setdefault(uI, set())
        for (uI, vI, timeI) in roads:
            roadsFrom[uI].add(vI)
            roadsFrom[vI].add(uI)
            roadTimes[(uI, vI)] = timeI
            roadTimes[(vI, uI)] = timeI
        print(f'{roadsFrom=}')
        print(f'{roadTimes=}')

        fastest_paths_to = {}
        fastest_paths_to[0] = (1, 0)   # (paths, time)
        seen = set()
        queue = [(0,0)]     # (time, nodeIndex)
        while queue:
            print(f'L={len(queue)}')
            queue.sort()    # always pick the shortest time
            (timeBefore, startNode) = queue.pop(0)
            (pathsToHere, ignore) = fastest_paths_to[startNode]
            print(f'  n={startNode}: ({timeBefore}) [{pathsToHere}]')
            if startNode in seen:
                print(f'    (done already)')
                continue
            else:
                seen.add(startNode)
            for endNode in roadsFrom[startNode]:
                totalPaths = pathsToHere
                timeDuring = roadTimes[(startNode, endNode)]
                totalTime = timeBefore + timeDuring
                print(f'    n={endNode}: ({timeDuring}:{totalTime})')
                if endNode in fastest_paths_to:
                    (priorPaths, priorTime) = fastest_paths_to[endNode]
                    if priorTime < totalTime:
                        print(f'      Slower than {priorTime}: skip')
                        continue
                    elif priorTime > totalTime:
                        print(f'      Overwrite slower ({priorTime}) time record')
                    elif priorTime == totalTime:
                        print(f'      Merge equal-time paths {pathsToHere} + {priorPaths}')
                        totalPaths += priorPaths
                else:
                    print(f'      Create new time record')
                fastest_paths_to[endNode] = (totalPaths, totalTime)
                print(f'        = [{totalPaths}]')
                queue.append(
                    (totalTime, endNode)
                )
        (pathsToHere, totalTime) = fastest_paths_to[n - 1]
        print(f'Paths to {n - 1}: time={totalTime}, paths={pathsToHere}')

        return pathsToHere % mod

# NOTE: re-ran for challenge:
# NOTE: Runtime 683 ms Beats 5.62%
# NOTE: Memory 29.18 MB Beats 5.31%
