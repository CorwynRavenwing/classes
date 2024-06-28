class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        mod = 10 ** 9 + 7
        size = len(arr)

        num_index_pairs = [
            (N, index)
            for (index, N) in enumerate(arr)
        ]

        answer = 0
        blocked = [-1, size]
        # print(f'{blocked=}')

        num_index_pairs.sort()
        while num_index_pairs:
            (min_N, min_index) = num_index_pairs.pop(0)

            location = bisect_left(blocked, min_index)
            blocked.insert(location, min_index)
            # print(f'Insert {min_index} at {location}:')
            # print(f'-> {blocked=}')
            L = blocked[location - 1] + 1
            R = blocked[location + 1] - 1

            subarrays_where_i_am_minimum = (
                (min_index - L + 1) * (R - min_index + 1)
            )

            print(f'+ {min_N} * {subarrays_where_i_am_minimum}')
            answer += (min_N * subarrays_where_i_am_minimum)
            answer %= mod

        return answer

