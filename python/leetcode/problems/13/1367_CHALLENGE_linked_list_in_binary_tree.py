# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def checkListToTree(node: ListNode, tree: TreeNode, depth=0) -> bool:
            margin = ".." * depth
            N = node.val if node else '-'
            T = tree.val if tree else '-'
            # print(f'{margin}checkList({N},{T},{depth})')
            if not node:
                # print(f'{margin}  YES: no node')
                return True
            elif not tree:
                # print(f'{margin}  NO: no tree')
                return False
            elif node.val != tree.val:
                # print(f'{margin}  NO: {N} != {T}')
                return False

            # print(f'{margin}checkList({N},{T},{depth})')
            # print(f'{margin}  maybe: check sublist to subtrees')
            return (
                (
                    checkListToTree(node.next, tree.left, depth+1)
                ) or (
                    checkListToTree(node.next, tree.right, depth+1)
                )
            )
            raise Exception('should be impossible to get here')
        
        def checkEverywhere(node: ListNode, tree: TreeNode, depth=0) -> bool:
            margin = "  " * depth
            N = node.val if node else '-'
            T = tree.val if tree else '-'
            # print(f'{margin}CE({N},{T},{depth})')
            if not node:
                # print(f'{margin}  YES: no node (should be impossible)')
                return True
            elif not tree:
                # print(f'{margin}  NO: no tree')
                return False
            elif node.val == tree.val:
                if checkListToTree(node, tree, depth+1):
                    # print(f'{margin}  YES: tree matches node')
                    return True
            # print(f'{margin}CE({N},{T},{depth})')
            # print(f'{margin}  maybe: check subtrees')
            return (
                (
                    checkEverywhere(node, tree.left, depth+1)
                ) or (
                    checkEverywhere(node, tree.right, depth+1)
                )
            )
            raise Exception('should be impossible to get here')

        return checkEverywhere(head, root)

# NOTE: Strangely, this worked, even though I felt like I was
#       writing a very similar program to the failing one.
# NOTE: Runtime 82 ms Beats 27.41%
# NOTE: Memory 20.12 MB Beats 12.21%
