class Solution:

    def __init__(self) -> None:
        self.DEBUG = False

    # we borrow some code from #3195:

    def INV(self, grid: List[List[int]]) -> List[List[int]]:
        # inverts grid, swapping X with Y
        return tuple(zip(*grid))

    def REV(self, grid: List[List[int]]) -> List[List[int]]:
        # reverses each row of grid, left to right
        return tuple(map(tuple, map(reversed, grid)))

    # gives the minimum area of a single rectangle
    # covering all ones in this section
    def minimumArea(self, grid: List[List[int]]) -> int:

        if self.DEBUG: print(f'  mA({grid})')

        SUM = lambda G: tuple(map(sum, G))

        NZ_raw = lambda L: [
            (
                index
                if value > 0
                else None
            )
            for index, value in enumerate(L)
        ]
        NZ = lambda L: [
            value
            for value in NZ_raw(L)
            if value is not None
        ]

        WIDTH = lambda L: (
            1 + max(L) - min(L)
            if len(L) > 0
            else None
        )

        width = WIDTH(NZ(SUM(grid)))
        height = WIDTH(NZ(SUM(self.INV(grid))))

        if None in (width, height):
            if self.DEBUG: print(f'  mA({grid}): {width}, {height} -> None')
            return None
        answer = width * height
        if self.DEBUG: print(f'  mA({grid}): {width}, {height} -> {answer}')
        return answer

    def minimumSum_N_simple(self, N: int, grid: List[List[int]]) -> int:
        
        if self.DEBUG: print(f'mSNs({N},{grid})')
        if N == 1:
            # bottom level: one rectangle spanning everything
            answer = self.minimumArea(grid)
            if self.DEBUG: print(f'mSNvt({N},{grid}): {answer}')
            return answer

        # else, we are calving off a section on the top
        # to check separately, and recursing:

        answers = []
        for index in range(1, len(grid)):
            # MUST split into two sections, therefore
            # neither first nor last row counts
            top_section = grid[:index]
            bottom_section = grid[index:]
            if self.DEBUG: print(f'  [{index}] {top_section} // {bottom_section}')
            top_size = self.minimumArea(top_section)
            if top_size is None:
                if self.DEBUG: print(f'mSNvt({N},{grid}): {top_size}, --- -> None')
                continue
            bottom_size = self.minimumSum_N(N - 1, bottom_section)
            if bottom_size is None:
                if self.DEBUG: print(f'mSNvt({N},{grid}): {top_size}, {bottom_size} -> None')
                continue
            answer = top_size + bottom_size
            if self.DEBUG: print(f'mSNvt({N},{grid}): {top_size}, {bottom_size} -> {answer}')
            answers.append(answer)
        return min(answers, default=None)

    def minimumSum_N_vertical_top(self, N: int, grid: List[List[int]]) -> int:
        if self.DEBUG: print(f'(vert top) {grid=}')
        return self.minimumSum_N_simple(N, grid)

    def minimumSum_N_horizontal_left(self, N: int, grid: List[List[int]]) -> int:
        grid = self.INV(grid)
        if self.DEBUG: print(f'(horiz left) {grid=}')
        return self.minimumSum_N_simple(N, grid)

    def minimumSum_N_horizontal_right(self, N: int, grid: List[List[int]]) -> int:
        grid = self.REV(grid)
        grid = self.INV(grid)
        if self.DEBUG: print(f'(horiz right) {grid=}')
        return self.minimumSum_N_simple(N, grid)

    def minimumSum_N_vertical_bottom(self, N: int, grid: List[List[int]]) -> int:
        grid = self.INV(grid)
        grid = self.REV(grid)
        grid = self.INV(grid)
        if self.DEBUG: print(f'(vert bottom) {grid=}')
        return self.minimumSum_N_simple(N, grid)

    def minimumSum_N(self, N: int, grid: List[List[int]]) -> int:
        answers = [
            self.minimumSum_N_vertical_top(N, grid),
            self.minimumSum_N_vertical_bottom(N, grid),
            self.minimumSum_N_horizontal_left(N, grid),
            self.minimumSum_N_horizontal_right(N, grid),
        ]
        while None in answers:
            answers.remove(None)
        return min(answers, default=None)

    def minimumSum(self, grid: List[List[int]]) -> int:
        
        answer = self.minimumSum_N(3, grid)
        return (
            answer
            if answer is not None
            else 3
        )

# NOTE: Acceptance Rate 32.3% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (was exiting loop early; output ex.)
# NOTE: Runtime 9851 ms Beats 7.14%
# NOTE: Memory 22.75 MB Beats 9.52%
