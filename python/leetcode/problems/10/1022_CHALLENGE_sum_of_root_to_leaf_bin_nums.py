# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        index = 0
        def uniq_index() -> int:
            nonlocal index
            index += 1
            return index

        def all_numbers_starting_at(node: TreeNode, pathSum: int) -> List[int]:
            index = uniq_index()
            if node is None:
                return []

            pathSum *= 2

            print(f'[{index}] {pathSum}+{node.val}: ?')

            if node.left is None and node.right is None:
                print(f'[{index}] {pathSum}+{node.val}: leaf node');
                return [pathSum + node.val]

            pathSum += node.val

            answers = (
                []
                + all_numbers_starting_at(node.left, pathSum)
                + all_numbers_starting_at(node.right, pathSum)
            )
            print(f'[{index}] {pathSum}+{node.val}: {answers}')
            return answers

        answers = all_numbers_starting_at(root, 0)
        print(f'ALL: {answers}')

        return sum(answers)

# NOTE: Acceptance Rate 74.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 2.86%
# NOTE: Memory 19.72 MB Beats 7.49%
