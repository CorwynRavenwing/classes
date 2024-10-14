class Graph:

    # we borrow some code from #778:

    def networkDelay(self, adjacent: Dict[any,Dict[any,int]], source: any, target: any) -> int:
        nodeDelay = {}
        queue = [(0, source)]    # second 0, node "source"
        while queue:
            (time, node) = queue.pop(0)     # earliest time
            # print(f'{node=} {time=}')
            if node in nodeDelay:
                # print(f'  (seen)')
                continue
            else:
                nodeDelay[node] = time
                if node not in adjacent:
                    # print(f'  (no neighbors)')
                    continue
                neighbors = adjacent[node]
                for (nextNode, delay) in neighbors.items():
                    newTime = time + delay
                    bisect.insort(
                        queue,
                        (newTime, nextNode)
                    )
        try:
            answer = nodeDelay[target]
        except KeyError:
            answer = None
        return answer

    def __init__(self, n: int, edges: List[List[int]]) -> None:
        self.N = n
        self.adjacent = {}
        for E in edges:
            self.addEdge(E)
        return

    def addEdge(self, edge: List[int]) -> None:
        (From, To, Cost) = edge
        self.adjacent.setdefault(From, {})
        self.adjacent[From][To] = Cost
        return

    def shortestPath(self, node1: int, node2: int) -> int:
        delay = self.networkDelay(self.adjacent, node1, node2)
        return (
            delay
            if delay is not None
            else -1
        )

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

# NOTE: Acceptance Rate 70.6% (HARD)
# NOTE: Accepted on second Run (first was variable scope typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 5099 ms Beats 5.04%
# NOTE: Memory 19.80 MB Beats 48.58%
