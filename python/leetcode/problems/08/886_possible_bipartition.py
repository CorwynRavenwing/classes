class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        # we borrow some code from #785:

        adjacent = {}
        for node in range(1, n + 1):
            adjacent.setdefault(node, set())
        for A, B in dislikes:
            adjacent[A].add(B)
            adjacent[B].add(A)
        print(f'{adjacent=}')

        nodeColor = {}
        for node in range(1, n + 1):
            print(f'{node=}')
            if node in nodeColor:
                print(f'  (skip, color={nodeColor[node]})')
                continue
            color = 'A'
            nodeColor[node] = color
            queue = {node}
            while queue:
                print(f'{queue=}')
                newQ = set()
                newColor = ('A' if (color == 'B') else 'B')
                print(f'  {color=} {newColor=}')
                for Q in queue:
                    print(f'  {Q=}:{nodeColor[Q]}')
                    for neighbor in adjacent[Q]:
                        print(f'    {neighbor=}')
                        if neighbor in nodeColor:
                            if nodeColor[neighbor] != newColor:
                                print(f'      Nope! {newColor=}, {nodeColor[neighbor]=}')
                                return False
                            else:
                                print(f'      (skip, color={nodeColor[neighbor]})')
                                continue
                        nodeColor[neighbor] = newColor
                        print(f'      Set {newColor=}')
                        newQ.add(neighbor)
                queue = newQ
                color = newColor
        
        # if we got here, we succeeded
        print(f'{nodeColor=}')
        return True

# NOTE: Runtime 700 ms Beats 5.29%
# NOTE: Memory 23.55 MB Beats 8.14%
