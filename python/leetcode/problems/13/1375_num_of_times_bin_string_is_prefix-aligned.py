class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flip = 0   # will never be in "flips" because of 1-indexing
        answer = 0
        for index, flip in enumerate(flips):
            one_based_index = index + 1
            max_flip = max(flip, max_flip)
            if one_based_index == max_flip:
                answer += 1
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 31 ms Beats 71.30%
# NOTE: Memory 22.07 MB Beats 75.90%
