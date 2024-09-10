class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:

        # we borrow some code from #3180
        # ... and it times out.  Let's try some bitset operations instead.

        rewardValues = sorted(set(rewardValues))
        # print(f'new {rewardValues=}')

        # per Hint 3,
        # dp[i][j] = dp[i - 1][j - rewardValues[i]] if j - rewardValues[i] < rewardValues[i]
        # translating k === j - rewardValues[i]:
        # dp[i][k + rewardValues[i]] = dp[i - 1][k] if k < rewardValues[i]

        # set up array of bitstrings:
        # bit #0 is always set (we can always have zero points)
        dp = [1] *  len(rewardValues)

        # base case:
        # set bit #rv[0] only for byte #0
        i = 0
        rv_bit = (1 << rewardValues[i])
        dp[i] |= rv_bit
        # print(f'  {i=} rv={rewardValues[i]}')
        # # print(f'  {i=} {rv_bit  =} {rv_bit:b}')
        # print(f'{i=} {dp[i]=}')
        # # print(f'{i=} {dp[i]=} {dp[i]:b}')

        for i in range(1, len(rewardValues)):
            dp_prev = dp[i - 1]
            rv_bit = (1 << rewardValues[i])
            mask = rv_bit - 1
            legal_k = dp_prev & mask    # only bit values < RV[i]
            legal_rv = legal_k << rewardValues[i]   # bitshift === add
            dp[i] |= dp_prev    # don't take RV[i]: keep prior values
            dp[i] |= legal_rv   # take RV[i]: also allow this set of values
            # print(f'  {i=} rv={rewardValues[i]}')
            # # print(f'  {i=} {dp_prev =} {dp_prev:b}')
            # # print(f'  {i=} {rv_bit  =} {rv_bit:b}')
            # # print(f'  {i=} {mask    =} {mask:b}')
            # # print(f'  {i=} {legal_k =} {legal_k:b}')
            # # print(f'  {i=} {legal_rv=} {legal_rv:b}')
            # print(f'{i=} {dp[i]=}')
            # # print(f'{i=} {dp[i]=} {dp[i]:b}')

        # print(f'{dp[i]=}')
        # ValueError: Exceeds the limit (4300 digits) for integer string conversion
        # print(f'{dp[i]:b}')
        # Strangely, this succeeds, but is just an incomprehensible wall of 1's

        return dp[i].bit_length() - 1

# NOTE: Runtime 719 ms Beats 26.57%
# NOTE: Memory 358.96 MB Beats 5.59%
