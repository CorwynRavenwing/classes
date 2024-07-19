# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        answer = 0

        def showNode(label: str, node: TreeNode):
            return  # Output Limit
            string = f'{label}: {node}'
            string = string.replace('TreeNode{', '{')
            string = string.replace('{val: ', '{')
            string = string.replace(', left: ', ' L:')
            string = string.replace(', right: ', ' R:')
            string = string.replace(':None', 'x')
            string = string.replace(' Lx Rx}', '}')
            print(string)

        def LeafNodeDistances(node: TreeNode, depth: int) -> List[int]:
            showNode(f'LND({depth})', node)
            nonlocal answer
            nonlocal distance
            leftDistances, rightDistances = [[],[]]
            if node.left is not None:
                leftDistances = LeafNodeDistances(node.left, depth + 1)
            if node.right is not None:
                rightDistances = LeafNodeDistances(node.right, depth + 1)
            showNode(f'Lnd({depth})', node)
            print(f'  L={leftDistances} R={rightDistances}')
            for L in leftDistances:
                for R in rightDistances:
                    nodeDistance = L + R - 2 * depth
                    if nodeDistance <= distance:
                        answer += 1
                        print(f'  {answer=}')
            bothDistances = leftDistances + rightDistances
            if bothDistances:
                return bothDistances
            else:
                return [depth]  # this is a leaf node
        
        ignore = LeafNodeDistances(root, 0)     # updates "answer" as side effect
        return answer

