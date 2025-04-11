<pre># Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -&gt; 
Optional[ListNode]:
        
        def length(head: ListNode) -&gt; int:
            answer = 0
            node = head
            while node:
                answer += 1
                node = node.next
            return answer
        
        len_A = length(headA)
        len_B = length(headB)
        print(f'{len_A=}')
        print(f'{len_B=}')

        diff = len_A - len_B
        if diff &gt; 0:
            while diff:
                print(f'Skip A {diff}')
                headA = headA.next
                diff -= 1
        else:
            diff = -diff
            while diff:
                print(f'Skip B {diff}')
                headB = headB.next
                diff -= 1
        
        print()

        while headA and headB:
            if headA == headB:
                print(f'FOUND {headA.val}')
                return headA
            elif headA.val == headB.val:
                print(f'WRONG {headA.val}')
            else:
                print(f'DIFF  {headA.val}/{headB.val}')
            headA = headA.next
            headB = headB.next

        return None

# NOTE: Accepted on second Run (logic error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 89 ms Beats 35.98%
# NOTE: Memory 27.94 MB Beats 33.03%</pre>