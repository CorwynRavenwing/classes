class Solution:
    def frequencySort(self, s: str) -> str:

        counts = Counter(s)
        print(f'{counts=}')
        freq = counts.most_common()
        print(f'{freq=}')
        groups = [
            letter * count
            for (letter, count) in freq
        ]
        print(f'{groups=}')
        
        return ''.join(groups)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 45 ms Beats 63.53%
# NOTE: Memory 17.83 MB Beats 56.82%
