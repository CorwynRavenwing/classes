# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def AllNodesAtDistanceK(self, root: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        if k == 0:
            return [root.val]
        
        left = self.AllNodesAtDistanceK(root.left, k - 1)
        right = self.AllNodesAtDistanceK(root.right, k - 1)
        return left + right

    def DistanceFoundAt_Plus_NodesAtDistanceK(self, root: TreeNode, target: int, k: int) -> Tuple[int,List[int]]:

        def TreeNode_toString(node: TreeNode) -> str:
            S = f'{node}'
            S = S.replace('TreeNode{val: ', 'Tree{')
            S = S.replace(', left: ', ' L:')
            S = S.replace(', right: ', ' R:')
            S = S.replace('L:Tree{', 'L:{')
            S = S.replace('R:Tree{', 'R:{')
            S = S.replace(' L:None', ' L:-')
            S = S.replace(' R:None', ' R:-')
            S = S.replace(' L:- R:-}', '}')
            return S

        def show_TreeNode(label: str, node: TreeNode):
            nodeStr = TreeNode_toString(node)
            print(f'{label}: {nodeStr}')

        show_TreeNode('CALL', root)

        if not root:
            show_TreeNode('NO', root)
            return (None, [])
        
        if root.val == target:
            show_TreeNode('YES HERE', root)
            # found on this node
            distance = 0
            nodeList = self.AllNodesAtDistanceK(root, k)
            return (distance, nodeList)
        
        show_TreeNode('TRY LEFT', root)
        (distance, nodeList) = self.DistanceFoundAt_Plus_NodesAtDistanceK(root.left, target, k)
        if distance is not None:
            show_TreeNode('YES LEFT', root)
            # found on left fork
            distance += 1
            right = self.AllNodesAtDistanceK(root.right, k - distance - 1)
            nodeList += right
            if distance == k:
                nodeList += [root.val]
            return (distance, nodeList)
        
        show_TreeNode('TRY RIGHT', root)
        (distance, nodeList) = self.DistanceFoundAt_Plus_NodesAtDistanceK(root.right, target, k)
        if distance is not None:
            show_TreeNode('YES RIGHT', root)
            # found on right fork
            distance += 1
            left = self.AllNodesAtDistanceK(root.left, k - distance - 1)
            nodeList += left
            if distance == k:
                nodeList += [root.val]
            return (distance, nodeList)
        
        # found on neither fork
        show_TreeNode('NEITHER', root)
        return (None, [])

    # WRONG! problem description says that target is an int, not a TreeNode
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    # def distanceK(self, root: TreeNode, target: int, k: int) -> List[int]:
        
        target = target.val     # make it match the problem description

        (distance, nodeList) = self.DistanceFoundAt_Plus_NodesAtDistanceK(root, target, k)
        print(f'FOUND at {distance=}')

        return nodeList

# NOTE: Runtime 239 ms Beats 5.33%
# NOTE: Memory 17.06 MB Beats 17.50%
