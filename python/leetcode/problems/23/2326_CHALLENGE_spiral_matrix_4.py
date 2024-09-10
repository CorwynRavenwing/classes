# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        grid = [
            [-1] * n
            for _ in range(m)
        ]

        directions = (
            (+0, +1),   # east
            (+1, +0),   # south
            (+0, -1),   # west
            (-1, +0),   # north
        )
        direction_index = 0
        direction = directions[direction_index]

        def turn() -> None:
            nonlocal direction_index, direction
            direction_index += 1
            direction_index %= len(directions)
            direction = directions[direction_index]
            return

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < m) and (0 <= Y < n)
        
        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        def valueAt(cell: Tuple[int,int]) -> int:
            if OOB(cell):
                return None
            (X, Y) = cell
            return grid[X][Y]

        def setValueAt(cell: Tuple[int,int], value: int) -> bool:
            print(f'setValueAt({cell},{value})')
            if OOB(cell):
                return False
            (X, Y) = cell
            grid[X][Y] = value
            return True
        
        def move(cell: Tuple[int,int], direction: Tuple[int,int]) -> Tuple[int,int]:
            (X, Y) = cell
            (I, J) = direction
            return (X + I, Y + J)
        
        def nextLegalPos(cell: Tuple[int,int]) -> Tuple[int,int]:
            nonlocal direction
            tryPos = move(cell, direction)
            if legalPos(tryPos):
                if valueAt(tryPos) == -1:
                    return tryPos
            
            turn()  # changes Global "direction"
            tryPos = move(cell, direction)
            if legalPos(tryPos):
                if valueAt(tryPos) == -1:
                    return tryPos
            
            print(f'ERROR: nextLegalPos({cell}) cannot move forward or clockwise')
            return None

        position = (0,0)
        if valueAt(position) != -1:
            print(f'ERROR: {position=} value={valueAt(position)} should be {-1}')
            return [[-99]]

        node = head
        while node:
            setValueAt(position, node.val)
            node = node.next
            position = nextLegalPos(position)
        
        return grid

# NOTE: Accepted on first Submit
# NOTE: Runtime 1340 ms Beats 5.07%
# NOTE: Memory 54.98 MB Beats 60.00%
