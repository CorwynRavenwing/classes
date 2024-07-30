class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:

        beans.sort()
        leftSum = 0
        rightSum = sum(beans)
        rightLen = len(beans)
        answers = []
        for B in beans:
            ans = leftSum + rightSum - (rightLen * B)
            answers.append(ans)
            # print(f'{B=} {leftSum=} {rightSum=} {rightLen=}: {ans=}')
            leftSum += B
            rightSum -= B
            rightLen -= 1

        return min(answers)
# NOTE: Runtime 927 ms Beats 68.31%
# NOTE: O(N log N)
# NOTE: Memory 30.27 MB Beats 77.05%
# NOTE: O(N)
