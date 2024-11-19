# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        def inOrder(node: TreeNode) -> List[int]:
            if not node:
                return ()
            L = inOrder(node.left)
            R = inOrder(node.right)
            C = (node.val,)
            return L + C + R
        
        def listMerge(list1: List[int], list2: List[int]) -> List[int]:
            answer = []
            while list1 and list2:
                if list1[0] < list2[0]:
                    answer.append(list1[0])
                    list1 = list1[1:]
                elif list1[0] > list2[0]:
                    answer.append(list2[0])
                    list2 = list2[1:]
                elif list1[0] == list2[0]:
                    answer.append(list1[0])
                    answer.append(list2[0])
                    list1 = list1[1:]
                    list2 = list2[1:]
            while list1:
                answer.append(list1[0])
                list1 = list1[1:]
            while list2:
                answer.append(list2[0])
                list2 = list2[1:]
            return answer
        
        list1 = inOrder(root1)
        list2 = inOrder(root2)

        return listMerge(list1, list2)

# NOTE: Accepted on third Run (was doing intersect, then no-dup merge)
# NOTE: Accepted on first Submit
# NOTE: Runtime 555 ms Beats 5.05%
# NOTE: Memory 20.85 MB Beats 7.48%
