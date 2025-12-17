class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        
        adjacentTo = {}
        for i in range(1, n + 1):
            adjacentTo.setdefault(i, set())
        for (a, b) in hierarchy:
            adjacentTo[a].add(b)
            adjacentTo[b].add(a)
        print(f'{adjacentTo=}')

        root = 1
        parentOf = {}
        childrenOf = {}
        for i in range(1, n + 1):
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
        print(f'{parentOf=}')
        print(f'{childrenOf=}')

        def DP_children(node: int, discount: bool, budgetLeft: int) -> int:
            print(f'DP_children({node},{discount},{budgetLeft})')
            # nonocal childrenOf
            children = tuple(childrenOf[node])

            def dp_child_take(index: int, budgetLeft: int) -> int:
                print(f'dp_child_take({index},{budgetLeft})')
                # take this child
                child = children[index]
                return DP(child, discount, budgetLeft)
                pass

            def dp_child_skip(index: int, budgetLeft: int) -> int:
                print(f'dp_child_skip({index},{budgetLeft})')
                # skip this child
                return dp_child(index + 1, budgetLeft)

            def dp_child(index: int, budgetLeft: int) -> int:
                print(f'dp_child({index},{budgetLeft})')
                if budgetLeft == 0:
                    return 0
                if budgetLeft < 0:
                    return None
                try:
                    _ = children[index]
                except IndexError:
                    return 0
                answers = [
                    dp_child_take(index, budgetLeft),
                    dp_child_skip(index, budgetLeft),
                ]
                while None in answers:
                    answers.remove(None)
                return max(answers, default=None)
            
            return dp_child(0, budgetLeft)

        def DP_take(node: int, discount: bool, budgetLeft: int) -> int:
            print(f'DP_take({node},{discount},{budgetLeft})')
            if budgetLeft == 0:
                return 0
            if budgetLeft < 0:
                return None
            price = present[node - 1]
            if discount:
                price //= 2
            value = future[node - 1]
            children = DP_children(node, True, budgetLeft - price)
            if children is None:
                return None
            else:
                return value - price + children

        def DP_skip(node: int, discount: bool, budgetLeft: int) -> int:
            print(f'DP_skip({node},{discount},{budgetLeft})')
            return DP_children(node, False, budgetLeft)

        def DP(node: int, discount: bool, budgetLeft: int) -> int:
            print(f'DP({node},{discount},{budgetLeft})')
            # returns max profit for subtree rooted at Node:
            #   discount: is discount available?
            #   budgetLeft: amount of budget which has not yet been spent 
            answers = [
                DP_take(node, discount, budgetLeft),
                DP_skip(node, discount, budgetLeft),
            ]
            while None in answers:
                answers.remove(None)
            return max(answers, default=None)

        answer = DP(root, False, budget)
        if answer is None:
            return 0
        else:
            return answer
        
# NOTE: Acceptance Rate 26.1% (HARD)

# NOTE: INCOMPLETE: wrong answer for testcase 275
