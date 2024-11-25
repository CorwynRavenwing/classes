class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

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
        while queue:
            node = queue.pop()
            for neighbor in adjacentTo[node]:
                if parentOf[node] == neighbor:
                    continue
                parentOf[neighbor] = node
                childrenOf[node].add(neighbor)
                queue.add(neighbor)
        # print(f'{parentOf=}')
        # print(f'{childrenOf=}')

        answers = [None] * n

        def DP(node: int) -> Dict[str,int]:
            nonlocal answers
            # updates answers array as a side-effect
            assert answers[node] is None
            my_label = labels[node]
            retval = Counter({
                my_label: 1,
            })
            # print(f'{node}: begin {retval}')
            for child in childrenOf[node]:
                child_retval = DP(child)
                # print(f'  {child}: {child_retval}')
                retval += child_retval
            # print(f'{node}: end {retval}')
            answers[node] = retval[my_label]
            return retval
        
        ignore = DP(root)
        # updates answers array as a side-effect
        return answers

# NOTE: Accepted on second Run (can't add Dict: use Counter instead)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 1831 ms Beats 5.95%
# NOTE: Memory 185.44 MB Beats 5.34%
