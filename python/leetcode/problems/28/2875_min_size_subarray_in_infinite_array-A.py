class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

        REV = lambda x: tuple(reversed(tuple(x)))
        SUM = lambda x: (0,) + tuple(accumulate(tuple(x)))

        prefix_sum = SUM(nums)
        suffix_sum = REV(SUM(REV(nums)))
        # print(f'{prefix_sum=}')
        # print(f'{suffix_sum=}')

        ArraySum = prefix_sum[-1]
        answers = []
        if target <= ArraySum:
            print(f'Subarray')
            for i in range(len(nums) + 1):
                for j in range(i + 1, len(nums) + 1):
                    Sum = prefix_sum[j] - prefix_sum[i]
                    # print(f'[{i}..{j}] {Sum}')
                    if Sum == target:
                        print(f'  Found at [{i}:{j}]')
                        answers.append(j - i)
        # else:
        # no, ALWAYS do this, because "k" can be zero
        print(f'Multiple')
        # here, i can't be len(nums) and j can't be 0,
        # but they CAN overlap
        for i in range(len(nums)):
            for j in range(1, len(nums) + 1):
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

        if not answers:
            print(f'  Not found')
            return -1

        print(f'{answers=}')
        return min(answers)
# NOTE: works for reasonable inputs, Time Limit Exceeded for big inputs
