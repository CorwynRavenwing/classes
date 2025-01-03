class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sums = [None] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]

        mods = [
            (
                S % k
                if k
                else S
            )
            for S in sums
        ]
        sums.insert(0, 0)   # sum of zero elements is 0
        mods.insert(0, 0)   # mod of zero is 0
        # print(f'{sums=}')
        # print(f'{mods=}')
        mod_counts = Counter(mods)
        multiples = [
            number
            for number, count in mod_counts.items()
            if count > 1
        ]
        # print(f'{multiples=}')
        answer = 0
        for M in multiples:
            indexes = [
                index
                for index, mod in enumerate(mods)
                if mod == M
            ]
            # print(f'{M}: {indexes}')
            if k == 0:
                # we need to count pairs of indexes
                # i.e. N pick 2
                # == (N!)/(N-2)!(2!)
                # == (N)(N-1)/2
                N = len(indexes)
                print(f'  add ({N} pick {2})')
                answer += N * (N - 1) // 2
            else:
                for i, index1 in enumerate(indexes):
                    for j, index2 in enumerate(indexes):
                        if i >= j:
                            # print(f'  {i=} {j=} skip')
                            continue
                        value = sums[index2] - sums[index1]
                        if value == k:
                            # print(f'  {i=} {j=} {index1}..{index2} {value=} YES')
                            answer += 1
                        # else:
                        #     print(f'  {i=} {j=} {index1}..{index2} {value=} no')
        
        return answer

# NOTE: Runtime 9461 ms Beats 5.27%
# NOTE: Memory 19.77 MB Beats 18.21%
