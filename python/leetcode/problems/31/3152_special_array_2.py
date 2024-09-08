class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        # we borrow some code from #3151
        
        # NOTE: once again, they are using "parity" to mean even-or-odd-ness

        parity = [
            N % 2
            for N in nums
        ]
        print(f'{parity=}')

        special = [
            1 if A == B else 0
            for A, B in pairwise(parity)
        ]
        special = [0] + special
        print(f'{special=}')

        bad_indexes = {
            # a set, for lookup speed
            index
            for index, value in enumerate(special)
            if value == 1
        }
        print(f'{bad_indexes=}')

        groups = tuple(accumulate(special))
        print(f'{groups=}')

        def doQuery(Q: Tuple[int,int]) -> bool:
            print(f'{Q=}')
            (fromI, toI) = Q

            if fromI == toI:
                print(f'  Yes: length 1')
                return True
            
            badTo = toI in bad_indexes
            if badTo:
                print(f'  No: bad index {toI}:{badTo}')
                return False

            fromG = groups[fromI]
            toG = groups[toI]
            print(f'  Maybe: compare groups {fromG} {toG}')
            return fromG == toG

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Runtime 1173 ms Beats 10.99%
# NOTE: Memory 56.08 MB Beats 21.98%
