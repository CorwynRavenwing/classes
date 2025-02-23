# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def ListNodeToList(l1: ListNode) -> List[int]:
            answer = []
            lp = l1
            while lp:
                answer.append(lp.val)
                lp = lp.next
            return tuple(answer)
        
        forward = ListNodeToList(head)
        backward = tuple(reversed(forward))
        print(f'{ forward=}')
        print(f'{backward=}')

        twin_sums = tuple(map(sum, zip(forward, backward)))
        print(f'{twin_sums=}')

        return max(twin_sums)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 194 ms Beats 5.02%
# NOTE: Memory 47.72 MB Beats 26.51%
