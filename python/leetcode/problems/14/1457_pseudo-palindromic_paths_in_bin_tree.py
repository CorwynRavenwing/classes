# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def PPP(node: TreeNode, bitMask=0) -> int:
            if not node:
                return 0
            
            # always do this, whether interior or leaf
            bitMask ^= (1 << node.val)

            if node.left or node.right:
                # INTERIOR NODE
                print(f'interior node {node.val}:')
                return sum([
                    PPP(node.left, bitMask),
                    PPP(node.right, bitMask),
                ])
            else:
                # LEAF NODE
                binary = f'{bitMask:b}'
                bits = list(binary)
                if '1' in bits:
                    bits.remove('1')                # a single 1 is removed
                answer_bool = ('1' not in bits)     # no other 1 exists
                answer_int = (1 if answer_bool else 0)
                print(f'  leaf node {node.val}: {bitMask} {binary} {bits} {answer_bool} {answer_int}')
                return answer_int
        
        return PPP(root)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case with no 1's)
# NOTE: Runtime 471 ms Beats 5.04%
# NOTE: Memory 51.43 MB Beats 10.30%
