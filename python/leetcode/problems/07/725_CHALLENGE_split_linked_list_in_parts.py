# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        def length_of_linked_list(node: ListNode) -> int:
            L = 0
            while node:
                L += 1
                node = node.next
            return L
        
        def snip_x_nodes(node: ListNode, X: int) -> ListNode:
            buffer = f'snip_x_nodes({node},{X})'
            buffer = buffer.replace('ListNode{val: ', '{')
            buffer = buffer.replace(', next: {', ', ')
            buffer = buffer.replace(', next: None', ', None')
            while '}}' in buffer:
                buffer = buffer.replace('}}', '}')
            print(buffer)
            for i in range(X - 1):
                node = node.next if node else None
            if node:
                answer = node.next
                node.next = None
            else:
                answer = None
            return answer
        
        Length = length_of_linked_list(head)
        groups = Length // k
        print(f'{Length=} {groups=}')

        answer = []
        for i in range(k):
            answer.append(head)
            X = groups + (1 if (i < (Length % k)) else 0)
            old_head = head
            head = snip_x_nodes(head, X)
            print(f'  snipped {length_of_linked_list(old_head)}')
        
        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 1110 ms Beats 7.07%
# NOTE: Memory 17.65 MB Beats 22.72%
