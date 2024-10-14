class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjacent = {}
        for (Ui, Vi, Wi) in times:
            adjacent.setdefault(Ui, {})
            adjacent[Ui][Vi] = Wi
        
        nodeDelay = {}
        queue = [(0, k)]    # second 0, node k
        while queue:
            (time, node) = queue.pop(0)     # earliest time
            print(f'{node=} {time=}')
            if node in nodeDelay:
                print(f'  (seen)')
            else:
                nodeDelay[node] = time
                if node not in adjacent:
                    print(f'  (no neighbors)')
                    continue
                neighbors = adjacent[node]
                for (nextNode, delay) in neighbors.items():
                    newTime = time + delay
                    bisect.insort(
                        queue,
                        (newTime, nextNode)
                    )
        allNodes = set(range(1, n + 1))
        reachedNodes = set(nodeDelay.keys())
        missingNodes = allNodes - reachedNodes
        if missingNodes:
            print(f'{missingNodes=}')
            return -1
        answer = max(nodeDelay.values())
        return answer

