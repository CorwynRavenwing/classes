class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:

        sumEverything = sum(heights)
        answers = []
        for peak in range(len(heights)):
            print(f'{peak=}')
            deletes = 0
            newHeights = heights.copy()
            for i in range(peak + 1, len(newHeights)):
                prev = newHeights[i - 1]
                curr = newHeights[i]
                if curr > prev:
                    # print(f'  [{i}] too high ({curr}>{prev})')
                    deletes += (curr - prev)
                    newHeights[i] = prev
            for i in reversed(range(0, peak)):
                prev = newHeights[i + 1]
                curr = newHeights[i]
                if curr > prev:
                    # print(f'  [{i}] too high ({curr}>{prev})')
                    deletes += (curr - prev)
                    newHeights[i] = prev
            # print(f'  {newHeights=}')

            remain = sumEverything - deletes
            print(f'  {deletes=} {remain=}')
            answers.append(remain)
        
        # print(f'{answers=}')
        return max(answers)
# NOTE: Runtime 872 ms Beats 59.38%
# NOTE: Memory 16.97 MB Beats 11.08%
