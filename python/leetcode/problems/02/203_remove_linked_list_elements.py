# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            print(f"DELETE {head.val=}")
            head = head.next
        
        tip = head
        while tip and tip.next:
            print(f"  CHECK {tip.next.val=}")
            while tip.next and tip.next.val == val:
                print(f"    DELETE {tip.next.val=}")
                tip.next = tip.next.next
            tip = tip.next
        # print(f"{head=}")
        return head

