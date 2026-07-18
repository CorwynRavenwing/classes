class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        
        # Euclidian Algorithm for GCD, as described in Wikipedia
        def GCD(A: int, B: int) -> int:
            # print(f'GCD({A},{B})')
            if B == 0:
                return A
            else:
                return GCD(B, A % B)

        def GCD_safe(A: int, B: int) -> int:
            if A is None:
                return B
            if B is None:
                return A
            else:
                return GCD(A, B)

        def sum_not_none_mod(L: list) -> int:
            while None in L:
                L.remove(None)
            return sum(L) % mod

        # NOTE subsequence, not subarray:
        # members DO NOT need to be adjacent

        mod = 10 ** 9 + 7
        
        def DP_pick_1(i: int, GCD1: int, GCD2: int) -> int:
            # print(f'DP({i},{GCD1},{GCD2}):pick1')
            N = nums[i]
            new_GCD1 = GCD_safe(GCD1, N)
            return DP(
                i + 1,
                new_GCD1,
                GCD2
            )
        
        def DP_pick_2(i: int, GCD1: int, GCD2: int) -> int:
            # print(f'DP({i},{GCD1},{GCD2}):pick2')
            N = nums[i]
            new_GCD2 = GCD_safe(GCD2, N)
            return DP(
                i + 1,
                GCD1,
                new_GCD2
            )
        
        def DP_skip(i: int, GCD1: int, GCD2: int) -> int:
            # print(f'DP({i},{GCD1},{GCD2}):skip')
            N = nums[i]
            return DP(
                i + 1,
                GCD1,
                GCD2
            )
        
        @cache
        def DP(i: int, GCD1: int, GCD2: int) -> int:
            # print(f'DP({i},{GCD1},{GCD2})')
            try:
                _ = nums[i]
            except IndexError:
                if GCD1 is None:
                    return 0
                if GCD2 is None:
                    return 0
                if GCD1 == GCD2:
                    # print(f'    YES')
                    return 1
                else:
                    # print(f'    NO')
                    return 0
            return sum_not_none_mod([
                DP_pick_1(i, GCD1, GCD2),
                DP_pick_2(i, GCD1, GCD2),
                DP_skip(i, GCD1, GCD2),
            ])
        
        return DP(0, None, None)

# NOTE: Acceptance Rate 39.1% (HARD)

# NOTE: Accepted on second Run (edge case None=None)
# NOTE: Accepted on third Submit (Output Exceeded; Time Exceeded)
# NOTE: Runtime 7213 ms Beats 9.09%
# NOTE: Memory 600.18 MB Beats 11.36%
