class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def tuplify(edges: List[List[int]]) -> List[List[int]]:
            return tuple(
                map(tuple, edges)
            )
        
        edges1 = tuplify(edges1)    # make them each hashable
        edges2 = tuplify(edges2)

        @cache
        def adjacency_dict(n: int, edges: List[List[int]]) -> Dict[int,List[int]]:
            adjacentTo = {}
            for i in range(n):
                adjacentTo.setdefault(i, set())
            for (a, b) in edges:
                adjacentTo[a].add(b)
                adjacentTo[b].add(a)
            # print(f'{adjacentTo=}')
            return adjacentTo

        def tree_diameter(edges: List[List[int]]) -> int:
            # print(f'\ntree_diameter({edges})')

            n = len(edges) + 1
            adjacentTo = adjacency_dict(n, edges)
            max_links = max(
                map(len, adjacentTo.values())
            )
            print(f'{max_links=}')
            if max_links == 1:
                print(f'  SHORTCUT 1')
                return 1
            if max_links == 2:
                print(f'  SHORTCUT 2')
                return n - 1

            # returns all node ids found 
            def path_to_farthest_point(startPoint: int, priorPoint=None) -> List[int]:
                # nonlocal adjacentTo    # read-only
                # print(f'  PtFP({startPoint},{priorPoint})')
                possibles = [
                    path_to_farthest_point(neighbor, startPoint)
                    for neighbor in adjacentTo[startPoint]
                    if neighbor != priorPoint
                ]
                if not possibles:
                    return [startPoint]
                
                # print(f'  PtFP({startPoint},{priorPoint}): {possibles=}')
                lengths = tuple(map(len, possibles))
                # print(f'    {lengths=}')
                maxLen = max(lengths)
                with_max_length = [
                    P
                    for P in possibles
                    if len(P) == maxLen
                ]
                # print(f'    {with_max_length=}')
                chosen = with_max_length[0]
                # print(f'    {chosen=}')
                return [startPoint] + chosen

            Xpath = path_to_farthest_point(0)   # 0 is arbitrary

            # print(f'  {Xpath=}')
            # if len(Xpath) == (n - 1):
            #     print(f'  SHORTCUT 3: RETURN n - 1')
            #     # NOPE, this shortcut is getting wrong answers.
            #     return n - 1
            X = Xpath[-1]   # endpoint of this path
            Ypath = path_to_farthest_point(X)   # now start there
            # print(f'  {Ypath=}')

            return len(Ypath) - 1   # diameter === count of edges, not nodes

        diam1 = tree_diameter(edges1)
        diam2 = tree_diameter(edges2)
        print()

        components = [
            (diam1 + 1) // 2,   # half of tree 1
            (diam2 + 1) // 2,   # half of tree 2
            1,                  # linking edge between trees
        ]
        print(f'  {components=}')
        diam3 = sum(components)
        print(f'{diam1=} {diam2=} {diam3=}')

        return max(diam1, diam2, diam3)

# NOTE: Acceptance Rate 34.9% (HARD)
# NOTE: Accepted on second Submit (Time Limit Exceeded)
# NOTE: Runtime 1306 ms Beats 10.34%
# NOTE: Memory 138.12 MB Beats 15.17%
