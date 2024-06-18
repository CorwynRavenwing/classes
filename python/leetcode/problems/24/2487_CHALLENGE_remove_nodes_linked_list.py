# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def ListNodeToList(node: ListNode) -> List[int]:
            answer = []
            while node:
                answer.append(node.val)
                node = node.next
            return answer
        
        def MaxToRight(L: List[int]) -> List[int]:
            M = L.copy()
            for i in reversed(range(1, len(L))):
                if M[i-1] < M[i]:
                    M[i-1] = M[i]
            return M

        # def any_larger_after(node: ListNode) -> bool:
        #     if not node:
        #         return False
        #     val = node.val
        #     while node.next:
        #         if node.next.val > val:
        #             print(f"{val} --> {node.next.val}")
        #             return True
        #         node = node.next
        #     # print(f"{val} --> OK")
        #     return False
        
        L = ListNodeToList(head)
        M = MaxToRight(L)
        # print(f"{L=}\n{M=}")
        i = 0

        # while head and any_larger_after(head):
        #     # print(f"delete head {head.val}")
        #     head = head.next
        # while L and L[i] < M[i]:
        while i < len(L) and L[i] < M[i]:
            # print(f"delete head {head.val}")
            # del L[i]
            # del M[i]
            i += 1
            # print(f"{L=}\n{M=}")
            head = head.next
        
        # node = head
        # while node and node.next:
        #     if any_larger_after(node.next):
        #         # print(f"delete node {node.next.val}")
        #         node.next = node.next.next
        #     else:
        #         # print(f"keep node {node.next.val}")
        #         node = node.next
        node = head
        # print(f"keep head {head.val}")
        # del L[i]
        # del M[i]
        i += 1
        # print(f"{L=}\n{M=}")

        # while L:
        while i < len(L):
            if L[i] < M[i]:
                # print(f"delete node {node.next.val}")
                # del L[i]
                # del M[i]
                i += 1
                # print(f"{L=}\n{M=}")
                node.next = node.next.next
            else:
                # print(f"keep node {node.next.val}")
                # del L[i]
                # del M[i]
                i += 1
                # print(f"{L=}\n{M=}")
                node = node.next

        # print("done")
        # print(f"{L=}\n{M=}")
        return head

