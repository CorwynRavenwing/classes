# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # print(f'PS({root},{targetSum})')
        
        # we borrow some code from #112:

        if not root:
            return []
        
        targetSum -= root.val
        if not root.left and not root.right:
            # leaf node
            if (targetSum == 0):
                return [[root.val]]
            else:
                return []
        
        answers = [
            self.pathSum(root.left, targetSum),
            self.pathSum(root.right, targetSum),
        ]
        print(f'orig {answers=}')
        answers = [
            [root.val] + A
            for group in answers
            for A in group
            # if A
        ]
        print(f'flat {answers=}')
        return answers

# NOTE: Reused much of the prior version
# NOTE: Runtime 94 ms Beats 5.43%
# NOTE: Memory 17.70 MB Beats 36.77%
