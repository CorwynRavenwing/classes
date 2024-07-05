# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        L = []
        node = head
        while node:
            L.append(node.val)
            node = node.next
        print(f'{L=}')

        Critical = [
            i
            for i, (A, B, C) in enumerate(zip(L, L[1:], L[2:]))
            if (A < B and B > C) or (A > B and B < C)
        ]
        print(f'{Critical=}')
        if not Critical:
            return [-1, -1]
        
        Distances = [
            B - A
            for (A, B) in zip(Critical, Critical[1:])
        ]
        print(f'{Distances=}')
        if not Distances:
            return [-1, -1]

        minDist = min(Distances)
        maxDist = Critical[-1] - Critical[0]
        return [minDist, maxDist]

