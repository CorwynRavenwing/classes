class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        @cache
        def checkFragSet(frag: Set[int]) -> int:
            diffs = {
                B - A
                for (A, B) in zip(frag, frag[1:])
            }
            # zeros will not appear, because of set(frag) above
            print(f'  {frag=} {diffs=}')
            if not diffs:
                return -1
            else:
                return min(diffs)
        
        # @cache
        def checkFragList(frag: List[int]) -> int:
            frag = tuple(sorted(set(frag)))
            return checkFragSet(frag)

        # @cache
        def answerQuery(Q: Tuple[int]) -> int:
            nonlocal nums
            (L, R) = Q
            frag = tuple(nums[L:R + 1])
            print(f'{Q=}:')
            # print(f'{Q=} {frag=}')
            return checkFragList(frag)
        
        return [
            answerQuery(tuple(Q))
            for Q in queries
        ]
# Either OLE, TLE, or MLE, dealer's choice, for large inputs
