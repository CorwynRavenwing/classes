# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # def show_TreeNode(self, label: str, node: TreeNode):
    #     S = f'{label}{node}'
    #     S = S.replace('TreeNode{val: ', 'Tree{')
    #     S = S.replace(', left: Tree{', ' L:{')
    #     S = S.replace(', right: Tree{', ' R:{')
    #     S = S.replace(', left: None', ' L:-')
    #     S = S.replace(', right: None', ' R:-')
    #     S = S.replace(' L:- R:-}', '}')
    #     print(S)

    def add_leftmost_path(self, node: TreeNode):
        pass
        while node:
            if node.left:
                direction = 'L'
            else:
                direction = '*'
            self.path.append((node, direction))
            node = node.left
        return
    
    def show_path(self, label: str):
        # print(f'\n===== {label} =====')
        # for P in self.path:
        #     self.show_TreeNode('P=', P)
        return

    def __init__(self, root: Optional[TreeNode]):
        # there is actually no need whatsoever for a "pointer" to the
        # current value.  What we need instead, is a pointer to the
        # NEXT value, if it exists, and a way to advance it to the
        # following value.
        self.path = []
        # initial "next" is the farthest-left value:
        self.add_leftmost_path(root)
        self.show_path('INIT')
        return

    def next(self) -> int:
        (answerNode, direction) = self.path[-1]
        assert direction == '*'
        answer = answerNode.val
        if answerNode.right:
            self.path[-1] = (answerNode, 'R')
            self.add_leftmost_path(answerNode.right)
        else:
            ignore = self.path.pop()
            while self.path:
                (pathNode, direction) = self.path[-1]
                if direction == 'L':
                    self.path[-1] = (pathNode, '*')
                    break
                elif direction == '*':
                    if pathNode.right:
                        self.path[-1] = (pathNode, 'R')
                        self.add_leftmost_path(pathNode.right)
                        break
                    else:
                        ignore = self.path.pop()
                        continue
                elif direction == 'R':
                    ignore = self.path.pop()
                    continue
        self.show_path('NEXT')
        return answer

    def hasNext(self) -> bool:
        return len(self.path)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# NOTE: Runtime 61 ms Beats 41.66%
# NOTE: Memory 22.68 MB Beats 5.31%
