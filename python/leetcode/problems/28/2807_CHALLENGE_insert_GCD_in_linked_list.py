# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Euclidian Algorithm for GCD, as described in Wikipedia
        def GCD(A: int, B: int) -> int:
            # print(f'GCD({A},{B})')
            if B == 0:
                return A
            else:
                return GCD(B, A % B)

        node = head
        while node and (nextNode := node.next):
            A = node.val
            B = nextNode.val
            C = GCD(A, B)
            print(f'Insert GCD {C} between {A},{B}')
            gcdNode = ListNode(C, nextNode)
            node.next = gcdNode
            node = nextNode

        return head

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 84 ms Beats 21.60%
# NOTE: Memory 19.79 MB Beats 10.35%
