class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        reachable = {
            B
            for A, B in edges
        }
        print(f'{reachable=}')

        all_nodes = set(range(n))
        unreachable = all_nodes - reachable
        print(f'{unreachable=}')

        return tuple(unreachable)

# NOTE: Accepted on second Run (return-type mismatch)
# NOTE: Accepted on first Submit
# NOTE: Runtime 39 ms Beats 36.34%
# NOTE: Memory 47.22 MB Beats 60.42%
