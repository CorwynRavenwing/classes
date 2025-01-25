class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        adjacent = {
            node: set(neighbors)
            for node, neighbors in enumerate(graph)
        }

        safe = set()
        cycles = set()
        current = set()
        while adjacent:
            # print(f'{adjacent=}')
            new_safe = {
                node
                for node, neighbors in adjacent.items()
                if not neighbors
            }
            print(f'{new_safe=}')
            if not new_safe:
                break
            safe |= new_safe
            frozen_for_loop = tuple(adjacent.items())
            for node, neighbors in frozen_for_loop:
                if node in new_safe:
                    print(f'checking: {node} {neighbors}')
                    print(f'  DELETE')
                    if adjacent[node]:
                        raise Exception(f'ERROR! {adjacent[node]=} SHOULD BE EMPTY')
                    del adjacent[node]
                to_delete = neighbors & new_safe
                if to_delete:
                    print(f'checking: {node} {neighbors}')
                    print(f'  {to_delete=}')
                    # print(f'    before {adjacent[node]}')
                    adjacent[node] -= to_delete
                    # print(f'    after: {adjacent[node]}')

        return sorted(safe)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 1479 ms Beats 5.06%
# NOTE: Memory 26.33 MB Beats 5.13%

# NOTE: re-ran for challenge:
# NOTE: Runtime 1044 ms Beats 5.04%
# NOTE: Memory 27.94 MB Beats 5.04%
