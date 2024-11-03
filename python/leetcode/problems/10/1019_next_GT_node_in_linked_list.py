# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        INF = float('+inf')
        NEXT = lambda: stack[-1] if stack else [INF, None]
        NEXT_VAL = lambda: NEXT()[0]
        NEXT_IDX = lambda: NEXT()[1]

        answer_dict = {}
        index = 0
        stack = []
        while head:
            V = head.val
            while NEXT_VAL() < V:
                answer_dict[NEXT_IDX()] = V
                ignore = stack.pop(-1)
            stack.append((V, index))

            index += 1
            head = head.next

        while NEXT_IDX() is not None:
            answer_dict[NEXT_IDX()] = 0
            ignore = stack.pop(-1)
        
        assert None not in answer_dict.values()
        answer_arr = [
            value
            for index, value in sorted(answer_dict.items())
        ]
        keys = tuple(sorted(answer_dict.keys()))
        check = tuple(range(len(answer_dict)))
        assert None not in answer_arr
        assert keys == check

        return answer_arr

# NOTE: Accepted on first Submit
# NOTE: Runtime 111 ms Beats 7.31%
# NOTE: Memory 20.57 MB Beats 42.96%
