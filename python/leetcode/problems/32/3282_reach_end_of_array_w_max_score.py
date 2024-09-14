class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:

        # Hint #1 says "it can be proven that from each index i,
        #   the optimal solution is to jump to the nearest index
        #   j > i such that nums[j] > nums[i]."
        # However, I refuse to use this hint until I can, in fact,
        #   prove that.

        # PROOF:
        # assume indexes [i, j, k] with values [A B C] exist,
        #   and we are currently at index i=A and are planning
        #   to eventually jump to index k=C.
        # Should we first jump to index j=B on our way?
        # Our score if we go via index j is:
        #   Sijk === A(j-i) + B(k-j)
        # our score if we go directly to index k is:
        #   Si_k === A(k-i)
        #   == A(k-j+j-i)
        #   == A(j-i) + A(k-j)
        #   which > Sijk if and only if A > B

        # Therefore, yes, we should always jump by way of each index
        # whose number is higher than our current index.

        # We're basically getting a score of nums[i] for each number
        #   we jump past; when we stop at j, we will start getting
        #   nums[j] for each number we jump past after that.
        #   By swapping for larger numbers, we're raising our
        #   total final score.

        # one-liner that should be equivalent:
        # return sum(tuple(accumulate(nums, max))[:-1])
        # i.e. get running-total maximum; throw out the last one; sum them.

        i = 0
        score = 0
        while i < len(nums) - 1:
            A = nums[i]
            # print(f'{i=} {A=}')
            for j in range(i + 1, len(nums)):
                B = nums[j]
                # print(f'  {j=} {B=}')
                if B > A or j == len(nums) - 1:
                    S = (j - i) * A
                    print(f'Jump from {i}({A}) to {j}({B}) for a score of {S}')
                    score += S
                    i = j
                    break   # break j == next i
        return score

# NOTE: Accepted on second Submit (first was Output Exceeded)

# NOTE: The "Hint 1" method, which should be O(N)
# NOTE: Runtime 1224 ms Beats 28.95%
# NOTE: Memory 31.67 MB Beats 35.53%

# NOTE: The "probably equivalent one-liner" method, also O(N)
# NOTE: Runtime 1185 ms Beats 44.91%
# NOTE: Memory 30.69 MB Beats 98.79%

# NOTE: The one-liner is much better in every metric!
