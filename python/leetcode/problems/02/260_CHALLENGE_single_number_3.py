class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        if len(nums) == 2:
            # two singletons must === the entire list
            return nums
        
        answers = []
        nums.sort()
        print(f'sorted {nums=}')
        prior = nums[0] - 1     # guaranteed different from all elements
        count = 0
        for N in nums:
            print(f'{prior=} {N=} {count=}')
            if prior == N:
                count += 1
            else:
                if count == 1:
                    print(f'{prior} once')
                    answers.append(prior)
                    if len(answers) == 2:
                        print(f'return early')
                        return answers
                count = 1
                prior = N
        print(f'{prior=} {N=} {count=}')
        if count == 1:
            print(f'{prior} once')
            answers.append(prior)
            if len(answers) == 2:
                print(f'return at end')
                return answers
        print(f'unsure how we got here: {answers=}')
        return answers

# NOTE: Runtime 61 ms Beats 41.98%
# NOTE: Memory 18.80 MB Beats 34.80%
