class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        
        # we borrow some code from #3372:

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

        cache_even_odd = []
        def clear_even_odd_caches() -> None:
            nonlocal cache_even_odd
            cache_even_odd = []

        def count_nodes_even_odd(startNode: int, parity: int, adjacentTo: Dict[int,List[int]]) -> int:
            nonlocal cache_even_odd

            # SHORTCUT: all even nodes are a group, and all odd nodes are a group;
            # we only need to calculate their membership once for each "adjacentTo"

            for cache in cache_even_odd:
                if startNode in cache:
                    return len(cache)
            # startNode not found in cache: compute and store
            
            seen = set()
            matches = set()
            queue = {startNode}
            distance = 0
            answer = 0
            # print(f'\nCNEO({startNode},{parity}):')
            while queue:
                # print(f'  node#{startNode} +{distance}: {len(queue)}')
                # print(f'  {queue}')
                newQ = set()

                for node in queue:
                    if node in seen:
                        continue
                    else:
                        seen.add(node)
                    if distance % 2 == parity:
                        matches.add(node)
                        answer += 1
                    # else wrong parity: not an answer, and don't' mark "seen" yet
                    newQ |= adjacentTo[node]

                queue = newQ
                distance += 1

            cache = matches
            cache_even_odd.append(cache)
            print(f'  set cache #{len(cache_even_odd)} to {cache}')

            assert answer == len(matches) == len(cache)
            return answer

        def total_nodes_even_odd(size: int, parity: int, adjacentTo: Dict[int,List[int]]) -> List[int]:
            return [
                count_nodes_even_odd(startNode, parity, adjacentTo)
                for startNode in range(size)
            ]

        print(f'Check tree #1:')
        parities_tree1 = total_nodes_even_odd(N, 0, adjacent1)      # even in tree 1
        clear_even_odd_caches()
        print(f'Check tree #2:')
        parities_tree2even = total_nodes_even_odd(M, 0, adjacent2)  # even in tree 2
        parities_tree2odd = total_nodes_even_odd(M, 1, adjacent2)   # odd in tree 2
        print(f'{parities_tree1=}')
        print(f'{parities_tree2even=}')
        print(f'{parities_tree2odd=}')

        best_tree2_distance = max(parities_tree2even + parities_tree2odd)
        answers = [
            distance + best_tree2_distance
            for distance in parities_tree1
        ]

        return answers


# NOTE: Acceptance Rate 54.9% (HARD)

# NOTE: re-used much of prior version
# NOTE: accepted on first Run
# NOTE: accepted on third Submit (Time Exceeded, needed new algorithm)
# NOTE: Runtime 1196 ms Beats 6.82%
# NOTE: Memory 145.94 MB Beats 9.09%
