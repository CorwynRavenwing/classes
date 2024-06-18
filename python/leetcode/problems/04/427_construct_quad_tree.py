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
    def construct(self, grid: List[List[int]]) -> 'Node':

        gridSize = len(grid)    # === len(grid[0])
        gridHalf = gridSize // 2
        print(f'construct({gridSize}x{gridSize})')

        def single_value(grid: List[List[int]]) -> int:
            flatten = [
                val
                for row in grid
                for val in row
            ]
            counts = Counter(flatten)
            print(f'{counts=}')
            if len(counts) > 1:
                return None

            # since all cells are the same, return any one of them
            return grid[0][0]
        
        # 1. check for all-one-value
        value = single_value(grid)
        if value is not None:
            print(f'Leaf node: {value}')
            return Node(value, True, None, None, None, None)
        
        # 2. split grid into 4 quadrants
        print(f'Quad node: half = {gridHalf}')
        grid_TopHalf = grid[:gridHalf]
        grid_BottomHalf = grid[gridHalf:]

        grid_TopLeft = [row[:gridHalf] for row in grid_TopHalf]
        grid_TopRight = [row[gridHalf:] for row in grid_TopHalf]

        grid_BottomLeft = [row[:gridHalf] for row in grid_BottomHalf]
        grid_BottomRight = [row[gridHalf:] for row in grid_BottomHalf]

        # 3. recurse
        topLeft = self.construct(grid_TopLeft)
        topRight = self.construct(grid_TopRight)
        bottomLeft = self.construct(grid_BottomLeft)
        bottomRight = self.construct(grid_BottomRight)

        return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)

