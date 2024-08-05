class Solution:
    def canChange(self, start: str, target: str) -> bool:

        # SHORTCUT: 'L' and 'R' pieces cannot move through (pass) each other.
        # Imagine the "shadow" of a string, created by removing all '_' pieces.
        # any legal move will preserve this shadow.  Therefore if Start and Target
        # don't have the same shadow, immediately return false.

        # print(f'\t\t {start=}')
        # print(f'\t\t{target=}')
        if start.replace('_', '') != target.replace('_', ''):
            print(f'Different shadows!')
            return 
        
        startIndexes = [
            (index, char)
            for index, char in enumerate(start)
            if char != '_'
        ]
        targetIndexes = [
            (index, char)
            for index, char in enumerate(target)
            if char != '_'
        ]
        assert len(startIndexes) == len(targetIndexes)
        check = [
            (
                'ERROR' if sChar != tChar else
                'OK L' if sChar == 'L' and tIndex <= sIndex else
                'BAD L' if sChar == 'L' and tIndex > sIndex else
                'OK R' if sChar == 'R' and tIndex >= sIndex else
                'BAD R' if sChar == 'R' and tIndex < sIndex else
                'UNKNOWN'
            )
            for ((sIndex, sChar), (tIndex, tChar)) in zip(startIndexes, targetIndexes)
        ]
        print(f'check: {dict(Counter(check))}')
        problems = [
            code
            for code in check
            if code not in ['OK L', 'OK R']
        ]
        print(f'{problems=}')
        
        return not problems

# NOTE: Runtime 213 ms Beats 29.36%
# NOTE: Memory 38.75 MB Beats 6.88%
