class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:

        partialSums = (0,) + tuple(accumulate(nums))
        # print(f'{partialSums=}')

        @cache
        def canSplitAtIndexes(I: int, J: index, depth=0) -> bool:
            margin = '  ' * depth
            # print(f'{margin}CSAI({I},{J})')
            if I == J:
                # print(f'{margin}  yes: single')
                return True
            if I > J:
                raise Exception(f'{margin}  ERROR!  {I=} > {J=}')
            rangeSum = partialSums[J + 1] - partialSums[I]
            if rangeSum < m:
                if depth > 0:
                    # print(f'{margin}  no: {rangeSum} < {m}')
                    return False
                # else:
                #     # print(f'{margin}  sum too small: {rangeSum} < {m}')
                #     # print(f'{margin}  (getting a pass because depth 0)')
            # print(f'{margin}  checking ...')
            answer = any([
                all([
                    canSplitAtIndexes(I, K, depth+1),
                    canSplitAtIndexes(K + 1, J, depth+1),
                ])
                for K in range(I, J)
            ])
            # if answer:
            #     # print(f'{margin}  ... yes')
            # else:
            #     # print(f'{margin}  ... no')
            return answer
        
        return canSplitAtIndexes(0, len(nums) - 1)

# NOTE: TLE on testcase 372/531
