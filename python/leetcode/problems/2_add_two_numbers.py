# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def ListNodeToList(l1: ListNode) -> List[int]:
            answer = []
            lp = l1
            while lp:
                answer.append(lp.val)
                lp = lp.next
            return answer

        def ListToListNode(s1: List[int]) -> ListNode:
            answer = None
            while s1:
                val = s1.pop()
                answer = ListNode(val, answer)

            return answer

        s1 = ListNodeToList(l1)
        s2 = ListNodeToList(l2)
        while len(s1) < len(s2):
            s1 += [0]
        while len(s2) < len(s1):
            s2 += [0]
        print(f"#{s1=}\n#{s2=}")
        sz = list(zip(s1, s2))
        print(f"#{sz=}")
        ss = list(map(sum, sz))
        while max(ss) > 9:
            print(f"#{ss=}")
            if ss[-1] > 9:
                ss += [0]
                continue
            index = ss.index(max(ss))
            carry = ss[index] // 10
            ss[index+1] += carry
            ss[index] -= carry*10
        print(f"#{ss=}")

        answer = ListToListNode(ss)
        return answer

