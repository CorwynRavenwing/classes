class Solution:
    def maximumLength(self, s: str) -> int:
        
        # we borrow some code from #2981:
        
        withCounts = [
            (L, 1)
            for L in s
        ]
        # print(f'{withCounts=}')
        for i in range(1, len(withCounts)):
            (prevLetter, prevCount) = withCounts[i - 1]
            (nextLetter, nextCount) = withCounts[i]
            # add counts together for same letter
            if prevLetter == nextLetter:
                withCounts[i - 1] = None
                withCounts[i] = (prevLetter, prevCount + nextCount)
        # print(f'{withCounts=}')
        withCounts = [
            W
            for W in withCounts
            if W is not None
        ]
        # print(f'{withCounts=}')

        specialCounts = Counter()
        for W in withCounts:
            print(f'{W=}')
            specialCounts[W] += 1
            (Letter, count) = W
            for i, C in enumerate(reversed(range(1, count))):
                W2 = (Letter, C)
                specialCounts[W2] += (i + 2)    # 1 for 0-index, 1 for we already did W
                print(f'  +{W2}')
                if specialCounts[W2] >= 3:
                    print(f'    Stop')
                    break
        print(f'{specialCounts=}')

        thrice = [
            W
            for W, count in specialCounts.items()
            if count >= 3
        ]
        print(f'{thrice=}')

        answers = [
            Size
            for (Letter, Size) in thrice
        ]
        print(f'{answers=}')
        return max(answers, default=-1)

# NOTE: reused code from 2981: just needed to remove some print()s
# NOTE: Runtime 1668 ms Beats 28.02%
# NOTE: Memory 56.94 MB Beats 25.27%
