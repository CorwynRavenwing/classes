# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        def allSubtreeSums(node: TreeNode) -> List[int]:
            # returns sum(node) as the first result
            if not node:
                return []
            L = allSubtreeSums(node.left)
            R = allSubtreeSums(node.right)
            SumOfNode = sum([
                node.val,
                L[0] if L else 0,
                R[0] if R else 0,
            ])
            return [SumOfNode] + L + R
        
        ASTS = allSubtreeSums(root)
        print(f'{ASTS=}')
        counts = Counter(ASTS)
        print(f'{counts=}')
        answer = []
        maxCount = None
        for (number,count) in counts.most_common():
            print(f'{number=} {count=}')
            if maxCount is None:
                maxCount = count
            if maxCount == count:
                answer.append(number)
            else:
                break

        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 49 ms Beats 28.29%
# NOTE: Memory 19.93 MB Beats 5.66%
