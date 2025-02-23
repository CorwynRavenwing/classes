# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        def find_all_indexes(needle: str, haystack: str) -> List[int]:
            answers = []
            startIndex = 0
            while True:
                try:
                    index = haystack.index(needle, startIndex)
                except ValueError:
                    break
                answers.append(index)
                startIndex = index + 1
            return answers
        
        hyphens = find_all_indexes('-', traversal)
        # print(f'{hyphens=}')
        for i in reversed(range(1, len(hyphens))):
            # print(f'[{i}]:')
            A = hyphens[i - 1]
            B = hyphens[i]
            if A + 1 == B:
                hyphens[i] = None
                # print(f'  {A},{B}: delete B')
        while None in hyphens:
            hyphens.remove(None)
        assert 0 not in hyphens
        hyphens = [0] + hyphens + [len(traversal) + 1]
        # print(f'{hyphens=}')

        pieces = [
            [0, traversal[A:B]]
            for A, B in pairwise(hyphens)
        ]
        # print(f'{pieces=}')

        for i, (depth, piece) in enumerate(pieces):
            # print(f'[{i}]: {(depth,piece)}')
            while piece.startswith('-'):
                depth += 1
                piece = piece[1:]
                pieces[i] = (depth, piece)
                # print(f'  Update {(depth,piece)=}')
            piece = int(piece)
            pieces[i] = (depth, piece)
            # print(f'  Update {(depth,piece)=}\n')
        # print(f'{pieces=}')

        def tree_from_pieces(pieces_ref: List[Tuple[int,int]], my_depth=0) -> TreeNode:
            # print(f'tree_from_pieces({depth},*{len(pieces_ref)})')
            if not pieces_ref:
                # print(f'  -> null')
                return None
            (test_depth, test_value) = pieces_ref[0]
            if test_depth < my_depth:
                # print(f'  -> {test_depth} < {my_depth}')
                return None
            if test_depth > my_depth:
                print(f'  -> ERROR: {test_depth} > {my_depth}')
                raise Exception(f'Test depth higher than current depth')
            
            _ = pieces_ref.pop(0)
            my_value = test_value
            left = tree_from_pieces(pieces_ref, my_depth + 1)
            right = tree_from_pieces(pieces_ref, my_depth + 1)
            answer = TreeNode(my_value, left, right)
            # VAL = lambda Node: (Node.val if Node else '-')
            # print(f'  => {VAL(answer)}: ({VAL(answer.left)},{VAL(answer.right)})')
            return answer

        answer = tree_from_pieces(pieces)
        assert pieces == []
        return answer

# NOTE: Acceptance Rate 76.3% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 698 ms Beats 5.00%
# NOTE: Memory 19.27 MB Beats 5.29%
