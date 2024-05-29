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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def NodeListToList(node: Optional[ListNode]) -> List[int]:
            answer = []
            while node:
                answer.append(node.val)
                node = node.next
            return answer

        def ListToBST(arr: List[int]) -> Optional[TreeNode]:
            print(f'BST {arr}:')
            if not arr:
                print(f'  ---')
                return None
            
            index = len(arr) // 2
            leftArr = arr[:index]
            thisValue = arr[index]
            rightArr = arr[index + 1:]
            
            print(f'  {index=} {leftArr} {thisValue} {rightArr}')
            
            leftNode = ListToBST(leftArr) if leftArr else None
            rightNode = ListToBST(rightArr) if rightArr else None

            return TreeNode(thisValue, leftNode, rightNode)
        
        return ListToBST(
            NodeListToList(
                head
            )
        )

