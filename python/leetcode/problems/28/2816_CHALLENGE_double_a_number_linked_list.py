# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. double the values in place:
        ptr = head
        while ptr:
            ptr.val *= 2
            ptr = ptr.next
        
        # 2. add a leading zero, temporarily:
        head = ListNode(0, head)

        # 3. perform carries until there are no more to do:
        working = True
        while working:
            working = False
            ptr = head
            while ptr and ptr.next:
                if ptr.next.val >= 10:
                    carry = ptr.next.val // 10
                    print(f"{ptr.val=} {ptr.next.val=} {carry=}")
                    ptr.val += carry
                    ptr.next.val -= carry * 10
                    working = True
                ptr = ptr.next
        

        # 4. remove leading 0 if it's still there:
        if head.val == 0:
            head = head.next
        
        return head

