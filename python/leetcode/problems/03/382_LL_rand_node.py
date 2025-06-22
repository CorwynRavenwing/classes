# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.values = []
        while head:
            self.values.append(head.val)
            head = head.next
        self.len = len(self.values)
        return

    def getRandom(self) -> int:
        index = randint(0, self.len - 1)
        return self.values[index]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# NOTE: Acceptance Rate 64.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 15 ms Beats 64.29%
# NOTE: Memory 20.56 MB Beats 31.36%
