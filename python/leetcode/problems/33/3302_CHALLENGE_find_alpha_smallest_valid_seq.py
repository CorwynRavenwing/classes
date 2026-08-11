class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        
        def DP_take(i: int, diffs_left: int, len_left: int) -> Tuple[int]:
            A = word1[i]
            B = word2[i]
            if (A != B):
                print(f'  [{A}<>{B}]')
                if not diffs_left:
                    print(f'  NO:  out of differences')
                    return None
                return DP(i + 1, diffs_left - 1, len_left - 1)
            else:
                print(f'  ({A}=={B})')
                return DP(i + 1, diffs_left, len_left - 1)

        def DP_skip(i: int, diffs_left: int, len_left: int) -> Tuple[int]:
            # we don't actually care about A or B
            return DP(i + 1, diffs_left, len_left)

        # @cache
        def DP(i: int, diffs_left: int, len_left: int) -> Tuple[int]:
            print(f'DP({i},{diffs_left},{len_left}):')
            if (len_left == 0):
                print(f'  YES: end of chain')
                return ()
            try:
                _ = word1[i]
                _ = word2[i]
            except IndexError:
                print(f'  NO:  out of values')
                return None
            Take = DP_take(i, diffs_left, len_left)
            if Take is not None:
                print(f'  Yes: Take')
                return (i,) + Take
            Skip = DP_skip(i, diffs_left, len_left)
            if Skip is not None:
                print(f'  Yes: Skip')
                return (i,) + Skip
            return None
        
        return DP(0, 1, len(word2))

# NOTE: Acceptance Rate 23.4% (medium)

# NOTE: Incomplete: this didn't actually work for some values
