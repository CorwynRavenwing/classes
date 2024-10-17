class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        # PROCESS:
        # No value GT right is allowed to be in any answer subarray,
        # because that value will be the maximum, making the subarray invalid.
        # A value LT left *is* allowed to be in an answer subarray,
        # but *not* subarrays containing *only* LT values.
        # Therefore we actually don't care about the values themselves, only
        # whether they are LT left, GT right, or between them (inclusive).

        def Triangle(X: int) -> int:
            return (X) * (X + 1) // 2

        codes = [
            (
                'OK' if left <= N <= right else
                'LT' if N < left else
                'GT' if N > right else
                '??'
            )
            for N in nums
        ]
        print(f'{codes=}')

        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(codes)
        ]
        print(f'{letters_and_counts=}')

        answer = 0
        this_section = 0
        for (code, count) in letters_and_counts:
            print(f'{code=} {count=}')
            if code == 'OK':
                this_section += count
                print(f'  {answer=} {this_section=}')
            elif code == 'LT':
                this_section += count
                answer -= Triangle(count)
                print(f'  {answer=} {this_section=}')
            elif code == 'GT':
                answer += Triangle(this_section)
                this_section = 0
                print(f'  {answer=} {this_section=}')
            else:
                raise Exception(f'Error: invalid {code=}, should be LT/OK/GT')
        print(f'After:')
        answer += Triangle(this_section)
        this_section = 0
        print(f'  {answer=} {this_section=}')

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 561 ms Beats 5.09%
# NOTE: Memory 27.16 MB Beats 13.03%
