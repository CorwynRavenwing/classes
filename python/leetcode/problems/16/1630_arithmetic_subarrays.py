class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def doQuery(Q: List[int]) -> bool:
            print(f'{Q=}')
            (L, R) = Q
            frag = nums[L:R + 1]
            print(f'  {frag=}')
            if len(frag) <= 1:
                print(f'  NO: too short to be arithmetic')
                return False

            counts = Counter(frag)
            print(f'  {counts=}')
            if len(counts) == 1:
                print(f'  YES: diff == 0')
                return True
            if len(counts) != len(frag):
                print(f'  NO: dups')
                return False
            
            arith_diff = None
            for (A, B) in pairwise(sorted(counts.keys())):
                diff = (B - A)
                print(f'  {(A,B)=} {diff=}')
                if arith_diff is None:
                    arith_diff = diff
                if arith_diff != diff:
                    print(f'  NO: diff')
                    return False

            print(f'  YES')
            return True

        queries = tuple(zip(l, r))  # why the non-traditional format?

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 392 ms Beats 5.02%
# NOTE: Memory 17.25 MB Beats 5.95%
