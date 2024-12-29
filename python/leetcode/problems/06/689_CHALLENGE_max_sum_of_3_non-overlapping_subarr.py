class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        partialSums = (0,) + tuple(accumulate(nums))
        # print(f'{partialSums=}')

        sumsOfK = tuple([
            partialSums[i] - partialSums[i - k]
            for i in range(k, len(nums) + 1)
        ])
        # print(f'{sumsOfK=}')

        # return value of each function is (sum_of_values, (list, of, indexes))

        def DP_skip(elements_left: int, start_index: int) -> Tuple[int,List[int]]:
            return DP(elements_left, start_index + 1)

        def DP_pick(elements_left: int, start_index: int) -> Tuple[int,List[int]]:
            sum_here = sumsOfK[start_index]
            (sum_of_values, index_list) = DP(elements_left - 1, start_index + k)
            return (
                sum_of_values + sum_here,
                (start_index,) + index_list
            )

        @cache
        def DP(elements_left: int, start_index: int) -> Tuple[int,List[int]]:
            print(f'DP({elements_left},{start_index})')
            if not elements_left:
                return (0, ())
            try:
                check = sumsOfK[start_index]
            except IndexError:
                return (0, ())
            answers = [
                DP_skip(elements_left, start_index),
                DP_pick(elements_left, start_index),
            ]
            return min(
                answers,
                # min with negative sum === max, but with lowest indexes
                key=lambda x: (-x[0], x[1])
            )

        (sum_of_values, index_list) = DP(3, 0)
        print(f'{sum_of_values=}')
        return index_list

# NOTE: Acceptance Rate 51.2% (HARD)
# NOTE: Accepted on second run (sorting issue)
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 463 ms Beats 5.55%
# NOTE: Memory 75.94 MB Beats 5.28%
