# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # we borrow some code from #141:

        seen = set()
        node = head
        while node:
            if node in seen:
                return node
            else:
                seen.add(node)
            node = node.next
        return None

# NOTE: reused all code from prior version, changing only the
#       return values
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 43 ms Beats 59.53%
# NOTE: Memory 19.65 MB Beats 6.67%
