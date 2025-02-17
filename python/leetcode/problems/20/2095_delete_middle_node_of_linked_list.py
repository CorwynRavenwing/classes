# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def show_ListNode(label: str, node: ListNode):
            S = f'{label}: {node}'
            S = S.replace('ListNode{val: ', 'ListNode{')
            S = S.replace('next: ListNode{', '')
            S = S.replace('next: None', 'EOL')
            while '}}' in S:
                S = S.replace('}}', '}')
            print(S)

        fakeHead = ListNode('SOL', head)
        show_ListNode('begin', fakeHead)

        prev = fakeHead
        slow = fakeHead
        fast = fakeHead
        iteration = 0
        while True:
            iteration += 1
            if fast:
                fast = fast.next
                prev = slow
                slow = slow.next
            else:
                break
            if fast:
                fast = fast.next
            # if fast:
            #     fast.val = f'F{iteration}'
            # if slow:
            #     slow.val = f'S{iteration}'
            # if prev:
            #     prev.val = f'P{iteration}'
            # show_ListNode(f'loop {iteration}', fakeHead)

        # if fast:
        #     fast.val = f'F'
        # if slow:
        #     slow.val = f'S'
        # if prev:
        #     prev.val = f'P'
        if prev and prev.next:
            prev.next.val = 'X'
        show_ListNode(f'found', fakeHead)

        if prev and prev.next:
            prev.next = prev.next.next

        show_ListNode(f' done', fakeHead)

        head = fakeHead.next

        return head

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Time Limit Exceeded)
# NOTE: Runtime 60 ms Beats 47.22%
# NOTE: Memory 48.92 MB Beats 47.80%
