class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        
        n = len(edges) + 1

        adjacentTo = {}
        for i in range(1,n+1):
            adjacentTo.setdefault(i, set())
        for (a, b) in edges:
            print(f'{(a,b)=}')
            adjacentTo[a].add(b)
            adjacentTo[b].add(a)
        print(f'{adjacentTo=}')

        root = 1
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
        print(f'{parentOf=}')
        print(f'{childrenOf=}')

        # NOTE: starting at {root}, find longest depth
        # then pick any possible *odd* number of 1's
        # less than that length, ignoring 2's.

        return -99999

# NOTE: Acceptance Rate 54.0% (medium)

# NOTE: Incomplete: need to execute the strategy above
