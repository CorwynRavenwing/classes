# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # we borrow some code from #147:
    # ... but Insertion Sort is too slow, so instead we use Merge Sort
    
    def show_ListNode(self, label: str, node: ListNode):
        S = f'{label}: {node}'
        S = S.replace('ListNode{val: ', 'ListNode{')
        S = S.replace('next: ListNode{', '')
        S = S.replace('next: None', 'EOL')
        while '}}' in S:
            S = S.replace('}}', '}')
        print(S)

    # assert list A and list B are already internally sorted
    def mergeLists(self, A: ListNode, B: ListNode) -> ListNode:
        if not A:
            return B
        if not B:
            return A
        
        preA = ListNode(100, A)
        preB = ListNode(200, B)
        nodeA = preA
        while nodeA and preB.next:
            # self.show_ListNode('preA', preA)
            # self.show_ListNode('preB', preB)
            # nodeA_val = (nodeA.val if nodeA else 'NULL')
            # nodeA_next_val = (nodeA.next.val if nodeA.next else 'EOL')
            # nodeB_val = (preB.next.val if preB.next else 'EOL')
            # print(f'  Trying {nodeB_val}, node:{nodeA_val} / next:{nodeA_next_val}')
            
            if not nodeA.next:
                # print(f'    Insert list B at EOL')
                B = preB.next
                nodeA.next = B
                # self.show_ListNode('preA', preA)
                # self.show_ListNode('preB', preB)
                return preA.next

            if preB.next.val <= nodeA.next.val:
                # print(f'    Insert B before node.next')
                B = preB.next       # record first real mamber of list B
                preB.next = B.next  # skip past node B
                B.next = nodeA.next # insert B before A.next ...
                nodeA.next = B      # ... and after A

            nodeA = nodeA.next
        
        # print(f'Ran out of list B')
        # self.show_ListNode('preA', preA)
        # self.show_ListNode('preB', preB)
        return preA.next

    def splitList(self, head: ListNode) -> Tuple[ListNode,ListNode]:

        if head and not head.next:
            # only one member in list
            return (head, None)

        preA = ListNode()
        preB = ListNode()
        node = head
        index = 0
        while node:
            # self.show_ListNode('preA', preA)
            # self.show_ListNode('preB', preB)
            # self.show_ListNode('node', node)
            N = node
            node = node.next
            if index % 2 == 0:
                # print(f'{index=} even: add to List A')
                N.next = preA.next
                preA.next = N
            else:
                # print(f'{index=} odd : add to List B')
                N.next = preB.next
                preB.next = N
            index += 1
        A = preA.next
        B = preB.next
        return (A, B)

    def mergeSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # self.show_ListNode('MSL() head', head)
        if not head:
            return head
        
        (A, B) = self.splitList(head)
        # self.show_ListNode('MSL() A split', A)
        # self.show_ListNode('MSL() B split', B)
        if not B:
            return A

        A = self.mergeSortList(A)
        B = self.mergeSortList(B)
        # self.show_ListNode('MSL() A merge', A)
        # self.show_ListNode('MSL() B merge', B)

        return self.mergeLists(A, B)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSortList(head)

# NOTE: Accepted on first Submit
# NOTE: Runtime 629 ms Beats 5.02%
# NOTE: Memory 32.70 MB Beats 23.90%
