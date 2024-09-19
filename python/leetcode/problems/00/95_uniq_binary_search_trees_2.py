# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def genTrees(self, nums: List[int]) -> List[Optional[TreeNode]]:
        
        # we borrow some code from #96:

        print(f'genTrees({nums})')

        if len(nums) == 0:
            return [None]           # a list containing one, null, treenode
        if len(nums) == 1:
            N = nums[0]
            return [TreeNode(N)]    # a list containing one treenode, value N
        
        answer = []
        print(f'{len(answer)=}')
        for index, center in enumerate(nums):
            # with each possible number as the root:
            left = nums[:index]
            right = nums[index + 1:]
            print(f'  {center=} {left=} {right=}')
            priorLeft = self.genTrees(left)
            priorRight = self.genTrees(right)
            print(f'  {priorLeft=} {priorRight=}')
            answer.extend([
                TreeNode(center, L, R)
                for L in priorLeft
                for R in priorRight
            ])
            print(f'{len(answer)=}')
            # each possible left group crossed with each possible right group
        
        return answer

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        return self.genTrees(tuple(range(1, n+1)))

# NOTE: Re-used most of the code from Version 1
# NOTE: Accepted on first Submit
# NOTE: Runtime 61 ms Beats 5.14%
# NOTE: Memory 17.60 MB Beats 65.49%
