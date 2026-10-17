class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        def g_pairs(nums: List[int]) -> List[List[int]]:
            squares = [
                x * x
                for x in nums
            ]
            # print(f'raw {squares=}')
            squares.sort()
            # print(f'sorted {squares=}')
            while squares:
                A = squares.pop(-1)  # from high end
                if not squares:
                    B = 0
                else:
                    B = squares.pop(0)   # from low end
                yield (A, B)
            return
        
        answers = [
            A - B
            for (A, B) in g_pairs(nums)
        ]
        print(f'{answers=}')

        return sum(answers)

# NOTE: Acceptance Rate 63.7% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4708 ms Beats 5.49%
# NOTE: Memory 34.94 MB Beats 5.49%
