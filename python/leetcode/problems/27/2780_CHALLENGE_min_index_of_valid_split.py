class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        # STEP 1: find dominant value
        
        counts = Counter(nums)
        most_common_list = counts.most_common(1)
        # print(f'{most_common_list=}')
        most_common_pair = most_common_list[0]
        # print(f'{most_common_pair=}')
        (dominant_value, dominant_count) = most_common_pair
        n = len(nums)
        print(f'{dominant_value=}, {dominant_count} / {n}')

        # STEP 2: we don't actually care about the values:
        # just whether or not they are the dominant one.

        is_dominant = [
            1 if value == dominant_value else 0
            for value in nums
        ]
        print(f'{is_dominant=}')

        partialSum = (0,) + tuple(accumulate(is_dominant))
        print(f'{partialSum=}')
        ps_0 = partialSum[0]
        ps_N = partialSum[-1]
        
        # split_data = []
        for i in range(0, n - 1):
            ps_I = partialSum[i + 1]
            dominant_A = ps_I - ps_0
            dominant_B = ps_N - ps_I
            elements_A = i + 1
            elements_B = n - elements_A
            pass_A = ((dominant_A * 2) > elements_A)
            pass_B = ((dominant_B * 2) > elements_B)
        #     split_data.append(
        #         (
        #             i,
        #             dominant_A,
        #             elements_A,
        #             dominant_B,
        #             elements_B,
        #             pass_A,
        #             pass_B,
        #         )
        #     )
            if pass_A and pass_B:
                return i
        # print(f'{split_data=}')

        return -1

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 155 ms Beats 13.72%
# NOTE: Memory 35.17 MB Beats 6.86%
