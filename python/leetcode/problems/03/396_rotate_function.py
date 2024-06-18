class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        # F(0)= 0A + 1B + 2C + 3D
        # F(1)= 1A + 2B + 3C + 0D
        # F(2)= 2A + 3B + 0C + 1D
        # F(3)= 3A + 0B + 1C + 2D
        # F(0)= 0A + 1B + 2C + 3D
        # the transition between these,
        # is to ADD (A+B+C+D), which is sum(nums),
        # and then SUBTRACT 4D, where 4 is len(nums)
        # you do this 4 times, once for each of D,C,B,A in that order
        # (actually only 3, b/c the 4th one will get back F(0) again)
        # ((unless you want to checksum your work))

        F0 = sum([
            i * N
            for i, N in enumerate(nums)
        ])
        answers = []
        Fi = F0
        i = 0
        print(f'F({i})={Fi}')
        SUM = sum(nums)
        LEN = len(nums)
        for N in reversed(nums):
            i += 1
            i %= LEN
            Fi = Fi + SUM - (LEN * N)
            # print(f'F({i})={Fi}')
            answers.append(Fi)
        # checksum last one
        assert Fi == F0
        print(f'{answers=}')
        return max(answers)

