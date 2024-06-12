# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def display_level(label: str, level: List[TreeNode|int|None]) -> None:
            display = [
                (
                    C
                    if (C is None) or isinstance(C, int)
                    else f'<{C.val}>'
                )
                for C in level
            ]
            print(f'{label}:{display}')
            return

        maxwidth = 0
        level = [root]
        display_level('start', level)
        while level:        
            # 0. combine adjacent integers
            for i in range(0, len(level)):
                if isinstance(level[i], int) and isinstance(level[i-1], int):
                    # print(f'combine [{i-1},{i}] {level[i-1]}, {level[i]}')
                    level[i] += level[i-1]
                    level[i-1] = 0
                    display_level('combined ints', level)
            while 0 in level:
                # print(f'remove a 0 at [{level.index(0)}]')
                level.remove(0)
                display_level('removed 0', level)

            # 1. check current width
            counts = [
                C if isinstance(C, int) else 1
                for C in level
            ]
            width = sum(counts)
            print(f'{width=}: {counts}')
            maxwidth = max(maxwidth, width)

            # 2. increase level
            new_level = []
            for C in level:
                if isinstance(C, int):
                    new_level.append(2 * C)
                else:
                    new_level.append(C.left)
                    new_level.append(C.right)
            print(f'old={len(level)} new={len(new_level)}')
            level = new_level
            display_level('increased', level)

            # 3. remove None, ints from first and last positions
            while level and ((level[0] is None) or isinstance(level[0], int)):
                # print(f'delete None/int from front')
                del level[0]
                display_level('del first', level)
            while level and ((level[-1] is None) or isinstance(level[-1], int)):
                # print(f'delete None/int from back')
                del level[-1]
                display_level('del last', level)
            print(f'now={len(level)}')

            # 4. replace interior None with 1:
            for i, C in enumerate(level):
                if C is None:
                    # print(f'[{i}]: replace {None} -> {1}')
                    level[i] = 1
                    display_level('None -> 1', level)
            
        return maxwidth

