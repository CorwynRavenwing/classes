class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        # we borrow code from #3095:
        # ... and it times out.

        # Instead, we do a perfectly normal sliding-window check:
        # ... and it times out.

        if max(nums) >= k:
            # trivial answer: OR([N]) === N >= k
            return 1
        
        def N_to_setBits(N: int) -> Set[int]:
            binary = f'{N:b}'
            binRev = tuple(reversed(binary))
            setBits = {
                index
                for index, value in enumerate(binRev)
                if value == '1'
            }
            # print(f'{N=} {binary=} {binRev=} {setBits=}')
            return setBits
        
        def setBits_to_N(setBits: Set[int]) -> int:
            answer = sum([
                2 ** B
                for B in setBits
            ])
            return answer

        bitSets = [
            N_to_setBits(N)
            for N in nums
        ]
        # print(f'{bitSets=}')
        verify = [
            setBits_to_N(SB)
            for SB in bitSets
        ]
        # print(f'{verify=}')
        assert verify == nums

        OR_everything = {B for BS in bitSets for B in BS}
        N = setBits_to_N(OR_everything)
        print(f'{OR_everything=} {N=}')
        if N < k:
            # trivial answer: OR([*]) < k means we will never find an answer
            return -1
        
        kBits = N_to_setBits(k)
        print(f'{k=} {kBits=}')

        # check = 10 ** 9
        # checkBits = N_to_setBits(check)
        # print(f'{check=} {checkBits=}')
        # binary = f'{check:b}'
        # print(f'{binary=}')

        # MAXBIT = 30           # 2^30 > 10^9 (11_1011_1001_1010_1100_1010_0000_0000)
        MAXBIT = max(kBits)
        # if anything set a higher bit, that number would be > k
        # and would therefore have tripped the "trivial return 1" section above
        bit_indexes = {}
        for bit in range(MAXBIT + 1):
            bit_indexes.setdefault(bit, [])
        for index, B in enumerate(bitSets):
            for bit in B:
                bit_indexes[bit].append(index)
        # print(f'{bit_indexes=}')
        print(f'bit_indexes:')
        for bit, indexes in bit_indexes.items():
            print(
                ' '.join([
                    f'  {bit=}:',
                    f'{indexes[:10]}',
                    ("..." if len(indexes) > 10 else ""),
                    (f'{indexes[-5:]}' if len(indexes) > 10 else ""),
                ])
            )
            
        def all_possible_bit_sets(kBits: Set[int]) -> List[List[int]]:
            # print(f'all_possible_bit_sets({kBits})')
            max_set_bit = max(kBits)
            kBitsRemain = kBits.copy()
            kBitsUsed = ()
            for bit in reversed(range(max_set_bit + 1)):
                # print(f'  {bit=}')
                if bit in kBitsRemain:
                    # print(f'    YES')
                    kBitsRemain.remove(bit)
                    kBitsUsed += (bit,)
                    # print(f'      {kBitsUsed=} {kBitsRemain=}')
                    if not kBitsRemain:
                        yield kBitsUsed
                        return
                else:
                    # print(f'    NO')
                    # print(f'      {kBitsUsed=} {bit=}')
                    # don't add this bit to kBitsUsed, just return the union
                    yield kBitsUsed + (bit,)
        
        @cache
        def shortest_ranges(bits: List[int], depth=0) -> List[Tuple[int,int]]:
            # input: list of set bits
            # output: list of ranges (low, high) containing at least one
            # of each bit
            nonlocal bit_indexes
            margin = '  ' * depth
            print(f'{margin}shortest_ranges({bits}):')
            if len(bits) == 1:
                bit = bits[0]
                indexes = bit_indexes[bit]
                answer = [
                    (I, I)
                    for I in indexes
                ]
                print(f'{margin}  {answer=}')
                return answer
            
            prior_bits = bits[:-1]
            print(f'{margin}  {prior_bits[:5]=}')
            bit = bits[-1]
            print(f'{margin}  {bit=}')
            indexes = bit_indexes[bit]
            print(f'{margin}  {indexes[:5]=}')

            if not indexes:
                # return quickly before expensive shortest_ranges() call
                return []

            prior_ranges = shortest_ranges(prior_bits, depth+1)
            print(f'{margin}  {prior_ranges[:5]=}')

            answer = []
            for (A, B) in prior_ranges:
                print(f'{margin}  {(A,B)=}')
            
                # the following is based on code from:
                # https://www.geeksforgeeks.org
                #   /python-find-closest-number-to-k-in-given-list/

                possibles = set()
                index = bisect.bisect_left(indexes, A)
                if index == 0:
                    C = indexes[0]
                    print(f'{margin}    A:0 {A=} {B=} {C=}')
                    possibles.add(
                        (
                            min(A,B,C),
                            max(A,B,C)
                        )
                    )
                elif index == len(indexes):
                    C = indexes[-1]
                    print(f'{margin}    A:MAX {A=} {B=} {C=}')
                    possibles.add(
                        (
                            min(A,B,C),
                            max(A,B,C)
                        )
                    )
                else:
                    beforeA = indexes[index-1]
                    afterA = indexes[index]
                    print(f'{margin}    A:mid {beforeA=} {A=} {afterA=} {B=}')
                    if A <= afterA <= B:
                        print(f'{margin}    A:YES {A=} {afterA=} {B=}')
                        possibles.add(
                            (A,B)
                        )

                index = bisect.bisect_left(indexes, B)
                if index == 0:
                    C = indexes[0]
                    print(f'{margin}    B:0 {A=} {B=} {C=}')
                    possibles.add(
                        (
                            min(A,B,C),
                            max(A,B,C)
                        )
                    )
                elif index == len(indexes):
                    C = indexes[-1]
                    print(f'{margin}    B:MAX {A=} {B=} {C=}')
                    possibles.add(
                        (
                            min(A,B,C),
                            max(A,B,C)
                        )
                    )
                else:
                    beforeB = indexes[index-1]
                    afterB = indexes[index]
                    print(f'{margin}    B:mid {A=} {beforeB=} {B=} {afterB=}')
                    if A <= beforeB <= B:
                        print(f'{margin}    B:YES {A=} {beforeB=} {B=}')
                        possibles.add(
                            (A, B)
                        )
                    else:
                        # we're not adding the closest, we're adding both
                        # and filtering them later
                        print(f'{margin}    AB: {beforeA=} {A=} {B=} ({afterB=})')
                        possibles.add((beforeA, B))
                        possibles.add((A, afterB))

                print(f'{margin}    {possibles=}')

                if len(possibles) == 0:
                    print(f'{margin}    (NONE) {possibles=}')
                    pass
                elif len(possibles) == 1:
                    print(f'{margin}    (only) {possibles=}')
                    answer.extend(possibles)
                else:
                    sorted_possibles = sorted([
                        (B - A, (A, B))
                        for (A, B) in possibles
                    ])
                    print(f'{margin}    {sorted_possibles=}')

                    (diff, (A, B)) = sorted_possibles[0]
                    filtered_possibles = [
                        (A, B)
                        for (D, (A, B)) in sorted_possibles
                        if D == diff
                    ]
                    print(f'{margin}    {filtered_possibles=}')
                    for (A, B) in filtered_possibles:
                        print(f'{margin}      {diff=} {(A,B)=}')
                        answer.append((A, B))

            print(f'{margin}  {answer=}')
            return answer

        ranges = []
        for bitSet in all_possible_bit_sets(kBits):
            print(f'{bitSet=}')

            newRanges = shortest_ranges(bitSet)
            print(f'{newRanges=}')
            ranges.extend(newRanges)
        
        if not ranges:
            print(f'No such special subarray found.  {ranges=}')
            return -1

        sorted_ranges = sorted([
            (B - A, (A, B))
            for (A, B) in ranges
        ])
        print(f'{sorted_ranges=}')

        (diff, (A, B)) = sorted_ranges[0]
        print(f'{diff=} {(A,B)=}')
        
        return diff + 1
        # (3, 5) -> 5-3 = 2, -> range width = 2 + 1 = 3

# NOTE: Runtime 2021 ms Beats 43.95%
# NOTE: Memory 199.00 MB Beats 5.10%
