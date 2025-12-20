class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        inverse = tuple(zip(*strs))
        print(f'{inverse=}')
        
        is_sorted = lambda L: (tuple(L) == tuple(sorted(L)))
        wrong = [
            ''.join(I)
            for I in inverse
            if not is_sorted(I)
        ]
        print(f'{wrong=}')

        return len(wrong)

# NOTE: Acceptance Rate 75.0% (easy)

# NOTE: Accepted on second Run (reversed parity)
# NOTE: Accepted on Submit Run
# NOTE: Runtime 83 ms Beats 15.80%
# NOTE: Memory 20.26 MB Beats 7.33%
