class Solution:
    def minFlips(self, target: str) -> int:
        
        values_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(target)
        ]
        print(f'{values_and_counts=}')

        (value, count) = values_and_counts[0]
        if value == '0':
            ignore = values_and_counts.pop(0)

        return len(values_and_counts)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 105 ms Beats 6.04%
# NOTE: Memory 22.88 MB Beats 5.13%
