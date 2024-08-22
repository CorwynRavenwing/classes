class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        Total = sum(values)
        print(f'{Total=}')

        adjacent = {}
        for i in range(len(values)):
            adjacent.setdefault(i, set())
        for A, B in edges:
            adjacent[A].add(B)
            adjacent[B].add(A)
        print(f'{adjacent=}')

        parent = [None] * len(values)
        parent[0] = None
        children = [None] * len(values)
        queue = {0}
        while queue:
            P = queue.pop()
            assert children[P] is None
            children[P] = []
            for C in adjacent[P]:
                if C == parent[P]:
                    continue
                parent[C] = P
                children[P].append(C)
                queue.add(C)
        print(f'{parent=}')
        print(f'{children=}')

        leaf_nodes = [
            N
            for N, C in enumerate(children)
            if C == []
        ]
        print(f'{leaf_nodes=}')

        # I was going to check for '0' values in leaf nodes
        # and their parents, which would complicate things; but
        # constraint: 'values' must consist of values from 1 to 1000000000 only

        @cache
        def sumOfAllDescendents(N: int) -> int:
            # Note: does *not* include value of N itself
            answer = sum([
                values[C] + sumOfAllDescendents(C)
                for C in children[N]
            ])
            print(f'SOAD({N}): {answer}')
            return answer

        # @cache
        def bestScoreFromNode(N: int) -> int:
            answer = max([
                # either (1) leave this node's value, take everything lower
                sumOfAllDescendents(N),
                (
                    # if no children, CANNOT do version (2) below
                    0
                    if (children[N] == [])
                    else
                    sum([
                        # or (2) take this node's value,
                        values[N],
                        # plus best score from children recursively
                        sum([
                            bestScoreFromNode(C)
                            for C in children[N]
                        ])
                    ])
                )
            ])
            print(f'BSFN({N}): {answer}')
            return answer

        return bestScoreFromNode(0)

# NOTE: Runtime 1645 ms Beats 5.34%
# NOTE: Memory 58.04 MB Beats 5.34%
