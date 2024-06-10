"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        
        def showTree(label: str, quadTree: 'Node', depth=0) -> None:
            margin = "  " * depth
            if quadTree.isLeaf:
                print(margin + f'{label} Leaf={quadTree.val}')
                return
            print(margin + f'{label} Quad Node:')
            showTree(label + " topLeft", quadTree.topLeft, depth+1)
            showTree(label + " topRight", quadTree.topRight, depth+1)
            showTree(label + " bottomLeft", quadTree.bottomLeft, depth+1)
            showTree(label + " bottomRight", quadTree.bottomRight, depth+1)
            # print(margin + f'{label} done')
        
        def combine(leafTree: 'Node', quadTree: 'Node') -> 'Node':
            if leafTree.val == True:
                # (True OR X) === True
                return leafTree
                # ... which leafTree already is
            else:
                # (False OR Y) === Y
                return quadTree
                # ... again, which quadTree already is
            # if we care about object ownership, we should really return
            # a deep copy of quadTree and a shallow copy of leafTree instead

        print(f'intersect():')
        showTree('QT1', quadTree1)
        showTree('QT2', quadTree2)

        if quadTree1.isLeaf and quadTree2.isLeaf:
            value = (quadTree1.val or quadTree2.val)
            print(f'  Leaf Node: {value}')
            return Node(value, True, None, None, None, None)
        
        # note the QT1 / QT2 labels are swapped between these cases!
        if quadTree1.isLeaf and not quadTree2.isLeaf:
            return combine(quadTree1, quadTree2)
        if quadTree2.isLeaf and not quadTree1.isLeaf:
            return combine(quadTree2, quadTree1)
        
        print(f'  Recurse')
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        leaf_nodes = [
            topLeft.isLeaf,
            topRight.isLeaf,
            bottomLeft.isLeaf,
            bottomRight.isLeaf,
        ]
        if all(leaf_nodes):
            values = [
                topLeft.val,
                topRight.val,
                bottomLeft.val,
                bottomRight.val,
            ]
            count_values = Counter(values)
            if len(count_values) == 1:
                value = values[0]   # again, they're all identical, so pick any
                print(f'  -> leaf node after all: {value}')
                return Node(value, True, None, None, None, None)
        
        print(f'Quad node')
        answer = Node(None, False, topLeft, topRight, bottomLeft, bottomRight)
        showTree('ANS', answer)
        return answer

