class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:

        # as we learned for the Ants project, "identical objects bounce
        # off each other and change direction" === "ignore collisions"
        
        new_positions = [
            (
                old_pos + d
                if direction == 'R'
                else
                old_pos - d
            )
            for old_pos, direction in zip(nums, s)
        ]
        # print(f'raw    {new_positions=}')
        new_positions.sort()
        # print(f'sorted {new_positions=}')

        # now to sum the position differences:
        # A, B, C, D, E, F ->
        # = B-A + C-A + D-A + E-A + F-A
        # +       C-B + D-B + E-B + F-B
        # +             D-C + E-C + F-C
        # +                   E-D + F-D
        # +                         F-E
        # = 5F-0F + 4E-1E + 3D-2D + 2C-3C + 1B-4B 0A-5A
        # = (5-0)F + (4-1)E + (3-2)D + (2-3)C + (1-4)B + (0-5)A
        # = 5F + 3E + 1D + (-1)C + (-3)B + (-5)A
        # show_me = [
        #     f'({index} - {len(new_positions) - 1 - index}) * {N}'
        #     for index, N in enumerate(new_positions)
        # ]
        # print(f'{show_me=}')
        partial_answers = [
            ((index) - (len(new_positions) - 1 - index)) * N
            for index, N in enumerate(new_positions)
        ]
        print(f'{partial_answers=}')

        mod = 10 ** 9 + 7

        return sum(partial_answers) % mod
# NOTE: Runtime 380 ms Beats 58.75%
# NOTE: Memory 34.29 MB Beats 5.00%
