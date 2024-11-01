# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        VAL = lambda x: (alphabet[x.val] if x else '')
        # REV = lambda x: tuple(reversed(tuple(x)))
        # JOIN = lambda x: ''.join(x)

        def smallestFromLeaf_givenStringSoFar(node: TreeNode, so_far: str) -> str:
            if not node:
                return ''
            
            this_value = VAL(node) + so_far     # prepend letter to front

            answers = []
            if node.left:
                answers.append(
                    smallestFromLeaf_givenStringSoFar(node.left, this_value)
                )
            if node.right:
                answers.append(
                    smallestFromLeaf_givenStringSoFar(node.right, this_value)
                )
            return min(
                answers,            # interior node: give best of children
                default=this_value  # a leaf node: give this answer
            )
        
        return smallestFromLeaf_givenStringSoFar(root, '')

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 9 ms Beats 18.75%
# NOTE: Memory 17.99 MB Beats 25.17%
