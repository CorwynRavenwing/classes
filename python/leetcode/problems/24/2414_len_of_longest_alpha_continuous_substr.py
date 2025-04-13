class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        Letter = lambda x: alphabet.index(x)
        adjacent = ''.join([
            ('+' if Letter(A) + 1 == Letter(B) else ' ')
            for (A, B) in pairwise(s)
        ])
        print(f'{adjacent=}')
        fragments = adjacent.split(' ')
        print(f'{fragments=}')
        sizes = tuple(map(len, fragments))
        print(f'{sizes=}')

        return max(sizes) + 1

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 635 ms Beats 5.20%
# NOTE: Memory 20.95 MB Beats 5.49%
