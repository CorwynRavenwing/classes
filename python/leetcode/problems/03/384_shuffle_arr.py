class Solution:

    def __init__(self, nums: List[int]):
        self.originalList = tuple(nums)
        return

    def reset(self) -> List[int]:
        return self.originalList

    def shuffle(self) -> List[int]:

        def fisher_yates_shuffle(nums: List[int]) -> List[int]:
            answer = list(nums)
            for i in reversed(range(len(nums))):
                j = randint(0, i)
                # print(f'[{i}]: [{j}] {answer=}')
                (answer[i], answer[j]) = (answer[j], answer[i])
            return tuple(answer)

        return fisher_yates_shuffle(self.originalList)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# NOTE: Acceptance Rate 59.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 84 ms Beats 5.09%
# NOTE: Memory 21.96 MB Beats 55.47%

# NOTE: without the debugging statement:
# NOTE: Runtime 51 ms Beats 6.10%
# NOTE: Memory 21.98 MB Beats 55.47%
# NOTE: a bit faster, same memory
