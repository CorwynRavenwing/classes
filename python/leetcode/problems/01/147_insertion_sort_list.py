# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertSorted(self, preHead: ListNode, newNode: ListNode) -> int:
        if not preHead:
            raise ValueError(f'Error: insertSorted(): null preHead passed')
        if not newNode:
            raise ValueError(f'Error: insertSorted(): null newNode passed')
        pos = 0
        node = preHead
        while node:
            # node_val = (node.val if node else 'NULL')
            # node_next_val = (node.next.val if node.next else 'EOL')
            # print(f'  Trying {newNode.val=} vs {pos=}, node:{node_val} / next:{node_next_val}')
            if not node.next:
                # print(f'    Insert at EOL')
                newNode.next = None     # new EOL
                node.next = newNode
                return pos
            if newNode.val <= node.next.val:
                # print(f'  Insert before node.next')
                newNode.next = node.next
                node.next = newNode
                return pos
            pos += 1
            node = node.next
        
        raise Exception(f'Error: insertSorted(): node was never inserted')

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # def show_ListNode(label: str, node: ListNode):
        #     S = f'{label}: {node}'
        #     S = S.replace('ListNode{val: ', 'ListNode{')
        #     S = S.replace('next: ListNode{', '')
        #     S = S.replace('next: None', 'EOL')
        #     while '}}' in S:
        #         S = S.replace('}}', '}')
        #     print(S)

        newHead = ListNode(999)    # create fictional node-before-head
        node = head
        while node:
            # show_ListNode('old list', node)
            # show_ListNode('new list', newHead)
            # print(f'Inserting {node.val=}')
            nextNode = node.next
            pos = self.insertSorted(newHead, node)
            print(f'Node {node.val=} inserted at {pos=}')
            node = nextNode
        # show_ListNode('old list', node)
        # show_ListNode('new list', newHead)
        newHead = newHead.next      # delete node-before-head
        # show_ListNode('fix list', newHead)
        return newHead

# NOTE: Runtime 680 ms Beats 11.60%
# NOTE: Memory 18.66 MB Beats 18.39%
