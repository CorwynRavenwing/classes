class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        mod = 10 ** 9 + 7

        sortedNums = sorted(set(nums))  # in order, each one unique
        # print(f'{sortedNums=}')

        partialSums = list(itertools.accumulate(nums))
        # print(f'{partialSums=}')

        def MSMP(first_index: int, last_index: int, MIN: int, depth=0) -> int:
            nonlocal sortedNums, partialSums
            margin = '  ' * depth
            # print(f'{margin}MSMP({first_index},{last_index},{MIN}):')
            if first_index > last_index:
                # nonexistent range
                return 0

            # print(f'{margin}  DEBUG: frag={nums[first_index:last_index + 1]}')

            if first_index == last_index:
                # only one number in this list
                NUM = nums[first_index]
                return NUM * NUM    # min([X]) == X; sum([X]) == X
            
            SUM = (
                partialSums[last_index] - partialSums[first_index - 1]
                if first_index
                else partialSums[last_index]
            )
            # print(f'  ... fetching sortedNums[{min_index}] (len={len(sortedNums)})')
            # MIN = sortedNums[min_index]
            retval = MIN * SUM
            new_min = None
            for i in range(first_index, last_index + 1):
                NUM = nums[i]
                if new_min is None or new_min > NUM:
                    new_min = NUM
                if NUM == MIN:
                    if first_index <= i:
                        retval = max(retval, MSMP(first_index, i - 1, new_min))
                        new_min = None
                    first_index = i + 1
            if first_index <= last_index:
                retval = max(retval, MSMP(first_index, last_index, new_min))
            return retval

        answer = MSMP(0, len(nums) - 1, min(nums))

        print(f'{answer=}')

        return answer % mod
# NOTE: Time Limit Exceeded for large inputs
