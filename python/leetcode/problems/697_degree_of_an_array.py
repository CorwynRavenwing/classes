from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        def degree_of(nums: List[int]) -> int:
            # print(f"{nums=}")
            C = Counter(nums)
            # print(f"  {C=}")
            V = C.values()
            # print(f"    {V=}")
            M = max(V) if V else 0
            # print(f"      {M=}")
            # print(f"degree {len(nums)} -> {M}")
            return M
        
        def shrink_from_left(nums: List[int], degree: int) -> List[int]:
            while degree_of(nums[1:]) == degree:
                # truncate first character, and any copies
                junk = nums[0]
                while nums[0] == junk:
                    nums = nums[1:]
            return nums

        def shrink_from_right(nums: List[int], degree: int) -> List[int]:
            while degree_of(nums[:-1]) == degree:
                # truncate last character, and any copies
                junk = nums[-1]
                while nums[-1] == junk:
                    nums = nums[:-1]
            return nums
            
        degree = degree_of(nums)
        
        from_left = shrink_from_left(nums, degree)
        from_left = shrink_from_right(from_left, degree)

        from_right = shrink_from_right(nums, degree)
        from_right = shrink_from_left(from_right, degree)

        return min(len(from_left), len(from_right))

