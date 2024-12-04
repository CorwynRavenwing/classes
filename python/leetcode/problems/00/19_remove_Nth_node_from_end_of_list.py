# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def show(node: Optional[ListNode]) -> str:
            return f"{node.val if node else None}"
        print(f"start: {show(head)}")

        front_ptr = head
        for i in range(n):
            # length of list is constrained to be >= n
            front_ptr = front_ptr.next
            print(f"moving front ptr by {n}: {show(front_ptr)}")
        
        if not front_ptr:
            print(f'at end of list: truncate head.  {show(head)} {show(head.next)}')
            head = head.next
            return head
        else:
            front_ptr = front_ptr.next
            print(f"moving front ptr by 1 more: {show(front_ptr)}")

        back_ptr = head
        print(f"added back_ptr: {show(front_ptr)} {show(back_ptr)}")

        while front_ptr:
            front_ptr = front_ptr.next
            back_ptr = back_ptr.next
            print(f"moving front_ptr to end: {show(front_ptr)} {show(back_ptr)}")
        
        print(f"back_ptr: {show(back_ptr)}")
        if back_ptr and back_ptr.next:
            back_ptr.next = back_ptr.next.next
        else:
            print("back_ptr or back_ptr.next is null here")
        # or should this be just "= front_ptr" ?

        return head

# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.58 MB Beats 5.22%
