# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def showNode(label: str, node: TreeNode) -> None:

            def NodeToString(node: TreeNode, depth=0) -> str:
                maxDepth = 2
                if depth > maxDepth:
                    return '...'
                left = ''
                right = ''
                if node.left:
                    nodeStr = NodeToString(node.left, depth + 1)
                    left = f' L:{nodeStr}'
                if node.right:
                    nodeStr = NodeToString(node.right, depth + 1)
                    right = f' R:{nodeStr}'
                LB = '{'
                RB = '}'
                return f'{LB}{node.val}{left}{right}{RB}'

            nodeStr = NodeToString(node)
            string = f'{label}: {nodeStr}'
            # string = string.replace('TreeNode{', '{')
            # string = string.replace('{val: ', '{')
            # string = string.replace(', left: ', ' L:')
            # string = string.replace(', right: ', ' R:')
            # string = string.replace(' L:None', '')
            # string = string.replace(' R:None', '')
            # string = string.replace(' (L) (R)}', '}')
            print(string)
        
        def sum_of_tree(node: TreeNode) -> int:
            # showNode('SOT()', node)
            nodeSum = node.val
            if node.left is not None:
                nodeSum += sum_of_tree(node.left)
            if node.right is not None:
                nodeSum += sum_of_tree(node.right)
            return nodeSum

        def sum_and_subtree_sum_nearest_M(node: TreeNode, M: float) -> Tuple[int,int]:
            # showNode('SSNM()', node)
            answers = []
            nodeSum = node.val
            if node.left is not None:
                (leftSum, leftAnswer) = sum_and_subtree_sum_nearest_M(node.left, M)
                answers.append(leftAnswer)
                nodeSum += leftSum
            if node.right is not None:
                (rightSum, rightAnswer) = sum_and_subtree_sum_nearest_M(node.right, M)
                nodeSum += rightSum
                answers.append(rightAnswer)
            answers.append(nodeSum)
            # showNode('ssnm()', node)
            # print(f'  -> {answers}')
            if len(answers) == 1:
                minDifference = answers[0]
                return (nodeSum, minDifference)

            differences = [
                (abs(A - M), A)
                for A in answers
            ]
            # print(f'raw: {differences=}')
            differences.sort()
            # print(f'sort:{differences=}')
            minDiffPair = differences[0]
            (diff, minDifference) = minDiffPair
            return (nodeSum, minDifference)

        # sums = all_possible_subtree_sums(root)
        # print(f'{sums=}')
        totalSum = sum_of_tree(root)
        M = totalSum / 2
        (totalSumAgain, nearestTotal) = sum_and_subtree_sum_nearest_M(root, M)
        print(f'found ({totalSumAgain=}, {nearestTotal=})')
        assert totalSum == totalSumAgain
        otherBranch = totalSum - nearestTotal
        answer = nearestTotal * otherBranch
        mod = 10 ** 9 + 7
        answerMod = answer % mod
        print(f'   {answer=}\n{answerMod=}')

        return answerMod

# NOTE: Acceptance Rate 48.3% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 104 ms Beats 15.21%
# NOTE: Memory 50.88 MB Beats 5.32%
