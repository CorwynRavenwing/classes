class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        @cache
        def DP(data: Tuple[int,int,int]) -> int:
            # print(f'DP{data}')
            if len(data) <= 1:
                return 0
            if 0 in data:
                index = data.index(0)
                new_data = data[:index] + data[index + 1:]
                return DP(new_data)

            if len(data) == 2:
                (A, B) = data
                new_data = (A - 1, B - 1)
                return 1 + DP(new_data)
            assert len(data) == 3

            # # We should probably only take highest and second-highest value
            # # rather than this mess:

            # answers = []
            # for i in range(3):
            #     for j in range(i + 1, 3):
            #         new_data = tuple(sorted([
            #             (
            #                 D - 1
            #                 if index in [i, j]
            #                 else D
            #             )
            #             for index, D in enumerate(data)
            #         ]))
            #         answers.append(
            #             1 + DP(new_data)
            #         )
            # return max(answers)
            
            # # Yup!  That hit Time Limit Exceeded.  Trying the quicker answer:
            (A, B, C) = data
            if not (A <= B <= C):
                new_data = tuple(sorted(data))
                return DP(new_data)
            
            new_data = tuple(sorted([
                (
                    D
                    if (index == 0)
                    else D - 1
                )
                for index, D in enumerate(data)
            ]))
            return 1 + DP(new_data)
        
        return DP((a, b, c))

# NOTE: Original version:
# NOTE: Accepted on first Run, but got Time Limit Exceeded on Submit
# NOTE: Faster version:
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 1332 ms Beats 5.31%
# NOTE: Memory 437.51 MB Beats 8.24%
