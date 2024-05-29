class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        answer = 0
        for N in numSet:
            if (N != -2_147_483_648) and ((N - 1) in numSet):
                # print(f'skip {N}: not first')
                # not at bottom of a group
                continue
            if N + answer not in numSet:
                # print(f'skip {N}: len < {answer}')
                continue
            # at bottom of a group
            L = 1
            while (N + L) in numSet:
                L += 1
            # print(f'  found group length {L} starting at {N}')
            answer = max(answer, L)
        return answer

# NOTE: 338 ms; Beats 83.46% of users with Python3

