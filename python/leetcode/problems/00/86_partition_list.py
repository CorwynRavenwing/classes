# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        def showNode(label: str, node: ListNode) -> None:
            S = f'{label}={node}'
            S = S.replace('ListNode{val: ', '{')
            S = S.replace(', next: {', ', ')
            S = S.replace(', next: None}', '}')
            while '}}' in S:
                S = S.replace('}}', '}')
            print(f'{S}')

        fake_head = ListNode(369, head)     # add new, fictional node before "head"
        LT_head = ListNode(404)
        GE_head = ListNode(420)
        node = fake_head
        LT = LT_head
        GE = GE_head
        while node and node.next:
            print(f'{node.next.val=}')
            showNode(' H', fake_head)
            showNode('LT', LT_head)
            showNode('GE', GE_head)
            if node.next.val < x:
                LT.next = node.next         # add node to LT list
                node.next = node.next.next  # skip past node we've moved
                LT = LT.next                # increment LT to end
                LT.next = None              # make this the end of LT list
                # showNode(' H', fake_head)
                # showNode('LT', LT_head)
            else:
                GE.next = node.next         # add node to GE list
                node.next = node.next.next  # skip past node we've moved
                GE = GE.next                # increment GE to end
                GE.next = None              # make this the end of GE list
                # showNode(' H', fake_head)
                # showNode('GE', GE_head)

        showNode(' H', fake_head)
        showNode('LT', LT_head)
        showNode('GE', GE_head)

        LT.next = GE_head.next   # link end of LT to beginning of GE
        GE_head.next = None      # make this the end of the GE list

        showNode(' H', fake_head)
        showNode('LT', LT_head)
        showNode('GE', GE_head)

        head = LT_head.next     # link answer to beginning of LT
        return head

# NOTE: Runtime 776 ms Beats 5.83%
# NOTE: Memory 16.77 MB Beats 35.83%
