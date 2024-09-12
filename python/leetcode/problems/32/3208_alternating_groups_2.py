class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        # we borrow some code from 3206:
        
        colors_wrapped = colors + [colors[0]]
        problems = [
            # this is '1' for problems and '0' for okay
            (0 if (A != B) else 1)
            for (A, B) in pairwise(colors_wrapped)
        ]
        # print(f'{problems=}')
        problems_wrapped = problems + problems[:k]
        problems_partialSum = (0,) + tuple(accumulate(problems_wrapped))
        print(f'{problems_partialSum=}')
        count_of_problems = [
            problems_partialSum[i + k - 1] - problems_partialSum[i]
            for i in range(len(colors))
        ]
        print(f'{count_of_problems=}')

        answer = len(
            tuple(
                filter(
                    lambda x: x == 0,
                    count_of_problems
                )
            )
        )
        return answer

# NOTE: Runtime 793 ms Beats 13.68%
# NOTE: Memory 24.58 MB Beats 6.84%
