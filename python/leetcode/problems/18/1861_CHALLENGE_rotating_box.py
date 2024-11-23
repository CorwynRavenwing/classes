class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        # SHORTCUT 1: rotate() is hard,
        # but rotate() === reverseEachRow(transpose())
        # and each of those is easy.
        # (note that transpose(reverseEachRow()) is *not* equivelent)

        # SHORTCUT 2: rearanging columns is harder than rearranging rows,
        # so I will do the work by pretending gravity is towards the right,
        # and rotate the matrix afterwards.

        def gravity_towards_right(row: List[str]) -> List[str]:
            prior_row = ['guaranteed to be different']
            # print(f'\n{row=} ({prior_row != row})')
            while prior_row != row:
                prior_row = row[:]      # must not be a pointer to the same object
                for i in range(1, len(row)):
                    (L, R) = row[i - 1:i + 1]
                    if (L, R) == ('#', '.'):
                        # stone followed by empty: stone falls to the right
                        row[i - 1:i + 1] = (R, L)     # swap stone and empty space
                # print(f'{row=} ({prior_row != row})')
            return row

        box_after_gravity = [
            gravity_towards_right(row)
            for row in box
        ]
        box_transposed = tuple(zip(*box_after_gravity))
        box_rotated = [
            tuple(reversed(row))
            for row in box_transposed
        ]
        return box_rotated

# NOTE: Accepted on second Run (first was reference-vs-copy error)
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 5367 ms Beats 5.06%
# NOTE: Memory 29.04 MB Beats 43.28%
