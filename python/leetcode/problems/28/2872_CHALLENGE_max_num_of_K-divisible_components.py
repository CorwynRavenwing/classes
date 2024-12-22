class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        adjacentTo = {}
        for i in range(n):
            adjacentTo.setdefault(i, set())
        for (a, b) in edges:
            adjacentTo[a].add(b)
            adjacentTo[b].add(a)
        print(f'{adjacentTo=}')

        root = 0
        parentOf = {}
        childrenOf = {}
        for i in range(n):
            childrenOf.setdefault(i, set())
        parentOf[root] = None
        queue = {root}
        while queue:
            node = queue.pop()
            for neighbor in adjacentTo[node]:
                if parentOf[node] == neighbor:
                    continue
                parentOf[neighbor] = node
                childrenOf[node].add(neighbor)
                queue.add(neighbor)
        print(f'{parentOf=}')
        print(f'{childrenOf=}')

        def subtotal_and_maxcuts(node: int) -> Tuple[int,int]:
            # nonlocal childrenOf   # read-only
            # nonlocal values       # read-only
            # nonlocal k            # read-only
            print(f'SAM({node})')
            (subTotal, maxCuts) = (0, 0)
            subTotal += values[node]
            for child in childrenOf[node]:
                (ST, MC) = subtotal_and_maxcuts(child)
                subTotal += ST
                maxCuts += MC
            subTotal %= k
            if subTotal == 0:
                print(f'  SAM({node}): CUT')
                return (0, maxCuts + 1)
            else:
                print(f'  SAM({node}): keep')
                return (subTotal, maxCuts)

        (subTotal, maxCuts) = subtotal_and_maxcuts(root)

        return maxCuts


# NOTE: Acceptance Rate 68.8% (HARD)
# NOTE: Accepted on second Run (variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 812 ms Beats 7.41%
# NOTE: Memory 53.42 MB Beats 7.41%
