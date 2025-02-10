# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # SHORTCUT: As we often do in these programs,
        # we will fetch the data out of the linked list,
        # perform our transformation on the data array,
        # and put the transformed data back into the linked list.

        node = head
        data = []
        while node:
            data.append(node.val)
            node = node.next
        # print(f'{data=}')

        groups = []
        group_size = 1
        while data:
            this_group = data[:group_size]
            data = data[group_size:]
            groups.append(this_group)
            group_size += 1
        # print(f'{groups=}')

        for i in range(len(groups)):
            G = groups[i]
            if len(G) % 2 == 0:
                G = tuple(reversed(G))
                groups[i] = G
        # print(f'{groups=}')

        data = [
            value
            for group in groups
            for value in group
        ]
        # print(f'{data=}')

        node = head
        for value in data:
            node.val = value
            node = node.next

        return head

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Time Limit Exceeded)
# NOTE: Runtime 700 ms Beats 5.49%
# NOTE: Memory 41.71 MB Beats 7.64%
