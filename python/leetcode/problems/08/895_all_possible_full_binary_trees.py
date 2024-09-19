# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # we borrow some code from #95:

    @cache
    def genTrees(self, nums: List[int]) -> List[Optional[TreeNode]]:

        print(f'genTrees({nums})')

        if len(nums) == 0:
            return [None]           # a list containing one, null, treenode
        if len(nums) == 1:
            N = nums[0]
            return [TreeNode(N)]    # a list containing one treenode, value N
        if len(nums) % 2 == 0:
            return []               # a list of no treenodes
            # (even numbers are not full trees)

        def showTree(label: str, node: TreeNode) -> None:
            S = f'{label}{node}'
            S = S.replace('TreeNode{val: ', 'Tree{')
            S = S.replace(' left: ', ' L:')
            S = S.replace(' right: ', ' R:')
            S = S.replace('L:Tree{', 'L:{')
            S = S.replace('R:Tree{', 'R:{')
            S = S.replace(', L:None', '')
            S = S.replace(', R:None', '')
            print(f'{S}')

        answer = []
        print(f'{len(answer)=}')
        for index, center in enumerate(nums):
            # with each possible number as the root:
            if index % 2 == 0:
                print(f'  {index}: SKIP non-full tree')
                continue
            left = nums[:index]
            right = nums[index + 1:]
            print(f'  {index}: {center=} {left=} {right=}')
            priorLeft = self.genTrees(left)
            priorRight = self.genTrees(right)
            showTree('   priorLeft=', priorLeft)
            showTree('  priorRight=', priorRight)
            answer.extend([
                TreeNode(center, L, R)
                for L in priorLeft
                for R in priorRight
            ])
            print(f'{len(answer)=}')
            # each possible left group crossed with each possible right group

        return answer

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        nums = (0,) * n

        return self.genTrees(nums)

# NOTE: Re-used most of the prior version
# NOTE: Accepted on first Submit
# NOTE: Runtime 342 ms Beats 5.06%
# NOTE: Memory 20.60 MB Beats 38.81%
