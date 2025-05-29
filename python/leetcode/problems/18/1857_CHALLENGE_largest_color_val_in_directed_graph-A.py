class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        DEBUG = False

        # PROCESS: we DP on "maximum count of nodes with
        # color C reachable from node X":
        # answer is max(DP( this color, each node reachable from here))
        # answer is +1 if C === node X's color.

        # SHORTCUT: the largest answer will always belong to a node
        # that has zero in-degree, because for any node *with* in-degree,
        # the DP() for each predecessor node is either equal, or greater by 1,
        # for each color, to the DP() for this node.
        # Therefore we only need to check DP() for each root and each color

        # UPDATE: If we do this, we also need to check for cycles.

        n = len(colors)     # there is 1 'colors' entry for each node
        nodes = tuple(range(n))

        ChildrenOf = {
            node: set()
            for node in nodes
        }
        ParentsOf = {
            node: set()
            for node in nodes
        }
        for Aj, Bj in edges:
            ChildrenOf[Aj].add(Bj)
            ParentsOf[Bj].add(Aj)
        if DEBUG: print(f'{ChildrenOf=}')
        if DEBUG: print(f'{ParentsOf=}')

        def graph_has_cycles(n: int, ChildrenOf: Dict[int,Set[int]]) -> bool:
            print(f'GHC({n}):')
            seen = [False] * n
            loop = [False] * n

            def node_has_cycles(node: int) -> bool:
                # print(f'    NHC({node})')
                if loop[node]:
                    # print(f'      YES')
                    return True
                else:
                    loop[node] = True
                    for child in ChildrenOf[node]:
                        if node_has_cycles(child):
                            # print(f'      YES')
                            return True
                    loop[node] = False
                    # print(f'      no')
                    return False

            for i in range(n):
                if seen[i]:
                    print(f'  {i}: seen')
                    continue
                else:
                    seen[i] = True
                print(f'  {i}: check')
                if node_has_cycles(i):
                    return True
            print(f'  No cycles.')
            return False
        
        if graph_has_cycles(n, ChildrenOf):
            print(f'  GRAPH HAS CYCLES')
            return -1

        roots = {
            node
            for node, predecessors in ParentsOf.items()
            if len(predecessors) == 0
        }
        if DEBUG: print(f'{roots=}')
        if len(roots) == 0:
            print(f'No roots!  There must be a cycle')
            return -1

        color_set = set(colors)
        if DEBUG: print(f'{color_set=}')

        @cache
        def DP(node: int, color: str) -> int:
            if DEBUG: print(f'DP({node},{color})')
            try:
                answers = [
                    DP(next_node, color)
                    for next_node in ChildrenOf[node]
                ]
            except RecursionError:
                print(f'  LOOP!')
                return -1
            if DEBUG: print(f'  {answers=}')
            if -1 in answers:
                print(f'  cascade loop')
                return -1
            answer = max(answers, default=0)
            if color == colors[node]:
                if DEBUG: print(f'  {answer} +1')
                answer += 1
            else:
                if DEBUG: print(f'  {answer}')
            
            return answer
        
        answers = [
            DP(node, color)
            for node in roots       # only check nodes with no in-degree
            for color in color_set  # only check each color once
        ]
        if DEBUG: print(f'\nTOTAL: {answers=}')
        if -1 in answers:
            print(f'  found a loop')
            return -1
        
        return max(answers)

# NOTE: Acceptance Rate 57.6% (HARD)

# NOTE: correct, but Time Limit Exceeded for large inputs.
