class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:

        # use Radix Sort Algorithm as per suggestion in the follow-up

        nums_with_indexes = [
            (N, Nindex)
            for Nindex, N in enumerate(nums)
        ]
        # print(f'{nums_with_indexes=}')

        sort_by_trim = lambda x: x[0][1]   # Q is x[0], trim is Q[1]

        queries_sorted_by_trim = sorted(
            [
                (Q, Qindex)
                for Qindex, Q in enumerate(queries)
            ],
            key=sort_by_trim
        )
        # print(f'{queries_sorted_by_trim=}')
        answers = [None] * len(queries)

        def radix_sort_nums(radix: int) -> None:
            nonlocal nums_with_indexes
            all_digits = '0123456789'
            # print(f'Called radix_sort_nums({radix})')
            buckets = {}
            for D in all_digits:
                buckets.setdefault(D, [])
            for NWI in nums_with_indexes:
                (N, Nindex) = NWI
                digit = N[-radix]   # i.e. radix=1 -> last character, etc.
                buckets[digit].append(NWI)
                # print(f'  Bucket "{digit}" gets {NWI}')
            nums_with_indexes = [
                element
                for D in all_digits
                for element in buckets[D]
            ]
            # print(f'    new order: {nums_with_indexes=}')
            
        radix = 0
        for (Q, Qindex) in queries_sorted_by_trim:
            (kI, trimI) = Q
            print(f'Query #{Qindex}:')
            while trimI > radix:
                radix += 1
                radix_sort_nums(radix)
            if trimI == radix:
                A = nums_with_indexes[kI - 1]   # zero-basis
                (N, Nindex) = A
                print(f'  Answer: #{kI} = {N}({Nindex})')
                answers[Qindex] = Nindex

        if None in answers:
            print(f'We missed answering something!')
            print(f'{answers=}')
        return answers
# NOTE: Runtime 305 ms Beats 96.31%
# NOTE: Memory 16.94 MB Beats 29.89%
