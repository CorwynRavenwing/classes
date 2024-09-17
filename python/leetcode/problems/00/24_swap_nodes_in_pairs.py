# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(404, head)  # fictional new head
        N = head
        while N and N.next and N.next.next:
            # this was checking if N, A, and B exist: C may be None.
            print(f'{head=}')
            # N -> A -> B -> C
            A = N.next
            B = A.next
            C = B.next
            # N -> B -> A -> C
            N.next = B
            B.next = A
            A.next = C
            #           N -> C
            N = A
        print(f'{head=}')
        head = head.next    # remove fictional head
        return head

# NOTE: Accepted on first Submit
# NOTE: Runtime 149 ms Beats 5.31%
# NOTE: Memory 16.70 MB Beats 18.57%
