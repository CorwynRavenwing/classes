class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        adjacent = {
            node: neighbors
            for node, neighbors in enumerate(graph)
        }
        print(f'{adjacent=}')

        nodeColor = {}
        for node in range(len(graph)):
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

# NOTE: Accepted on first Submit
# NOTE: Runtime 166 ms Beats 8.30%
# NOTE: Memory 17.34 MB Beats 18.54%
