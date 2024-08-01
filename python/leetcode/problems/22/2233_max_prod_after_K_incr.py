class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:

        mod = 10 ** 9 + 7

        numCounts = Counter(nums)
        nums_with_counts = [
            (N, count)
            for N, count in numCounts.items()
        ]
        nums_with_counts.sort()
        # print(f'start {nums_with_counts[:2]=}')

        while k > 0:
            print(f'{k}: DEBUG {nums_with_counts[:2]=}')
            first = nums_with_counts.pop(0)     # take the lowest
            (N1, N1count) = first
            print(f'{k}: {first}')
            if nums_with_counts:
                second = nums_with_counts.pop(0)    # .. and second-lowest
                (N2, N2count) = second
                print(f'  compare {second=}')
                required = (N2 - N1) * N1count      # to raise block 1 to block 2's value
                if required <= k:
                    print(f'  {required=} <= {k}')
                    # we have enough to do this
                    first = (N2, N1count + N2count)
                    # second has disappeared
                    print(f'    {N1} -> {N2} * {N1count}')
                    k -= required
                    bisect.insort(nums_with_counts, first)
                else:
                    print(f'  {required=} > {k}')
                    # we do not have enough.  Undo pop of "second":
                    bisect.insort(nums_with_counts, second)

                    # NOTE: we may be able to fall through here,
                    # because this section and the section after
                    # "else not nums_with_counts" are identical

                    # instead, upgrade N1 as much as possible
                    change = k // N1count
                    print(f'    {k} / {N1count} = {change}')
                    if change:
                        print(f'    Enough to upgrade entire group several times')
                        # we can upgrade that number 'change' times
                        first = (N1 + change, N1count)
                        k -= N1count * change
                        print(f'    {N1} -> {N1 + change} * {N1count}')
                        bisect.insort(nums_with_counts, first)
                    else:
                        print(f'    Not enough to do that.  Splitting.')
                        # not enough to change all of this block.  Split it.
                        first = (N1 + 1, k)         # increment K of them by 1
                        second = (N1, N1count - k)  # keep the others at the old value
                        print(f'    {N1} -> {N1 + change} * {k}')
                        k -= k
                        bisect.insort(nums_with_counts, first)
                        bisect.insort(nums_with_counts, second)
                    # endif change
                # endif required < k
            else:
                # else not nums_with_counts
                # there is only one number in the list
                change = k // N1count
                print(f'    {k} / {N1count} = {change}')
                if change:
                    print(f'    Enough to upgrade entire group several times')
                    # we can upgrade that number 'change' times
                    first = (N1 + change, N1count)
                    k -= N1count * change
                    print(f'    {N1} -> {N1 + change} * {N1count}')
                    bisect.insort(nums_with_counts, first)
                else:
                    print(f'    Not enough to do that.  Splitting.')
                    # not enough to change all of this block.  Split it.
                    first = (N1 + 1, k)         # increment K of them by 1
                    second = (N1, N1count - k)  # keep the others at the old value
                    print(f'    {N1} -> {N1 + change} * {k}')
                    k -= k
                    bisect.insort(nums_with_counts, first)
                    bisect.insort(nums_with_counts, second)
                # endif change

            # print(f'{k}: {N1} -> {new_N}')
        print(f'end: {nums_with_counts[:2]=}')

        nums_pow_counts = [
            N ** count
            for N, count in nums_with_counts
        ]
        # print(f'{nums_pow_counts[:5]=}')
        answer = math.prod(nums_pow_counts)

        return answer % mod

