# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def show_ListNode(label: str, node: ListNode):
            S = f'{label}: {node}'
            S = S.replace('ListNode{val: ', 'ListNode{')
            S = S.replace('next: ListNode{', '')
            S = S.replace('next: None', 'EOL')
            while '}}' in S:
                S = S.replace('}}', '}')
            print(S)

        show_ListNode('start  : l1', l1)
        show_ListNode('start  : l2', l2)
        s1 = l1
        s2 = l2
        while s1 and s2:
            if s1.next or s2.next:
                # if either list has a "next", they both must, with value 0
                if not s1.next:
                    s1.next = ListNode(0)
                if not s2.next:
                    s2.next = ListNode(0)
                show_ListNode('stretch: l1', l1)
                show_ListNode('stretch: l2', l2)
            s1.val += s2.val
            s2.val -= s2.val
            show_ListNode('add    : l1', l1)
            show_ListNode('add    : l2', l2)
            s1 = s1.next
            s2 = s2.next

        s1 = l1
        while s1:
            if s1.val > 9:
                show_ListNode('val > 9: l1', l1)
                if not s1.next:
                    s1.next = ListNode(0)
                    show_ListNode('stretch: l1', l1)
                carry = s1.val // 10
                print(f'  {carry=}')
                s1.next.val += carry
                s1.val -= carry*10
                show_ListNode('carry  : l1', l1)
            s1 = s1.next
            
        return l1

# NOTE: A version that is much more in keeping with what
#       the problem-setter had in mind.
# NOTE: Accepted on first Submit
# NOTE: Runtime 820 ms Beats 5.44%
# NOTE: Memory 16.64 MB Beats 32.97%
