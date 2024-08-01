class Solution:
    def halveArray(self, nums: List[int]) -> int:

        nums.sort()
        original_sum = sum(nums)
        current_sum = original_sum
        target = original_sum / 2
        print(f'{original_sum=} {target=}')
        answer = 0
        while current_sum > target:
            # print(f'{answer} {current_sum} {target=}')
            # print(f'  DEBUG: {nums=}')
            answer += 1
            highest_num = nums.pop()    # take last
            new_num = highest_num / 2
            # print(f'  {highest_num} -> {new_num}')
            current_sum -= new_num
            bisect.insort(nums, new_num)
        print(f'{answer} {current_sum} {target=}')
        # print(f'  DEBUG: {nums=}')
        return answer

