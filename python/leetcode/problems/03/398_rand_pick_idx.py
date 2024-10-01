class Solution:

    def __init__(self, nums: List[int]):
        self.IndexesByValue = {}
        for index, N in enumerate(nums):
            self.IndexesByValue.setdefault(N, [])
            self.IndexesByValue[N].append(index)
        return

    def pick(self, target: int) -> int:
        indexes = self.IndexesByValue[target]
        return random.choice(indexes)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 288 ms Beats 33.64%
# NOTE: Memory 26.79 MB Beats 13.43%
