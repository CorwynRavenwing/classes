class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        adjacentTo = {}
        for i in range(n):
            adjacentTo.setdefault(i, set())
        for (a, b) in edges:
            adjacentTo[a].add(b)
            adjacentTo[b].add(a)
        # print(f'{adjacentTo=}')

        root = 0
        parentOf = {}
        childrenOf = {}
        for i in range(n):
            childrenOf.setdefault(i, set())
        parentOf[root] = None
        queue = {root}
        seen = set()
        while queue:
            node = queue.pop()
            if node in seen:
                continue
            else:
                seen.add(node)
            for neighbor in adjacentTo[node]:
                if parentOf[node] == neighbor:
                    continue
                parentOf[neighbor] = node
                childrenOf[node].add(neighbor)
                queue.add(neighbor)
        # print(f'{parentOf=}')
        # print(f'{childrenOf=}')

        restricted = set(restricted)    # speedier lookups

        queue = {root}
        answer = 0
        while queue:
            node = queue.pop()
            print(f'{node}:')
            if node in restricted:
                print(f'  RESTRICTED')
                continue
            print(f'  OK')
            answer += 1
            for child in childrenOf[node]:
                if child in restricted:
                    print(f'  -{child} restricted')
                    continue
                else:
                    print(f'  +{child}')
                    queue.add(child)

        return answer

# NOTE: Acceptance Rate 59.3% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 820 ms Beats 5.00%
# NOTE: Memory 117.40 MB Beats 5.00%
