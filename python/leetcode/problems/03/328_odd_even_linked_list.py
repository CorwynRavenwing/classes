# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def show_ListNode(label: str, node: ListNode):
            S = f'{label}: {node}'
            S = S.replace('ListNode{val: ', 'ListNode{')
            S = S.replace('next: ListNode{', '')
            S = S.replace('next: None', 'EOL')
            while '}}' in S:
                S = S.replace('}}', '}')
            print(S)

        def moveItem(fromNode: ListNode, toNode: ListNode) -> ListNode:
            if not fromNode:
                print(f'Error: fromNode is null')
                return toNode
            if not toNode:
                print(f'Error: toNode is null')
                return toNode
            node = fromNode.next
            if not node:
                print(f'Nothing to move')
                return toNode
            print(f'Move {node.val} after {toNode.val}')
            fromNode.next = node.next
            toNode.next = node
            node.next = None
            return node

        newHead = ListNode(999, head)
        oddHead = ListNode(111, None)
        evenHead = ListNode(222, None)

        odd = oddHead
        even = evenHead
        # show_ListNode('head', newHead)
        # show_ListNode('odd ', oddHead)
        # show_ListNode('even', evenHead)
        while newHead.next:
            odd = moveItem(newHead, odd)
            even = moveItem(newHead, even)
            # show_ListNode('head', newHead)
            # show_ListNode('odd ', oddHead)
            # show_ListNode('even', evenHead)
        
        # show_ListNode('.odd ', odd)
        # show_ListNode('.even', even)

        odd.next = evenHead.next

        # show_ListNode('head', newHead)
        # show_ListNode('odd ', oddHead)
        # show_ListNode('even', evenHead)

        return oddHead.next

# NOTE: Accepted on first Submit
# NOTE: Runtime 40 ms Beats 55.45%
# NOTE: Memory 18.52 MB Beats 41.81%
