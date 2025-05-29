class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        # SHORTCUT 1: since we may pick any node in tree 1 as U,
        # and any node in tree 2 as V, and since we are trying
        # to maximize the number of nodes reachable in <=K steps,
        # we should therefore always pick node I as node U, so that
        # the distance within tree 1 is zero, and the total distance
        # is only the distance within tree 2 (plus 1 for the UV edge)
        # This lowers the complexity from O(n * n^2 * m^2) to O(n^2 * m^2)

        # SHORTCUT 2: for every possible node in tree 2 as V, there
        # is a specific number of nodes reachable in (k - 1) steps.
        # Choose the node with the highest such count.
        # *Always* use this node as V.
        # This lowers the complexity to O(n^2 + m^2)

        def edges_to_adjacent(size: int, edges: List[Tuple[int,int]]) -> Dict[int,List[int]]:
            adjacentTo = {}
            for i in range(size):
                adjacentTo.setdefault(i, set())
            for (a, b) in edges:
                adjacentTo[a].add(b)
                adjacentTo[b].add(a)
            # print(f'{adjacentTo=}')
            return adjacentTo

        N = len(edges1) + 1
        M = len(edges2) + 1
        print(f'\n{N=}')
        adjacent1 = edges_to_adjacent(N, edges1)
        print(f'\n{M=}')
        adjacent2 = edges_to_adjacent(M, edges2)

        def count_nodes_LT_distance(startNode: int, k: int, adjacentTo: Dict[int,List[int]]) -> int:
            if k < 0:
                return 0
            elif k == 0:
                return 1
            seen = set()
            queue = {startNode}
            distance = 0
            answer = 0
            # print(f'\nCNAD({startNode},{k}):')
            while queue:
                # print(f'  node#{startNode} +{distance}: {len(queue)}')
                # print(f'  {queue}')
                newQ = set()

                for node in queue:
                    if node in seen:
                        continue
                    else:
                        seen.add(node)
                        answer += 1
                    newQ |= adjacentTo[node]

                queue = newQ
                distance += 1
                if distance > k:
                    print(f'{distance=} > {k}')
                    break
            return answer
            
        def total_nodes_LT_distance(size: int, k: int, adjacentTo: Dict[int,List[int]]) -> List[int]:
            return [
                count_nodes_LT_distance(startNode, k, adjacentTo)
                for startNode in range(size)
            ]
        
        distances_tree1 = total_nodes_LT_distance(N, k, adjacent1)
        distances_tree2 = total_nodes_LT_distance(M, k - 1, adjacent2)
        print(f'{distances_tree1=}')
        print(f'{distances_tree2=}')

        best_tree2_distance = max(distances_tree2)
        answers = [
            distance + best_tree2_distance
            for distance in distances_tree1
        ]

        return answers

# NOTE: Acceptance Rate 68.7% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge case k=0, Output Exceeded)
# NOTE: Runtime 2332 ms Beats 18.11%
# NOTE: Memory 19.45 MB Beats 21.26%
