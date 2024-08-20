class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

        REV = lambda x: tuple(reversed(tuple(x)))
        SUM = lambda x: (0,) + tuple(accumulate(tuple(x)))

        prefix_sum = SUM(nums)
        rev_suffix = SUM(REV(nums))
        suffix_sum = REV(rev_suffix)
        # print(f'{prefix_sum=}')
        # print(f'{rev_suffix=}')
        # print(f'{suffix_sum=}')

        ArraySum = prefix_sum[-1]
        answers = []
        if target <= ArraySum:
            print(f'Subarray')
            for i in range(len(nums) + 1):
                PrefixJ = prefix_sum[i] + target
                j = bisect_left(prefix_sum, PrefixJ)
                if j >= len(prefix_sum):
                    # print(f'[{i}] {prefix_sum[i]} ({PrefixJ}) -> [{j}] (OOB) not found')
                    continue
                if (prefix_sum[j] != PrefixJ):
                    # print(f'[{i}] {prefix_sum[i]} ({PrefixJ}) -> [{j}] {prefix_sum[j]} not found')
                    continue

                Sum = prefix_sum[j] - prefix_sum[i]
                # print(f'[{i}..{j}] {Sum}')
                if Sum == target:
                    print(f'  Found at [{i}:{j}]')
                    answers.append(j - i)
                else:
                    print(f'  ERROR: {Sum=} did not add up here')
                    return -555

        # no, ALWAYS do this, because "k" can be zero
        print(f'Multiple')
        # here, i can't be len(nums) and j can't be 0,
        # but they CAN overlap
        for i in range(len(nums)):
            targetK0 = target % ArraySum
            targetK1 = targetK0 + ArraySum
            # print(f'{i}: seek {targetK0},{targetK1}')
            for targetKn in [targetK0, targetK1]:
                SuffixJ = targetKn - prefix_sum[i]
                # print(f'  Checking {SuffixJ} = {targetKn} - {prefix_sum[i]}')
                j_reversed = bisect_left(rev_suffix, SuffixJ)
                j = len(suffix_sum) - j_reversed - 1
                if j >= len(suffix_sum):
                    # print(f'[{i}] {prefix_sum[i]} ({SuffixJ}) -> [{j}] (OOB) not found')
                    continue
                if (suffix_sum[j] != SuffixJ):
                    # print(f'[{i}] {prefix_sum[i]} ({SuffixJ}) -> [{j}] {suffix_sum[j]} not found')
                    continue
                # print(f'  {j_reversed=} -> {j=}')
                Sum = prefix_sum[i] + suffix_sum[j]
                # print(f'[..{i}]+[{j}..] {Sum}')
                if (target - Sum) % ArraySum == 0:
                    k = (target - Sum) // ArraySum
                    checkSum = prefix_sum[i] + (k * ArraySum) + suffix_sum[j]
                    if checkSum != target:
                        print(f'  FAIL: checksum does not match!')
                        print(f'{k} = ({target} - {Sum}) // {ArraySum}')
                        print(f'{checkSum} = {prefix_sum[i]} + ({k} * {ArraySum}) + {suffix_sum[j]}')
                        return -777
                    print(f'  Found at [0..{i}] + [{j}..{len(nums)}] + {k} * array')
                    # print(f'  DEBUG {nums[:i]} + {nums[j:]} + {k} * {ArraySum}')
                    # print(f'  DEBUG {sum(nums[:i])} + {sum(nums[j:])} + {k * ArraySum}')
                    count = i + (k * len(nums)) + (len(nums) - j)
                    print(f'    {count=} {i} + {len(nums) - j} + {k} * {len(nums)}')
                    answers.append(count)
                else:
                    print(f'  ERROR: {Sum=} did not add up here')
                    return -444

        if not answers:
            print(f'  Not found')
            return -1

        print(f'{answers=}')
        return min(answers)
# NOTE: Runtime 693 ms Beats 7.30%
# NOTE: Memory 34.47 MB Beats 46.63%
