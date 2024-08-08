class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # SHORTCUT: Bob will only take one possible path.  He will hit each
        # node on that path at a particular time.
        # Alice is a particular distance from each of those nodes.  If she reaches
        # them, she will receive either:
        # (A) full price, if her distance to the node < Bob's distance
        # (B) half price, if the paths are equal, or
        # (C) nothing, if her distance is > Bob's distance
        # THEREFORE, we can check the distance from Alice and Bob to that small list
        # of nodes, and *change their prices* to reflect what the future value will be.
        # THEN we ignore Bob altogether and look for the leaf node with maximal value.
        # We can also start at each leaf node and work upwards instead of downwards.

        adjacent = {}
        for N1, N2 in edges:
            adjacent.setdefault(N1, [])
            adjacent.setdefault(N2, [])
            adjacent[N1].append(N2)
            adjacent[N2].append(N1)
        # print(f'{adjacent=}')

        parentNode = {}
        parentNode[0] = None
        childNodes = {}
        leafNodes = set()

        queue = {0}
        seen = set()
        while queue:
            P = queue.pop()
            # print(f'{P=}')
            seen.add(P)
            childNodes.setdefault(P, set())
            for C in adjacent[P]:
                # print(f'  {C=}')
                if C in seen:
                    # print(f'    (seen)')
                    continue
                parentNode[C] = P
                childNodes[P].add(C)
                queue.add(C)
            if childNodes[P] == set():
                # print(f'  {P} is a leaf node')
                leafNodes.add(P)
        # print(f'{parentNode=}')
        # print(f'{childNodes=}')
        # print(f'{leafNodes=}')

        bob_path = []
        B = bob
        # print(f'Bob path: {bob=}')
        while B is not None:
            bob_path.append(B)
            B = parentNode[B]
            # print(f'  {B}')
        # print(f'{bob_path=}')
        # print(f'before: {amount=}')
        while bob_path:
            if len(bob_path) == 1:
                node = bob_path.pop()
                # print(f'Bob and Alice tie at {node=}')
                # print(f'  {amount[node]} -> {amount[node] //  2}')
                amount[node] //= 2
            else:
                aliceNode = bob_path.pop(-1)
                bobNode = bob_path.pop(0)
                # print(f'Bob reaches {bobNode} while Alice reaches {aliceNode}')
                # print(f'  {amount[bobNode]} -> {0}')
                amount[bobNode] = 0
        # print(f' after: {amount=}')

        answer = float('-inf')
        for Alice in leafNodes:
            # print(f'{Alice=}')
            A = Alice
            pathProfit = 0
            while A is not None:
                pathProfit += amount[A]
                # print(f'  {A=} {pathProfit=}')
                A = parentNode[A]
            answer = max(answer, pathProfit)

        return answer
# NOTE: Runtime 2533 ms Beats 13.23%
# NOTE: Memory 109.69 MB Beats 5.79%
