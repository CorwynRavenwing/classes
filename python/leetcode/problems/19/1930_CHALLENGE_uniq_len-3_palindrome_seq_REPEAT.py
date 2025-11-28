class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # NOTE: any length-three palindrome will contain:
        # * any central letter
        # * the same letter both before and after that letter
        # therefore we compose all palindromes by precalculating
        # the letters *before* and *after* each position,
        # checking for letters that appear in *both* (uniquely),
        # and then composing the resultant palindrome (uniquely)

        def letters_seen_before(s: str) -> List[Set[str]]:
            # print(f'LSB({s})')
            answer = []
            partial = set()
            for char in s:
                partial = partial | {char}
                answer.append(partial)
            # append blank value and delete last value
            return [set()] + answer[:-1]
        
        def letters_seen_after(s: str) -> List[Set[str]]:
            REV = lambda L: tuple(reversed(L))
            rev_s = REV(s)
            rev_s = ''.join(rev_s)
            rev_answer = letters_seen_before(rev_s)
            return REV(rev_answer)
        
        def letters_seen_both(s: str) -> List[Set[str]]:
            before = letters_seen_before(s)
            after = letters_seen_after(s)
            return [
                B & A
                for (B, A) in zip(before, after)
            ]
        
        # print(f'{letters_seen_before(s)=}')
        # print(f'{letters_seen_after(s)=}')
        # print(f'{letters_seen_both(s)=}')

        answers = [
            ends + center + ends
            for center, matches in zip(s, letters_seen_both(s))
            for ends in matches
        ]
        # print(f'{answers=}')

        return len(set(answers))

# NOTE: Acceptance Rate 71.5% (medium)

# NOTE: re-created this after losing my computer
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 4596 ms Beats 5.11%
# NOTE: Memory 609.72 MB Beats 5.11%
