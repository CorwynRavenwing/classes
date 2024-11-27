# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        node = list1
        i = 0
        while i < a - 1:
            # stop one early so we have the prior node
            print(f'{a=}: skip {i} {node.val if node else None}')
            i += 1
            node = node.next
        list1_before_removal = node
        print(f'{a=}: found {i} {node.val if node else None}')

        while i < b + 1:
            print(f'{b=}: skip {i} {node.val if node else None}')
            # start from node (a - 1) above
            # stop one late so we have the prior node
            i += 1
            node = node.next
        list1_after_removal = node
        print(f'{b=}: found {i} {node.val if node else None}')

        node = list2
        while node and node.next:
            # skip to the end of list2
            node = node.next
        list2_last_node = node

        list1_before_removal.next = list2
        list2_last_node.next = list1_after_removal

        return list1

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 272 ms Beats 5.15%
# NOTE: Memory 21.63 MB Beats 7.84%
