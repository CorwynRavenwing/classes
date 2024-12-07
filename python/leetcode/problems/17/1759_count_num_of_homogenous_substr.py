class Solution:
    def countHomogenous(self, s: str) -> int:

        mod = 10 ** 9 + 7
        
        def Nchoose2(N: int) -> int:
            return N * (N - 1) // 2

        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(s)
        ]
        print(f'{letters_and_counts=}')

        answer = [
            Nchoose2(count + 1)
            for (letter, count) in letters_and_counts
        ]
        print(f'{answer=}')

        return sum(answer) % mod

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 96 ms Beats 28.71%
# NOTE: Memory 23.55 MB Beats 5.14%
