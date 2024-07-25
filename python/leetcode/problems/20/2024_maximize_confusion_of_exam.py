class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        # we borrow some code from #1004:
        
        bestSoFar = 0

        print(f'Trying to minimize TRUES:')
        L = 0
        R = 0
        windowSize = (R - L)
        truesInWindow = 0
        while R <= len(answerKey):
            # print(f'[{L}:{R}]={truesInWindow}')
            # print(f'  DEBUG: {windowSize=} frag={answerKey[L:R]}')
            if truesInWindow <= k:
                # print(f'  {truesInWindow} zeros <= {k}: expand window to Right')
                bestSoFar = max(bestSoFar, windowSize)  # BEFORE changing windowsize
                if R >= len(answerKey):
                    print(f'    Ran out of room: quit')
                    break
                right = answerKey[R] # BEFORE changing R
                R += 1
                windowSize = (R - L)
                if right == 'T':
                    truesInWindow += 1
            else:
                # print(f'  {truesInWindow} zeros > {k}: shrink window from Left')
                # no need to check bestSoFar: it is getting worse here
                if L > len(answerKey):
                    print(f'    Ran out of room: quit')
                    break
                left = answerKey[L]  # BEFORE changing L
                L += 1
                windowSize = (R - L)
                if left == 'T':
                    truesInWindow -= 1
                
        print(f'Trying to minimize FALSES:')
        L = 0
        R = 0
        windowSize = (R - L)
        falsesInWindow = 0
        while R <= len(answerKey):
            # print(f'[{L}:{R}]={falsesInWindow}')
            # print(f'  DEBUG: {windowSize=} frag={answerKey[L:R]}')
            if falsesInWindow <= k:
                # print(f'  {falsesInWindow} zeros <= {k}: expand window to Right')
                bestSoFar = max(bestSoFar, windowSize)  # BEFORE changing windowsize
                if R >= len(answerKey):
                    print(f'    Ran out of room: quit')
                    break
                right = answerKey[R] # BEFORE changing R
                R += 1
                windowSize = (R - L)
                if right == 'F':
                    falsesInWindow += 1
            else:
                # print(f'  {falsesInWindow} zeros > {k}: shrink window from Left')
                # no need to check bestSoFar: it is getting worse here
                if L > len(answerKey):
                    print(f'    Ran out of room: quit')
                    break
                left = answerKey[L]  # BEFORE changing L
                L += 1
                windowSize = (R - L)
                if left == 'F':
                    falsesInWindow -= 1

        return bestSoFar

