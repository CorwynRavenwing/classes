# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def nodes_sum_and_matches_so_far(node: TreeNode) -> Tuple[int,int,int]:
            if node is None:
                return (0, 0, 0)
            
            print(f'N_S_Msf({node.val})')

            Left = nodes_sum_and_matches_so_far(node.left)
            Right = nodes_sum_and_matches_so_far(node.right)

            (left_nodes, left_sum, left_matches) = Left
            (right_nodes, right_sum, right_matches) = Right

            total_nodes = sum([
                left_nodes,
                right_nodes,
                1,
            ])
            total_sum = sum([
                left_sum,
                right_sum,
                node.val,
            ])

            total_average = total_sum // total_nodes
            total_matches = sum([
                left_matches,
                right_matches,
                (
                    1
                    if (total_average == node.val)
                    else 0
                )
            ])

            answer = (total_nodes, total_sum, total_matches)
            print(f'N_S_Msf({node.val}): {answer}')
            return answer

        (nodes, total, matches) = nodes_sum_and_matches_so_far(root)
        return matches

# NOTE: Accepted on second Run (function-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 62 ms Beats 5.12%
# NOTE: Memory 17.92 MB Beats 93.01%
