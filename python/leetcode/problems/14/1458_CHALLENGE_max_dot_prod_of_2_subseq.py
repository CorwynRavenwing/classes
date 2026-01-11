class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        def max_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return max(L, default=None)
        
        def dp_take_both(i: int, j: int) -> int:
            A = nums1[i]
            B = nums2[j]
            remainder = dp(i + 1, j + 1)
            # we cannot add "remainder" if it is None,
            # but we want the freedom to *not* add remainder
            # if that would make the dot-product worse:
            return (A * B) + max_not_none([remainder, 0])
        
        def dp_skip_j(i: int, j: int) -> int:
            return dp(i, j + 1)
        
        def dp_skip_i(i: int, j: int) -> int:
            return dp(i + 1, j)
        
        def dp_skip_both(i: int, j: int) -> int:
            return dp(i + 1, j + 1)
        
        @cache
        def dp(i: int, j: int) -> int:
            # print(f'dp({i},{j}):')
            try:
                A = nums1[i]
                B = nums2[j]
            except IndexError:
                # print(f'dp({i},{j}): nope')
                return None
            
            answers = [
                dp_take_both(i, j),
                dp_skip_j(i, j),
                dp_skip_i(i, j),
                dp_skip_both(i, j),
            ]
            # print(f'dp({i},{j}): {answers}')

            retval = max_not_none(answers)
            # print(f'dp({i},{j}): {retval}')
            
            return retval
        
        return dp(0,0)

# NOTE: Acceptance Rate 62.9% (HARD)

# NOTE: Accepted on third Run (edge case)
# NOTE: Accepted on third Submit (another edge case; Output Exceeded)
# NOTE: Runtime 904 ms Beats 5.03%
# NOTE: Memory 111.95 MB Beats 5.53%
