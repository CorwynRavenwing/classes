# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head
        
        begin_section_1 = head  # (?)

        # add one more node on the beginning,
        # to remove "head/not-head" questions
        head = ListNode(-99, head)

        # go forward to the node *before* the blue section:
        S1_end = head
        for _ in range(left - 1):
            S1_end = S1_end.next
        A = S1_end
        B = A.next
        S2_end = B
        S2 = B

        def show_node(label: str, node: ListNode) -> None:
            text = f'{label} {node}'
            text = text.replace('ListNode{val: ', '{')
            text = text.replace(', next: ', ' ')
            text = text.replace(' None}', '}')
            print(text)
            return

        show_node('check S1', S1_end)
        show_node('check S2', S2)
        show_node('check S2_end', S2_end)

        for _ in range(right - left + 1):
            print(f'loop {_} of {right - left + 1}:')
            B = A.next
            A.next = B.next
            B.next = S2
            S2 = B
            S2_end.next = None
            show_node('check S1', S1_end)
            show_node('check S2', S2)
            show_node('check S2_end', S2_end)

        S2_end.next = S1_end.next
        S1_end.next = S2

        show_node('check S1', S1_end)
        # show_node('check S2', S2)
        # show_node('check S2_end', S2_end)

        # remove extra node from the beginning again
        NP = head
        head = head.next
        del NP

        return head

