class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i, A in enumerate(numbers):
            print(f'{i=} {A=}')
            if A * 2 > target:
                raise Exception(f'{A=} * 2 ({A*2}) > {target=}')
            B = target - A
            j = bisect_left(numbers, B, i + 1)
            if j >= len(numbers):
                print(f'  {j=} {B=} OOB')
                continue
            if B != numbers[j]:
                print(f'  {j=} {B=} {numbers[j]=} WRONG')
                continue
            print(f'  {j=} {B=} {numbers[j]=} YES')
            return [i+1, j+1]
        return [None,None]

# NOTE: Runtime 134 ms Beats 6.08%
# NOTE: Memory 17.91 MB Beats 41.17%
