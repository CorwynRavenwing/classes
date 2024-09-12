class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        colors_wrapped = colors + [colors[0]]
        diff_from_prior = [
            ('Y' if (A != B) else 'n')
            for (A, B) in pairwise(colors_wrapped)
        ]
        print(f'{diff_from_prior=}')
        diff_wrapped = diff_from_prior + [diff_from_prior[0]]
        alternating = [
            (A + B)
            for (A, B) in pairwise(diff_wrapped)
        ]
        print(f'{alternating=}')

        answer = len(
            tuple(
                filter(
                    lambda x: x == 'YY',
                    alternating
                )
            )
        )

        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 56 ms Beats 29.25%
# NOTE: Memory 16.64 MB Beats 5.76%
