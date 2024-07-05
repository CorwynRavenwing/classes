# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        numbers = []
        node = head
        while node:
            numbers.append(node.val)
            node = node.next
        # print(f'{numbers=}')
        for i in range(1, len(numbers)):
            if numbers[i] and numbers[i - 1]:
                numbers[i] += numbers[i - 1]
                numbers[i - 1] = 0
                # print(f'{numbers=}')
        nonzeros = [
            N
            for N in numbers
            if N
        ]
        # print(f'{nonzeros=}')
        node = None
        # print(f'> {node=}')
        for N in reversed(nonzeros):
            node = ListNode(N, node)
            # print(f'{N} {node=}')
        
        return node

