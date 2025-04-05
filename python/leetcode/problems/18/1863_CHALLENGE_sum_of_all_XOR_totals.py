class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        # format: answers[xor_value] == count
        answers = {
            0: 1
        }
        
        for N in nums:
            print(f'{N=}')
            for (A, count) in tuple(answers.items()):
                print(f'  {A}: {count}')
                new_A = A ^ N
                answers.setdefault(new_A, 0)
                answers[new_A] += count
                print(f'  answers[{new_A}] += {count}')
        print(f'{answers=}')
        retval = 0
        for (A, count) in answers.items():
            print(f'  {A}: {count}')
            retval += A * count
        return retval

# NOTE: re-ran for challenge:
# NOTE: Runtime 3 ms Beats 83.33%
# NOTE: Memory 17.83 MB Beats 41.01%
