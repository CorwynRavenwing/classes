class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        sort1 = sorted(s1)
        sort2 = sorted(s2)
        diffs = [
            (
                '+' if A > B else
                '-' if A < B else
                '0' if A == B else
                '?'
            )
            for (A, B) in zip(sort1, sort2)
        ]
        print(f'{diffs=}')
        assert '?' not in diffs

        if '+' not in diffs:
            return True
        if '-' not in diffs:
            return True
        return False

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 146 ms Beats 9.09%
# NOTE: Memory 20.71 MB Beats 5.24%
