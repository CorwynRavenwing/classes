# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        fakeHead = ListNode(9999, head)

        # we borrow some code from #19:
        
        def show(node: Optional[ListNode]) -> str:
            return f"{node.val if node else None}"
        
        print(f"start: {show(head)}")

        front_ptr = fakeHead
        for i in range(k - 1):
            front_ptr = front_ptr.next
            # print(f"moving front ptr by {i + 1}/{k - 1}: {show(front_ptr)}")
        
        before_A = front_ptr
        print(f'Got before_A={show(before_A)}')

        for i in range(k - 1, k + 1):
            front_ptr = front_ptr.next
            # print(f"moving front ptr by {i + 1}/{k + 1}: {show(front_ptr)}")

        back_ptr = fakeHead
        print(f"added back_ptr: {show(front_ptr)} {show(back_ptr)}")

        while front_ptr:
            front_ptr = front_ptr.next
            back_ptr = back_ptr.next
            # print(f"moving front_ptr to end: {show(front_ptr)} {show(back_ptr)}")

        print(f"back_ptr: {show(back_ptr)}")

        before_B = back_ptr
        print(f'Got before_B={show(before_B)}')

        A = before_A.next
        after_A = A.next
        B = before_B.next
        after_B = B.next

        print(f'A: {show(before_A)} {show(A)} {show(after_A)}')
        print(f'B: {show(before_B)} {show(B)} {show(after_B)}')

        if A == B:
            # change nothing
            pass
        elif A == before_B:
            # X A B Y -> X B A Y
            before_A.next = B
            B.next = A
            A.next = after_B
        elif B == before_A:
            # X B A Y -> X A B Y
            before_B.next = A
            A.next = B
            B.next = after_A
        else:
            # X A Y P B Q -> X B Y P A Q
            before_A.next = B
            B.next = after_A
            before_B.next = A
            A.next = after_B
        
        head = fakeHead.next
        del fakeHead

        return head

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 34 ms Beats 75.17%
# NOTE: Memory 40.03 MB Beats 28.08%
