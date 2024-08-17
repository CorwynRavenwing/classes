class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        # Constraint: arrays[i] is sorted in ascending order.
        # SHORTCUT: therefore arrays[i][0] is min and arrays[i][-1] is max

        (minSoFar, maxSoFar) = (None, None)
        answers = []
        for A in arrays:
            (thisMin, thisMax) = (A[0], A[-1])
            print(f'{(thisMin, thisMax)=}')
            if minSoFar is None:
                (minSoFar, maxSoFar) = (thisMin, thisMax)
                print(f'{  (minSoFar, maxSoFar)=}')
                continue
            answers.append(maxSoFar - thisMin)
            answers.append(thisMax - minSoFar)
            print(f'  add answers {answers[-2:]}')
            maxSoFar = max(maxSoFar, thisMax)
            minSoFar = min(minSoFar, thisMin)
            print(f'{  (minSoFar, maxSoFar)=}')
        
        print(f'{answers=}')
        return max(answers)
# NOTE: At first, this was a Subscription-only puzzle.  They fixed it.
# NOTE: Success on first Run; Accept on first Submit :-)
# NOTE: Runtime 1658 ms Beats 5.21%
# NOTE: Memory 42.54 MB Beats 51.30%
