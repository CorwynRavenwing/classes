class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        # SHORTCUT 1: we're going to just zero out the values in nums
        # when we mark them, rather than keeping a separate "marked" list.
        # UPDATE: we're timing out, so I'm going to reverse this decision,
        # and see how much faster it is.  We're also precomputing sum(nums).
        # Test Case 653:
        # 4449ms    use the shortcut method, compute sum(nums) inside loop
        #  250ms    still using the shortcut, pre-compute NumSum
        # 4204ms    using marked = set(), compute sum(nums) inside loop
        #  193ms    using marked = set(), pre-compute NumSum
        # clearly, the set helps a little, but the sum() was the true problem

        # SHORTCUT 2: we will produce a list of (number, index) pairs,
        # which we will then sort by value for Step Two.
        
        marked = set()
        NumSum = sum(nums)
        value_index_queue = sorted([
            (value, index)
            for (index, value) in enumerate(nums)
        ])
        # print(f'{value_index_queue=}')
        VIQ = 0

        def doQuery(Q: List[int]) -> int:
            nonlocal value_index_queue
            nonlocal VIQ
            nonlocal nums
            nonlocal NumSum
            # print(f'DEBUG: {nums=}')
            indexI, kI = Q
            # step one:
            # if nums[indexI] == 0:
            if indexI in marked:
                print(f'Step 1: skip {indexI}')
            else:
                print(f'Step 1: MARK {indexI}')
                NumSum -= nums[indexI]
            nums[indexI] = 0
            marked.add(indexI)
            # step two:
            while kI:
                if VIQ >= len(value_index_queue):
                    # print(f'     2: skip marking {kI}: done')
                    break
                (value, index) = value_index_queue[VIQ]
                VIQ += 1
                # print(f'  :{index=} {value=} {nums[index]=}')
                # if nums[index] == 0:
                if index in marked:
                    print(f'     2: skip {index}')
                    continue
                else:
                    print(f'     2: MARK {index}, #{kI}')
                    kI -= 1
                    NumSum -= nums[index]
                    nums[index] = 0
                    marked.add(index)

            # return sum(nums)  # this is extremely slow!
            return NumSum       # pre-compute for speed

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Runtime 1496 ms Beats 20.37%
# NOTE: Memory 50.56 MB Beats 29.63%
