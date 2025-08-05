class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        def targetCharBecomes1(s: str, target: str) -> List[int]:
            return [
                (1 if (ch == target) else 0)
                for ch in s
            ]
        
        # adds a leading 0 onto each answer, for "sum of no elements"
        partialSum = lambda x: (0,) + tuple(accumulate(tuple(x)))

        REV = lambda x: tuple(reversed(tuple(x)))
        
        letterList = 'abc'
        counts = Counter(s)
        for letter in letterList:
            if counts[letter] < k:
                print(f'No: not enough {letter} ({counts[letter]} < {k})')
                return -1
        
        ones = [
            targetCharBecomes1(s, letter)
            for letter in letterList
        ]
        sums = [
            partialSum(One)
            for One in ones
        ]
        revs = [
            partialSum(REV(One))            
            for One in ones
        ]
        # for index, letter in enumerate(letterList):
        #     print(f'ones[{letter}]= {ones[index]}')
        #     print(f'sums[{letter}]= {sums[index]}')
        #     print(f'revs[{letter}]= {revs[index]}')
        #     print()
        
        @cache
        def firstSumWithCount(count: int, index: int) -> int:
            # index == which letter this is for
            Sum = sums[index]
            answer = bisect_left(Sum, count)
            # print(f'found {count=} at pos#{answer} in sums[{index}]')
            return answer
        
        answer = float('+inf')
        for rightCount, ABC in enumerate(zip(*revs)):
            # print(f'R={rightCount}: ABC={ABC}', end=' ')
            # print(f'R={rightCount} ', end='')
            if rightCount >= answer:
                print(f'STOP: R={rightCount} >= A={answer}')
                break
            leftCount = leftCount = max([
                firstSumWithCount(
                    max(0, k - count),  # needed
                    index
                )
                for index, count in enumerate(ABC)
            ])
            totalCount = leftCount + rightCount
            answer = min(answer, totalCount)
            # print(f'L={leftCount} T={totalCount} A={answer}')
        
        return answer

# NOTE: Runtime 753 ms Beats 12.97%
# NOTE: Memory 63.90 MB Beats 5.34%

# NOTE: re-ran for challenge:
# NOTE: Runtime 731 ms Beats 6.11%
# NOTE: Memory 63.20 MB Beats 5.36%
