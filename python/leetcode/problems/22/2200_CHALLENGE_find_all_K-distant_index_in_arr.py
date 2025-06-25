class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        
        indexes_matching_key = [
            index
            for index, value in enumerate(nums)
            if value == key
        ]
        # print(f'{indexes_matching_key=}')

        k_endpoints = [
            (
                max(index - k, 0),
                min(index + k, len(nums) - 1),
            )
            for index in indexes_matching_key
        ]
        # print(f'{k_endpoints=}')

        unroll_endpoints = {
            C
            for (A, B) in k_endpoints
            for C in range(A, B + 1)
        }
        # print(f'{unroll_endpoints=}')

        return tuple(sorted(unroll_endpoints))

# NOTE: Acceptance Rate 70.4% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 135 ms Beats 41.05%
# NOTE: Memory 18.12 MB Beats 28.93%
