class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        letters_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(colors)
        ]
        print(f'{letters_and_counts=}')

        removable = ''.join([
            (
                letter * (count - 2)
            )
            for letter, count in letters_and_counts
            if count >= 3
        ])
        print(f'{removable=}')
        
        moves = Counter(removable)
        A = moves['A']
        B = moves['B']

        return A > B

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 231 ms Beats 8.16%
# NOTE: Memory 25.38 MB Beats 5.44%
