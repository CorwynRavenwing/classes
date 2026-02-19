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

# NOTE: Acceptance Rate 66.5% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 127 ms Beats 7.30%
# NOTE: Memory 22.81 MB Beats 8.06%
