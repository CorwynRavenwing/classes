class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        numbers_and_counts = [
            (key, len(tuple(values)))
            for key, values in groupby(s)
        ]
        print(f'{numbers_and_counts=}')
        counts = [
            count
            for number, count in numbers_and_counts
        ]
        print(f'{counts=}')
        
        substrings =  [
            min(A, B)
            for (A, B) in pairwise(counts)
        ]
        print(f'{substrings=}')

        return sum(substrings)

# NOTE: Accepted on first Submit
# NOTE: Runtime 190 ms Beats 8.24%
# NOTE: O(N)
# NOTE: Memory 20.13 MB Beats 5.35%
# NOTE: O(N)
