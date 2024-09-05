class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        # # we borrow code from #3095:
        # # ... and it times out.
        # print(f'{nums=}')
        # for length_try in range(1, len(nums)+1):
        #     # print(f'trying length {length_try}')
        #     for index in range(0, len(nums)-length_try+1):
        #         array = nums[index:index+length_try]
        #         # print(f'  {array=}')
        #         bitwise_or = array[0]
        #         for element in array[1:]:
        #             bitwise_or |= element
        #         # print(f'    {bitwise_or}')
        #         if bitwise_or >= k:
        #             # print(f'      >= {k}')
        #             return length_try
        # return -1

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

        first_window = Counter()
        for window_size in range(1, len(nums) + 1):
            print(f'{window_size=}')
            i = 0
            j = i + window_size - 1
            first_window.update(bitSets[j]) # new FW is old FW plus J
            # window = bitSets[i:j+1]
            # assert len(window) == window_size
            if window_size == 1:
                # because we've already tried "1" in trivial section above
                continue
            setBitsCount = first_window.copy()
            print(f'{setBitsCount=}')
            while j < len(bitSets):
                union = set(setBitsCount.keys())
                N = setBits_to_N(union)
                # print(f'WS={window_size} {i=} {j=} L={len(bitSets)} {union=} {N=}')
                # print(f'WS={window_size} {i=} {j=} L={len(bitSets)} {N=}')
                if N >= k:
                    window = bitSets[i:j+1]
                    print(f'WS={window_size} {i=} {j=} {window=}')
                    print(f'{setBitsCount=}')
                    print(f'{union=}')
                    return window_size
                try:
                    setBitsCount.subtract(bitSets[i])
                    i += 1  # increment AFTER using
                    j += 1  # increment BEFORE using
                    setBitsCount.update(bitSets[j])
                    setBitsCount = +setBitsCount    # no zero values
                except IndexError:
                    # print(f'Fell out of window: {i=} {j=} {len(bitSets)=}')
                    break
                
        return -1
# NOTE: times out for extremely large inputs (#715)
