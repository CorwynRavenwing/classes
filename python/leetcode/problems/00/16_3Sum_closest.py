class Solution:

    # we borrow some code from question #18:

    def findClosest(self, nums: List[int], target: int) -> int:
        # nums need not be sorted: possibles will be sorted later
        # print(f'      [0] FC({nums[:5]},{target})')
        if not nums:
            # print(f'      [0] no input')
            return float('+inf')
        possibles = [
            (abs(target - N), N)
            for N in nums
        ]
        possibles.sort()
        # print(f'      [0] {possibles=}')
        (dist, N) = possibles[0]
        return N
        
    def numberClosest(self, nums: List[int], target: int) -> int:
        # nums is already sorted
        # print(f'    [1] NC({nums[:5]},{target})')
        index = bisect_left(nums, target)
        if index > 0:
            index -= 1
        possibles = nums[index:min(index + 3, len(nums))]
        # print(f'    [1] {possibles=}')
        N = self.findClosest(possibles, target)
        return N

    def twoSumClosest(self, nums: List[int], target: int) -> int:
        # nums is already sorted
        # print(f'  [2] 2SC({nums[:5]},{target})')
        possibles = []
        for i, N in enumerate(nums):
            T = target - N
            NC = N + self.numberClosest(nums[i + 1:], T)
            # print(f'  [2] {i=} {N=} {T=} {NC=}')
            possibles.append(NC)
        # print(f'  [2] {possibles=}')
        return self.findClosest(possibles, target)

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # print(f'[3] 3SC({nums[:5]},{target})')
        possibles = []
        for i, N in enumerate(nums):
            T = target - N
            NC = N + self.twoSumClosest(nums[i + 1:], T)
            # print(f'[3] {i=} {N=} {T=} {NC=}')
            possibles.append(NC)
        # print(f'[3] {possibles=}')
        return self.findClosest(possibles, target)

# NOTE: Runtime 4126 ms Beats 5.01%
# NOTE: Memory 16.70 MB Beats 42.20%
