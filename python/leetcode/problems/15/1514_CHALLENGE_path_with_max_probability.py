class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adjacent = {}
        for A in range(n):
            adjacent.setdefault(A, {})
        for ((A, B), prob) in zip(edges, succProb):
            print(f'{A=}->{B=}: {prob=}')
            adjacent[A][B] = prob
            adjacent[B][A] = prob
        print(f'{adjacent=}')

        seen = set()
        queue = [(-1.0, start_node)]    # 100% chance of reaching start node
        while queue:
            (neg_prob, location) = queue.pop(0)
            # queue is kept in order by negative probability
            print(f'{location=} %={-neg_prob}')
            if location == end_node:
                print(f'  FOUND!')
                return -neg_prob
            if location in seen:
                print(f'  (seen)')
                continue
            else:
                seen.add(location)
            for N, P in adjacent[location].items():
                print(f'  {N}: {P}')
                bisect.insort(
                    queue,
                    (
                        neg_prob * P,
                        N
                    )
                )

        print(f'no path found')
        return 0.0

# NOTE: Accepted on first Submit
# NOTE: Runtime 987 ms Beats 5.02%
# NOTE: Memory 29.80 MB Beats 19.10%
