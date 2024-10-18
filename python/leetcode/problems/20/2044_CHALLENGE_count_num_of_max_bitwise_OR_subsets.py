class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        # PROCESS: (1a) a bitwise OR subset will get *larger* or
        # stay the same, when you add more numbers into the
        # subset.
        # (1b) therefore, the maximum OR value of any subset
        # must equal the OR value of the entire array.
        # (2) since we're doing pick/don't pick, finding subsets
        # and not contiguous subarrays, and then performing
        # bitwise OR (a transitive/commutative action) on them,
        # element order *does not* matter.
        # (3) the maximum bitwise OR value, will be the number
        # composed of all the bits that are set in any number
        # in the array.
        # (4) the number of subsets with this maximum, will be the
        # number of different ways you can get (at least) one
        # number with each bit set.
        # (5) nums.length is <= 16; therefore we can enumerate all
        # possible subsets in just 2^16 == 65536 possibilities.
        # This should be quick enough.  In cases where nums.length
        # is shorter, we can skip large pieces of that worst-case
        # search space.

        OR = lambda x: reduce(operator.__or__, tuple(x), 0)

        maxValue = OR(nums)
        print(f'{maxValue=}')

        def bitArray(bitset: int) -> List[bool]:
            answer = []
            while bitset:
                answer.append(bitset % 2)
                bitset //= 2
            return answer

        def choose_subset(nums: List[int], bitset: int) -> List[int]:
            return [
                val
                for (val, bit) in zip(nums, bitArray(bitset))
                if bit
            ]

        N = len(nums)
        answer = 0
        for bitset in range(2 ** N):
            subset = choose_subset(nums, bitset)
            value = OR(subset)
            if value == maxValue:
                answer += 1
            # print(f'[{answer}] {bitset:0{N}b}: {value}={subset}')

        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 2515 ms Beats 5.18%
# NOTE: Memory 16.77 MB Beats 32.63%
