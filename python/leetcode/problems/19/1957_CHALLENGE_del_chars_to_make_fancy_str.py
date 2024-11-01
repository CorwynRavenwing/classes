class Solution:
    def makeFancyString(self, s: str) -> str:
        
        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(s)
        ]
        # print(f'orig={letters_and_counts}')
        max_of_two = [
            (key, min(2, length))
            for (key, length) in letters_and_counts
        ]
        # print(f'max2={max_of_two}')
        recombine = [
            key
            for (key, length) in max_of_two
            for i in range(length)
        ]
        # print(f'fixd={recombine}')

        return ''.join(recombine)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (first two were Output Exceeded)
# NOTE: Runtime 531 ms Beats 13.51%
# NOTE: Memory 35.30 MB Beats 5.17%
