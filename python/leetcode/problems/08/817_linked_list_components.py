# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        node = head
        answer = 0
        in_a_component = False
        while node:
            node_matches = (node.val in nums)
            if node_matches and not in_a_component:
                answer += 1
            in_a_component = node_matches
            node = node.next
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 827 ms Beats 18.64%
# NOTE: Memory 20.22 MB Beats 81.36%
