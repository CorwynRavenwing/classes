# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def list_depth() -> int:
            P = head
            D = 0
            while P:
                P = P.next
                D += 1
            return D
        
        def nth_node(N: int) -> Optional[ListNode]:
            print(f'nth_node({N}):')
            P = head
            for _ in range(N):
                print(f'  {_}')
                P = P.next
            return P
        
        depth = list_depth()
        print(f'{depth=}')

        if depth == 0:
            return head

        k %= depth
        print(f'% {k=}')

        if k == 0:
            return head
        
        last_node_num = depth - 1
        new_end = nth_node(last_node_num - k)
        new_head = nth_node(last_node_num - k + 1)
        old_end = nth_node(last_node_num)

        assert old_end.next is None
        old_end.next = head
        
        assert new_head == new_end.next
        new_end.next = None

        assert new_head is not None
        head = new_head

        return head

