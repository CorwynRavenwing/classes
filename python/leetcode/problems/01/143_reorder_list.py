# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # SHORTCUT: since doing this is ridiculous, we'll solve it
        # in a ridiculous fashion:
        listify = []
        node = head
        while node:
            listify.append(node)
            node = node.next
        L = len(listify)
        center = L // 2 + L % 2     # 3 and 4 -> 2; 5 and 6 -> 3
        evenList = listify[:center]
        oddList = listify[center:]

        Z = evenList[-1]    # record last even node
        for (A, B) in pairwise(evenList):
            C = oddList.pop(-1)
            A.next = C
            C.next = B
            B.next = None
        if oddList:
            C = oddList.pop(-1)
            Z.next = C
            C.next = None
        return

# NOTE: Accepted on first Submit
# NOTE: Runtime 51 ms Beats 81.47%
# NOTE: Memory 25.19 MB Beats 6.41%
