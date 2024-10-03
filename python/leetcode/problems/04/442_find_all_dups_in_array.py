class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # with the constraints of: O(N) time, O(1) space
        # which makes all the useful, reasonable answers illegal.

        # (0): Brute force -> O(N^2) time, O(1) space.
        # answer = []
        # for i, N in enumerate(nums):
        #     for j in range(len(nums)):
        #         if j <= i:
        #             continue
        #         M = nums[j]
        #         if N == M:
        #             answer.append(N)
        #             break   # break j == next i
        # return answer

# NOTE: Time Limit Exceeded, as it should be.

        # (1): Sort -> O(N log N) time, O(1) space.
        # answer = []
        # nums.sort()
        # for i in range(1, len(nums)):
        #     N = nums[i - 1]
        #     M = nums[i]
        #     if N == M:
        #         answer.append(N)
        # return answer

# NOTE: Runtime 270 ms Beats 38.73%
# NOTE: Memory 23.80 MB Beats 92.33%
# NOTE: ... despite breaking the rules.

        # (2): Counter, other hash maps -> O(N) time, O(N) space.
        # counts = Counter(nums)
        # answer = [
        #     N
        #     for N, count in counts.items()
        #     if count == 2
        # ]
        # return answer

# NOTE: Runtime 252 ms Beats 80.80%
# NOTE: Memory 25.52 MB Beats 18.50%
# NOTE: ... again, despite breaking the rules.

        # (3): sets -> O(N) time, O(N) space.
        # answer = []
        # seen = set()
        # for N in nums:
        #     if N in seen:
        #         answer.append(N)
        #     else:
        #         seen.add(N)
        # return answer

# NOTE: Runtime 240 ms Beats 96.45%
# NOTE: Memory 26.10 MB Beats 8.06%
# NOTE: ... didn't Batman tell "me cheaters never prosper"?  Hmmm.

        # (4): abusing the input vector and pretending that it
        #   (A) doesn't take up any space, and
        #   (B) is okay to overwrite your inputs randomly
        # but it does give us the O(N) time O(1) space demanded.
        
        answer = []
        for i in range(len(nums)):
            N = abs(nums[i])    # because some idiot might have made it negative ...
            flag = nums[N - 1]  # map [1..N] values onto [0..N-1] indexes
            if flag < 0:
                answer.append(N)
            else:
                nums[N - 1] *= -1   # ... like me, for example
        return answer

# NOTE: Accepted on first Run (each version)
# NOTE: Accepted on first Submit (each version)
# NOTE: Runtime 260 ms Beats 63.63%
# NOTE: Memory 24.60 MB Beats 70.66%
# NOTE: ... so, noticeably worse then most of the "illegal" versions
#       when this one is supposed to be so much smaller and faster
#       (but hokey and dangerous)
# NOTE: I'm not a fan of tricks like this.  It's "clever"
#       in the "what did my idiot predecessor think he was
#       doing?" sense of the word.
