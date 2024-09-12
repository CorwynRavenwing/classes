class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        adjacent = {}
        for i in range(n):
            adjacent.setdefault(i, set())
        for i in range(n - 1):
            adjacent[i].add(i + 1)
        print(f'{adjacent=}')

        INF = float('+inf')
        distance = [INF] * n
        distance[0] = 0

        def compute_distances_starting_at(initialNode: int) -> None:
            queue = [(distance[initialNode], initialNode)]
            while queue:
                (dist, node) = queue.pop(0)
                real_dist = distance[node]
                if real_dist < dist:
                    dist = real_dist
                print(f'{node}: {dist}')
                for A in adjacent[node]:
                    A_dist = distance[A]
                    A_this = dist + 1
                    if A_this < A_dist:
                        if A_dist == INF:
                            print(f'  {A=} initial distance {A_this}')
                        else:
                            print(f'  {A=}: Faster via this link ({A_this} < {A_dist})')
                        distance[A] = A_this
                        bisect.insort(
                            queue,
                            (A_this, A)
                        )

        def new_dist_after_recomputing(node: int) -> int:
            compute_distances_starting_at(node)
            return distance[n - 1]

        initial_distance = new_dist_after_recomputing(0)
        print(f'{initial_distance=}')

        def doQuery(Q: List[int]) -> int:
            (fromI, toI) = Q
            adjacent[fromI].add(toI)
            return new_dist_after_recomputing(fromI)
        
        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Accepted on first Submit
# NOTE: Runtime 699 ms Beats 77.09%
# NOTE: Memory 17.26 MB Beats 5.50%
