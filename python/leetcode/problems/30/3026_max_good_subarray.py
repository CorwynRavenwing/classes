class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = (0,) + tuple(accumulate(nums))
        # print(f'{prefixSum=}')

        answers = []
        leftEndMin = {}
        zipEverything = zip(
            nums,
            prefixSum,      # sum to the left of "i"
            prefixSum[1:],  # sum including "i"
        )
        for (numsI, sumWithout, T) in zipEverything:
            # print(f'{numsI=} {sumWithout=} {T=}')
            
            # First, check for existing answer left of here:
            for numsJ in [numsI + k, numsI - k]:
                try:
                    P = leftEndMin[numsJ]
                except KeyError:
                    # print(f'  {numsJ=} ---')
                    continue
                # print(f'  {numsJ=} {P=}')
                answers.append(T - P)

            # Second, add this value to the "leftEnd" dict
            if numsI not in leftEndMin:
                leftEndMin[numsI] = sumWithout
            elif leftEndMin[numsI] > sumWithout:
                leftEndMin[numsI] = sumWithout
            # else don't update

        # print(f'{answers=}')

        return max(answers, default=0)

# NOTE: Accepted on first Submit
# NOTE: Runtime 993 ms Beats 24.50%
# NOTE: Memory 30.65 MB Beats 35.10%
