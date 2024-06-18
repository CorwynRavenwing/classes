# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            (list2, list1) = (list1, list2)
        start = list1
        while list1 and list2:
            if list1.next:
                if list1.next.val > list2.val:
                    new_2 = list2.next
                    list2.next = list1.next
                    list1.next = list2
                    list2 = new_2
                else:
                    list1 = list1.next
            else:
                list1.next = list2
                list2 = None
        return start

