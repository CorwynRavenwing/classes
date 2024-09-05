class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        INF = 10 ** 9

        OrderedTuple = lambda A, B: tuple([min(A,B),max(A,B)])

        adjacent = {}
        costs = {}
        for node in range(n):
            adjacent.setdefault(node, set())
        for (A, B, cost) in edges:
            adjacent[A].add(B)
            adjacent[B].add(A)
            E = OrderedTuple(A,B)
            costs.setdefault(E, INF)
            costs[E] = min(costs[E], cost)
        # print(f'{adjacent=}')
        # print(f'{costs=}')

        answer = [None] * n     # None means "we don't know yet"

        seen = set()
        queue = [(0, 0)]    # zero seconds to reach start node
        while queue:
            (time, node) = queue.pop(0)     # take earliest time first
            # print(f'{node}: ${time}')
            if node in seen:
                # print(f'  (seen)')
                continue
            else:
                seen.add(node)

            if answer[node] is not None:
                print(f'  (weird) {answer[node]=}')
                continue
            elif time >= disappear[node]:
                print(f'  (gone) @{disappear[node]}')
                answer[node] = -1
                continue
            else:
                answer[node] = time
            
            for A in adjacent[node]:
                if A in seen:
                    # skip several expensive calls if already seen
                    # print(f'  {A=} (seen)')
                    continue
                E = OrderedTuple(A,node)
                cost = costs[E]
                # print(f'  {A=} ${cost} -> {time + cost}')
                bisect.insort(
                    queue,
                    (time + cost, A)
                )

        if None in answer:
            answer = [
                A if (A is not None) else -1
                for A in answer
            ]

        # print(f'{answer=}')
        return answer

# NOTE: Accepted on second Submit (first was an Output Exceeded)
# NOTE: Runtime 4655 ms Beats 5.18%
# NOTE: Memory 84.42 MB Beats 7.62%
