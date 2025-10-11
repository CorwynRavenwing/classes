class Solution:
    def maxArea(self, height: List[int]) -> int:

        @cache
        def DP(i: int, j: int) -> int:
            # print(f'DP({i},{j})')
            if i >= j:
                # print(f'  -> no')
                return 0
            hI = height[i]
            hJ = height[j]
            area = (j - i) * min(hI, hJ)
            # print(f'  -> {area=} = ({j-i=}) * {min(hI,hJ)=}')
            answers = [area]
            if hI == hJ:
                answers.append(
                    DP(i + 1, j)
                )
                answers.append(
                    DP(i, j - 1)
                )
            elif hI < hJ:
                answers.append(
                    DP(i + 1, j)
                )
            elif hI > hJ:
                answers.append(
                    DP(i, j - 1)
                )
            # print(f'  -> {answers=}')
            return max(answers)

        return DP(0, len(height) - 1)

# NOTE: Acceptance Rate 58.4% (medium)

# NOTE: Runtime 5447 ms Beats 5.03%
# NOTE: Memory 280.80 MB Beats 24.76%

# NOTE: re-ran for challenge:
# NOTE: Runtime 5015 ms Beats 5.19%
# NOTE: Memory 280.01 MB Beats 23.74%
