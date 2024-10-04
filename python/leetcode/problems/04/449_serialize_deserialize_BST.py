# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # we borrow some code from #297:

    def levelValuesWithNones(self, nodes: List[TreeNode]) -> List[int]:
        # print(f'>>{nodes=}')
        values = [
            node.val if node else None
            for node in nodes
        ]
        # print(f'<<{values=}')
        return values

    def nextLevelWithNones(self, nodes: List[TreeNode]) -> List[TreeNode]:
        newNodes = [
            [node.left, node.right]
            for node in nodes
            if node
        ]
        # print(f'{newNodes=}')
        answer = [
            node
            for group in newNodes
            for node in group
            # if node
        ]
        # print(f'{answer=}')
        return answer

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = [root]
        answer = []
        while nodes:
            # print(f'{nodes=}')
            answer.append(
                self.levelValuesWithNones(nodes)
            )
            nodes = self.nextLevelWithNones(nodes)
            if all([N is None for N in nodes]):
                break
        # print(f'{answer=}')
        # if [] in answer:
        #     answer.remove([])

        return answer

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        levelOrder = self.levelOrder(root)
        print(f'{levelOrder=}')
        flattened = [
            N
            for flatten in levelOrder
            for N in flatten
        ]
        print(f'{flattened=}')
        answer = ','.join([
            str(N) if N is not None else 'X'
            for N in flattened
        ])
        answer = f'[{answer}]'
        print(f'{answer=}')
        return answer

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        print(f'decode({data}):')
        assert data[0] == '['
        assert data[-1] == ']'
        data = data.replace('[','',1)
        data = data.replace(']','',1)
        assert '[' not in data
        assert ']' not in data
        levelOrder = [
            None if N == 'X' else int(N)
            for N in data.split(',')
        ]
        print(f'{levelOrder=}')
        N = levelOrder.pop(0)
        head = TreeNode(N) if N is not None else None
        level = [head]
        while level:
            newLevel = []
            for node in level:
                if node is None:
                    continue
                else:
                    print(f'Under {node.val}:')
                    N = levelOrder.pop(0) if levelOrder else None
                    print(f'  left : {N}')
                    newNode = TreeNode(N) if N is not None else None
                    node.left = newNode
                    newLevel.append(newNode)
                    # -----
                    N = levelOrder.pop(0) if levelOrder else None
                    print(f'  right: {N}')
                    newNode = TreeNode(N) if N is not None else None
                    node.right = newNode
                    newLevel.append(newNode)
            level = newLevel
        assert levelOrder == []
        checksum = self.levelOrder(head)
        print(f'Checksum:')
        for C in checksum:
            print(f'  {C}')

        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

# NOTE: Acceptance Rate: 58.0%
# NOTE: Re-used exact prior version without changes
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 105 ms Beats 5.07%
# NOTE: Memory 20.46 MB Beats 44.14%
# NOTE: This version does not count on the tree being binary
#       and therefore is not as efficient as it would be if it did.
