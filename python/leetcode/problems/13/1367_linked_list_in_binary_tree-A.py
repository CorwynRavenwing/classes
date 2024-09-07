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

        def showBoth(level: int, label: str, node: TreeNode, head: ListNode) -> None:
            maxSize = 40
            indent = "\t" * level
            s1 = f'{indent}{label}:'
            
            s2 = f'{indent}{node=}'
            s2 = s2.replace('TreeNode{','{')
            s2 = s2.replace('{val: ','{')
            s2 = s2.replace(', left: ',' L:')
            s2 = s2.replace(', right: ',' R:')
            s2 = s2.replace(' L:None','')
            s2 = s2.replace(' R:None','')
            if len(s2) > maxSize:
                s2 = s2[:maxSize]+'...'
            
            s3 = f'{indent}{head=}'
            s3 = s3.replace('ListNode{','{')
            s3 = s3.replace('{val: ','{')
            s3 = s3.replace(', next: ',' -> ')
            if len(s3) > maxSize:
                s3 = s3[:maxSize]+'...'

            print(f'{s1}\n{s2}\n{s3}')

        def checkNode(node: TreeNode, height: int, head: ListNode, length: int) -> bool:
            showBoth(1, f'cn({height},{length})', node, head)
            if length > height:
                print(f'\t\tNO: {length} > {height}')
                return False
            if not head:
                print(f'\t\tYES: {head=}')
                return True
            if not node:
                print(f'\t\tNO: {node=}')
                return False
            if node.val != head.val:
                print(f'\t\tNO: {node.val} != {head.val}')
                return False
            if checkNode(node.left, height - 1, head.next, length - 1):
                return True
            if checkNode(node.right, height - 1, head.next, length - 1):
                return True
            print(f'\t\tNO')
            return False

        def treeHeight(node: TreeNode) -> int:
            if node is None:
                return 0
            return 1 + max(
                treeHeight(node.left),
                treeHeight(node.right),
            )
        
        def listLength(head: ListNode) -> int:
            if head is None:
                return 0
            return 1 + listLength(head.next)

        def checkAllNodes(node: TreeNode, height: int, head: ListNode, length: int) -> bool:
            showBoth(0, f'CAN({height},{length})', node, head)
            if length > height:
                print(f'\tNO: {length} > {height}')
                return False
            if not node:
                print(f'\tNO: {node=}')
                return False
            if node.val == head.val:
                if checkNode(node, height, head, length):
                    return True
            if checkAllNodes(node.left, height - 1, head, length):
                return True
            if checkAllNodes(node.right, height - 1, head, length):
                return True
            return False
        
        TH = treeHeight(root)
        LL = listLength(head)
        return checkAllNodes(root, TH, head, LL)

# NOTE: Time Limit Exceeded for very large testcases
