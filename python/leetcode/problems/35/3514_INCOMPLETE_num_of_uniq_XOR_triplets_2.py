class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        def DP_pick(xor_so_far: int, nums_idx: int, triplet_idx: int) -> List[int]:
            N = nums[nums_idx]
            value = xor_so_far ^ N   # XOR
            if triplet_idx == 1:
                # last value of triplet
                return { value }
            else:
                # other value of triplet
                return DP(
                    value,              # precompute XOR so far
                    nums_idx,           # no change b/c i<=j<=k: can be equal
                    triplet_idx - 1     # one less triplet
                )
        
        def DP_skip(xor_so_far: int, nums_idx: int, triplet_idx: int) -> List[int]:
            return DP(
                xor_so_far,         # no change to XOR
                nums_idx + 1,       # skip this index
                triplet_idx         # try again for this index
            )

        @cache
        def DP(xor_so_far: int, nums_idx: int, triplet_idx: int) -> List[int]:
            if triplet_idx <= 0:
                # ran out of values in triplet
                # SHOULD NOT GET HERE
                return set()
            try:
                _ = nums[nums_idx]
            except IndexError:
                # ran out of values in nums
                return set()
            return (
                DP_pick(xor_so_far, nums_idx, triplet_idx)
                |       # UNION
                DP_skip(xor_so_far, nums_idx, triplet_idx)
            )
        
        possibles = DP(0, 0, 3)
        print(f'{possibles=}')
        return len(possibles)

# NOTE: Acceptance Rate 34.2% (medium)

# NOTE: Incomplete; Time Exceeded without cache; Memory Exceeded with cache
