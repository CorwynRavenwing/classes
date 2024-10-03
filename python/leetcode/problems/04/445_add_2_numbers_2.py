# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # we borrow some code from problem #2:
        
        def show_ListNode(label: str, node: ListNode):
            S = f'{label}: {node}'
            S = S.replace('ListNode{val: ', 'ListNode{')
            S = S.replace('next: ListNode{', '')
            S = S.replace('next: None', 'EOL')
            while '}}' in S:
                S = S.replace('}}', '}')
            print(S)

        def length_ListNode(node: ListNode) -> int:
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        # make them the same length by adding leading zeros:
        show_ListNode('start  : l1', l1)
        show_ListNode('start  : l2', l2)
        d1 = length_ListNode(l1)
        d2 = length_ListNode(l2)
        while d1 < d2:
            l1 = ListNode(0, l1)
            d1 += 1
            show_ListNode('stretch : l1', l1)
            show_ListNode('stretch : l2', l2)
        while d2 < d1:
            l2 = ListNode(0, l2)
            d2 += 1
            show_ListNode('stretch : l1', l1)
            show_ListNode('stretch : l2', l2)
        d1 = length_ListNode(l1)
        d2 = length_ListNode(l2)
        assert d1 == d2

        # add without carrying:
        s1 = l1
        s2 = l2
        while s1 and s2:
            s1.val += s2.val
            s2.val -= s2.val
            s1 = s1.next
            s2 = s2.next
            show_ListNode('add    : l1', l1)
            show_ListNode('add    : l2', l2)

        # carry
        show_ListNode('carry  : l1', l1)
        changes = True
        while changes:
            # loop until we run out of carrying to do
            # NOTE: with a doubly-linked list, we could do this
            #       from Right to Left, once, instead of looping
            changes = False
            if l1.val > 9:
                # add leading zero if first digit needs to carry
                l1 = ListNode(0, l1)
                show_ListNode('stretch: l1', l1)
                changes = True
            s1 = l1
            while s1 and s1.next:
                if s1.next.val > 9:
                    carry = s1.next.val // 10
                    # print(f'  {carry=}')
                    s1.val += carry
                    s1.next.val -= carry*10
                    show_ListNode('carry  : l1', l1)
                    changes = True
                s1 = s1.next
            
        return l1

# NOTE: re-used all of prior version with a few changes
# NOTE: used follow-up rule of "don't just reverse the lists"
# NOTE: Accepted on first Submit
# NOTE: Runtime 566 ms Beats 6.01%
# NOTE: Memory 16.76 MB Beats 8.30%
