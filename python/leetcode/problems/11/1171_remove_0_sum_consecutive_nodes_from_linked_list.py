# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def show_ListNode(label: str, node: ListNode):
            S = f'{label}: {node}'
            S = S.replace('ListNode{val: ', 'ListNode{')
            S = S.replace('next: ListNode{', '')
            S = S.replace('next: None', 'EOL')
            while '}}' in S:
                S = S.replace('}}', '}')
            print(S)

        dummy = ListNode(10000, head)
        # show_ListNode('init', dummy)
        node = dummy
        while node:
            while node.next and not node.next.val:
                node.next = node.next.next
            node = node.next

        prev = None
        node = dummy
        Sum = 0
        partialSums = {0: dummy}

        print(f'Loop 0 Sum=0')
        while node:
            # show_ListNode('loop', dummy)
            node = node.next
            if not node:
                break
            Sum += node.val
            print(f'Loop {node.val} {Sum=}')
            if Sum not in partialSums:
                partialSums[Sum] = node
            else:
                prev = partialSums[Sum]
                print(f'Delete {prev.next.val} to {node.val}')
                prev.next = node.next
                node = dummy
                Sum = 0
                partialSums = {0: dummy}
                # show_ListNode('  deleted', dummy)
                print(f'  (restart)')
                print(f'Loop 0 Sum=0')
                continue
        
        head = dummy.next
        return head

# NOTE: Accepted on first Submit
# NOTE: Runtime 31 ms Beats 12.61%
# NOTE: Memory 17.10 MB Beats 8.96%
