class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        edges = roads
        n = len(edges) + 1

        adjacentTo = {}
        for i in range(n):
            adjacentTo.setdefault(i, set())
        for (a, b) in edges:
            adjacentTo[a].add(b)
            adjacentTo[b].add(a)
        # print(f'{adjacentTo=}')

        root = 0
        parentOf = {}
        childrenOf = {}
        for i in range(n):
            childrenOf.setdefault(i, set())
        parentOf[root] = None
        queue = {root}
        seen = set()
        while queue:
            node = queue.pop()
            if node in seen:
                continue
            else:
                seen.add(node)
            for neighbor in adjacentTo[node]:
                if parentOf[node] == neighbor:
                    continue
                parentOf[neighbor] = node
                childrenOf[node].add(neighbor)
                queue.add(neighbor)
        # print(f'{parentOf=}')
        # print(f'{childrenOf=}')

        @cache
        def subtreeSize(node: int) -> int:
            child_sizes = [
                subtreeSize(child)
                for child in childrenOf[node]
            ]
            return 1 + sum(child_sizes)
        
        liters = 0
        for i in range(n):
            employees = subtreeSize(i)
            print(f'[{i}] {employees}')
            if i == 0:
                print(f'  (already at capitol)')
                continue
            vans = employees // seats
            employees -= (vans * seats)
            if employees:
                vans += 1
            print(f'  ({vans=})')
            liters += vans

        return liters

# NOTE: Accepted on third Run (variable typo, indent typo)
# NOTE: Accepted on second Submit (Time Exceeded: cache)
# NOTE: Runtime 1191 ms Beats 5.03%
# NOTE: Memory 237.35 MB Beats 5.03%
