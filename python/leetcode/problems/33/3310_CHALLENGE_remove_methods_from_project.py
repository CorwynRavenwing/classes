class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        nodes = set(range(n))
        childrenOf = {}

        for i in nodes:
            childrenOf.setdefault(i, set())

        for (Ai, Bi) in invocations:
            childrenOf[Ai].add(Bi)
        
        # print(f'{childrenOf=}')

        reachable_from_k = set()
        queue = {k}
        while queue:
            # print(f'Q#={len(queue)}:')
            X = queue.pop()
            if X in reachable_from_k:
                continue
            else:
                # print(f'  +{X}')
                reachable_from_k.add(X)
                queue |= childrenOf[X]
        # print(f'{reachable_from_k=}')

        unreachable_from_k = nodes - reachable_from_k
        # print(f'{unreachable_from_k=}')

        for X in unreachable_from_k:
            assert X not in reachable_from_k
            for C in childrenOf[X]:
                if C in reachable_from_k:
                    print(f'NOPE! {X} -> {C}')
                    # If it is not possible to remove
                    # all the suspicious methods,
                    # none should be removed.
                    return list(nodes)
                # print(f'okay: {X} -> {C}')
            # print(f'okay: {X}')

        return list(unreachable_from_k)

# NOTE: Acceptance Rate 52.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 423 ms Beats 38.97%
# NOTE: Memory 110.63 MB Beats 50.73%
