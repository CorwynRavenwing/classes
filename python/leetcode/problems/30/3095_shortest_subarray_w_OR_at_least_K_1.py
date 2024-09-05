class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        print(f'{nums=}')
        for length_try in range(1, len(nums)+1):
            print(f'trying length {length_try}')
            for index in range(0, len(nums)-length_try+1):
                array = nums[index:index+length_try]
                print(f'  {array=}')
                bitwise_or = array[0]
                for element in array[1:]:
                    bitwise_or |= element
                print(f'    {bitwise_or}')
                if bitwise_or >= k:
                    print(f'      >= {k}')
                    return length_try
        return -1

# NOTE: Runtime 89 ms Beats 7.16%
# NOTE: Memory 16.48 MB Beats 80.52%
