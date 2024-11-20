# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        levelForNode = {}
        nodesAtLevel = {}
        bestTwoDepthsAtLevel = {}
        maxDepthForNode = {}

        def maxDepth(node: TreeNode, level=1) -> int:

            DEBUG = False
            
            if DEBUG: print(f'maxDepth({node.val if node else "-"},{level})')
            if not node:
                return level - 1
            
            nodesAtLevel.setdefault(level, set())
            nodesAtLevel[level].add(node.val)
            if DEBUG: print(f'  set nodesAtLevel[{level}] + {node.val}')

            levelForNode[node.val] = level
            if DEBUG: print(f'  set levelForNode[{node.val}] = {level}')

            Left = maxDepth(node.left, level + 1)
            Right = maxDepth(node.right, level + 1)

            MyAnswer = max(Left, Right)

            maxDepthForNode[node.val] = MyAnswer
            if DEBUG: print(f'  set maxDepthForNode[{node.val}] = {MyAnswer}')

            bestTwoDepthsAtLevel.setdefault(level, [-1, -1])
            bestTwoDepthsAtLevel[level].append(MyAnswer)
            bestTwoDepthsAtLevel[level].sort(reverse=True)
            if DEBUG: print(f'  set bestTwoDepthsAtLevel[{level}] + {MyAnswer}')
            if len(bestTwoDepthsAtLevel[level]) >= 3:
                del bestTwoDepthsAtLevel[level][-1]
                if DEBUG: print(f'    del bestTwoDepthsAtLevel[{level}]')
            if DEBUG: print(f'  new {bestTwoDepthsAtLevel[level]=}')
            
            return MyAnswer

        TreeDepth = maxDepth(root)

        def depth_without_node(N: int) -> int:
            level = levelForNode[N]
            depth = maxDepthForNode[N]
            (first, second) = bestTwoDepthsAtLevel[level]
            if first != depth:
                # we deleted something irrelevant
                return TreeDepth
            # else we deleted a node on the deepest path

            if second == -1:
                # there were no other nodes on this level
                return level - 1
                # prior level is now the bottom of the tree
            # else there were other nodes
            
            return second

        def doQuery(Q: int) -> int:
            return depth_without_node(Q) - 1
        
        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 42.0% (HARD)
# NOTE: Challenge failed due to completing it after the time limit
# NOTE: Runtime 387 ms Beats 19.88%
# NOTE: Memory 79.90 MB Beats 5.46%
