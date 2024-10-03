class Solution:
    # we borrow some code from #1004:

    def longestRunOfX(self, X: str, haystack: List[str], k: int) -> int:
        L = 0
        R = 0
        windowSize = (R - L)
        otherLettersInWindow = 0
        bestSoFar = 0
        while R <= len(haystack):
            # print(f'[{L}:{R}]={otherLettersInWindow}')
            # print(f'  DEBUG: {windowSize=} frag={haystack[L:R]}')
            if otherLettersInWindow <= k:
                # print(f'  {otherLettersInWindow} zeros <= {k}: expand window to Right')
                bestSoFar = max(bestSoFar, windowSize)  # BEFORE changing windowsize
                if R >= len(haystack):
                    # print(f'    Ran out of room: quit')
                    break
                right = haystack[R] # BEFORE changing R
                R += 1
                windowSize = (R - L)
                if right != X:
                    otherLettersInWindow += 1
            else:
                # print(f'  {otherLettersInWindow} other letters > {k}: shrink window from Left')
                # no need to check bestSoFar: it is getting worse here
                if L > len(haystack):
                    # print(f'    Ran out of room: quit')
                    break
                left = haystack[L]  # BEFORE changing L
                L += 1
                windowSize = (R - L)
                if left != X:
                    otherLettersInWindow -= 1
                
        return bestSoFar

    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(s)
        print(f'{letters=}')
        answers = {
            X: self.longestRunOfX(X, s, k)
            for X in letters
        }
        print(f'{answers=}')
        return max(answers.values())

# NOTE: re-used entire prior version, with minor changes
# NOTE: Accepted on first Submit
# NOTE: Runtime 425 ms Beats 5.00%
# NOTE: O(N)
# NOTE: Memory 16.61 MB Beats 41.85%
# NOTE: O(N)
