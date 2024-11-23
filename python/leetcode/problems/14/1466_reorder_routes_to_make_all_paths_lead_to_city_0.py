class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        adjacent = {}
        backwards = set()
        for i in range(n):
            adjacent.setdefault(i, set())
        for (A, B) in connections:
            adjacent[A].add(B)
            adjacent[B].add(A)
            backwards.add((B, A))
        
        def DP(sourceNode: int, priorNode=None) -> int:
            print(f'DP({sourceNode},{priorNode})')
            answer = 0
            for node in adjacent[sourceNode]:
                if node == priorNode:
                    print(f'  skip {node}')
                    continue
                print(f'  -> {node}')
                path = (node, sourceNode)   # is the flow from node towards source?
                if path in backwards:
                    print(f'  reverse {path=}')
                    answer += 1
                answer += DP(node, sourceNode)
            return answer
        
        return DP(0)

# NOTE: Accepted on second Run (first was parity error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 532 ms Beats 5.05%
# NOTE: Memory 62.63 MB Beats 5.01%
