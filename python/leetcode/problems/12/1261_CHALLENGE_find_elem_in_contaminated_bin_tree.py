# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def decontaminate(self, node: TreeNode, value: int):
        if not node:
            return
        node.val = value
        self.decontaminate(node.left, value * 2 + 1)
        self.decontaminate(node.right, value * 2 + 2)
        return
    
    def getValues(self, node: TreeNode) -> Set[int]:
        if not node:
            return set()
        Self = {node.val}
        Left = self.getValues(node.left)
        Right = self.getValues(node.right)
        return Self | Left | Right

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        self.decontaminate(root, 0)
        self.values = self.getValues(root)
        # print(f'DEBUG: {root}')
        return

    def find(self, target: int) -> bool:
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 28 ms Beats 16.92%
# NOTE: Memory 22.40 MB Beats 5.54%

# NOTE: re-ran for challenge:
# NOTE: Runtime 23 ms Beats 16.84%
# NOTE: Memory 22.88 MB Beats 10.70%
# NOTE: same memory, 2x better percentage
