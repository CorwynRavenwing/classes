# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        delete_me = set(nums)

        head = ListNode(None, head)     # trivialize deleting head node
        node = head
        # print(f'New head, {head.val=}')
        while node and node.next:
            # print(f'  {node.next.val=}')
            if node.next.val in delete_me:
                # print(f'    Delete')
                node.next = node.next.next
                # stay on this node and re-check new "next" node
            else:
                # print(f'    Keep')
                node = node.next
                # move to next node
        
        head = head.next                # get rid of helper front node
        return head

# NOTE: Runtime 726 ms Beats 47.98%
# NOTE: Memory 54.37 MB Beats 98.22%
