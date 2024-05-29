# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        value = None
        while head and head.next and head.val == head.next.val:
            value = head.val
            while head and head.val == value:
                print(f'del {value} from head')
                head = head.next
        P = head
        while P:
            while (
                    (
                        (P and P.next and P.next.next)
                    ) and (
                        (P.next.val == P.next.next.val)
                    )
                ):
                value = P.next.val
                while P.next and P.next.val == value:
                    print(f'del {value} from P.next')
                    P.next = P.next.next
            P = P.next
        return head

