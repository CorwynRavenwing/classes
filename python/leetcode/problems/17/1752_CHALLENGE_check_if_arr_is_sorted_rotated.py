class Solution:
    def check(self, nums: List[int]) -> bool:
        
        def find_all_indexes(needle: int, haystack: List[int]) -> List[int]:
            answers = []
            startIndex = 0
            while True:
                try:
                    index = haystack.index(needle, startIndex)
                except ValueError:
                    break
                answers.append(index)
                startIndex = index + 1
            return answers

        highest_value = max(nums)
        lowest_value = min(nums)
        highest_indexes = find_all_indexes(highest_value, nums)
        lowest_indexes = find_all_indexes(lowest_value, nums)
        lowest_index = None
        for high_index in highest_indexes:
            low_index = high_index + 1
            if low_index in lowest_indexes:
                lowest_index = low_index
                break
        if nums[0] == lowest_value and nums[-1] == highest_value:
            lowest_index = 0
        if lowest_index is None:
            print(f'{lowest_value =}')
            print(f'{highest_value=}')
            print(f'{lowest_indexes =}')
            print(f'{highest_indexes=}')
            print(f'NO: highest value is never followed by lowest value')
            return False
        unrotated = nums[lowest_index:] + nums[:lowest_index]
        sorted_arr = sorted(nums)
        print(f'{unrotated =}')
        print(f'{sorted_arr=}')
        return (unrotated == sorted_arr)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case with duplicate low value)
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.84 MB Beats 29.61%
