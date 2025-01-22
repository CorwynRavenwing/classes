class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        H = len(grid)       # should == 2
        N = len(grid[0])
        # INTUITION: whatever the first robot does, the second robot
        # only has two rational paths:
        # A: D immediately, R R R to the end
        # B: R R R to the end, D last
        # These two paths will sum to specific things.
        # If we call the path of robot 1 "R 'X' times, D once, R 'N - X' times"
        # meaning robot 1 moves D in column #X, then robot 2's sums are:
        # A: sum of BOTTOM row LEFT of column X
        # B: sum of TOP row RIGHT of column X
        # robot 1 can only change their choice of X, and for each one those two sums
        # will be fixed.  Whichever pair is picked, robot 2 chooses the higher one.
        # Therefore robot 1 wants to choose X such that (max of A and B) is minimized.

        # HOWEVER, top left corner and bottom right corner will never be included
        # in robot 2's score.

        REV = lambda x: list(reversed(list(x)))

        sumTopFromRight = REV(itertools.accumulate(REV(grid[0])))
        sumBottomFromLeft = list(itertools.accumulate(grid[1]))
        # print(f'  {sumTopFromRight=}')
        # print(f'{sumBottomFromLeft=}')

        answers = []
        for X in range(N):
            TOP = (
                sumTopFromRight[X + 1]
                if X < N - 1
                else 0
            )
            BOTTOM = (
                sumBottomFromLeft[X - 1]
                if X > 0
                else 0
            )
            # print(f'{X=} {TOP=} {BOTTOM=}')
            answers.append(max(TOP,BOTTOM))
        print(f'{answers=}')

        return min(answers)

# NOTE: Runtime 832 ms Beats 54.93%
# NOTE: Memory 32.84 MB Beats 40.04%

# NOTE: re-ran for challenge:
# NOTE: Runtime 111 ms Beats 54.75%
# NOTE: Memory 32.32 MB Beats 5.25%
# NOTE: greatly better speed: basically identical percantage
# NOTE: basically identical memory usage: much worse percentage
