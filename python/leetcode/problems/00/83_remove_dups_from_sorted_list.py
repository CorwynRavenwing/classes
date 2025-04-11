<pre># Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -&gt; Optional[ListNode]:
        
        fake_head = ListNode(99999, head)

        node = fake_head
        while node and node.next and node.next.next:
            if node.next.val == node.next.next.val:
                print(f'DEL  {node.next.val}')
                node.next = node.next.next
            else:
                print(f'KEEP {node.next.val}')
                node = node.next

        head = fake_head.next
        return head


# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 5 ms Beats 2.74%
# NOTE: Memory 17.86 MB Beats 40.14%</pre>