# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        adjacentTo = {}

        def populate_adjacentTo(node: TreeNode, parent: int) -> None:
            nonlocal adjacentTo
            if node is None:
                return
            # print(f'p_At({node.val if node else "-"},{parent})')
            value = node.val
            adjacentTo.setdefault(value, set())
            if parent is not None:
                adjacentTo[value].add(parent)
                adjacentTo[parent].add(value)
            populate_adjacentTo(node.left, value)
            populate_adjacentTo(node.right, value)
            return
        
        populate_adjacentTo(root, None)
        # print(f'{adjacentTo=}')

        infected = set()
        healthy = set(adjacentTo.keys())
        queue = {start}
        infected |= queue
        healthy -= queue
        time = 0
        while queue and healthy:
            time += 1
            # print(f'{time=}\n\t{healthy =}\n\t{infected=}')
            print(f'{time=}\n\tqueue   ={len(queue)}\n\thealthy ={len(healthy)}\n\tinfected={len(infected)}')
            newQ = set()
            for node in queue:
                for neighbor in adjacentTo[node]:
                    if neighbor in infected:
                        continue
                    else:
                        infected.add(neighbor)
                    if neighbor in healthy:
                        healthy.remove(neighbor)
                    newQ.add(neighbor)
            queue = newQ

        return time

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 402 ms Beats 5.14%
# NOTE: Memory 79.70 MB Beats 5.27%
