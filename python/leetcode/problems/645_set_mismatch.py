from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # print(f"{nums=}")
        L = len(nums)
        counts = Counter(nums)
        # print(f"{counts=}")
        (twice, missing) = (None, None)
        for i in range(1, L+1):
            C = counts[i]
            # print(f"  {i=} {C=}")
            if C == 2:
                twice = i
            elif C == 0:
                missing = i
            elif C == 1:
                pass
            else:
                raise Exception(f'Count of {i} is {C}, not in range [0,1,2]')
        return [twice, missing]

