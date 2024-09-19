# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # assume we can hash a ListNode: if so, this becomes pretty easy.
        # otherwise we have to get much more clever.

        seen = set()
        node = head
        while node:
            if node in seen:
                return True
            else:
                seen.add(node)
            node = node.next
        return False

# NOTE: Accepted on first Submit
# NOTE: Runtime 48 ms Beats 37.76%
# NOTE: Memory 19.56 MB Beats 14.36%
