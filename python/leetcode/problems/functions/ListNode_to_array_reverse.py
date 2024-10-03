
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

