class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        changes = [
            (
                '+' if A < B
                else
                '-' if A > B
                else
                '=' if A == B
                else
                '?'
            )
            for (A, B) in pairwise(nums)
        ]
        print(f'{changes=}')
        if '?' in changes:
            raise Exception(f'Error: found "?" in {changes=}')
        
        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(changes)
        ]
        print(f'{letters_and_counts=}')

        answers = [
            (
                count if letter == '+'
                else
                count if letter == '-'
                else
                0 if letter == '='
                else
                Exception(f'Invalid {letter=}')
            )
            for letter, count in letters_and_counts
        ]
        print(f'{answers=}')

        return max(answers, default=0) + 1

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 13.83%
# NOTE: Memory 17.98 MB Beats 11.65%
