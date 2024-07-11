class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        # we borrow some code from #560:

        sums = [None] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]

        mods = [
            (
                S % target
                if target
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
        pairs = []
        for M in multiples:
            indexes = [
                index
                for index, mod in enumerate(mods)
                if mod == M
            ]
            print(f'{M}: {indexes}')
            for i, index1 in enumerate(indexes):
                for j, index2 in enumerate(indexes):
                    if i >= j:
                        continue
                    value = sums[index2] - sums[index1]
                    if value == target:
                        print(f'  {i=} {j=} {index1}..{index2} {value=} YES')
                        pairs.append((index1, index2 - 1))
                        # we want non-overlapping ranges
                        # therefore take only the first pair found
                        break
        pairs.sort()
        # print(f'{pairs=}')
        # greedy algorithm doesn't work here
        answers = [(0, -1)]     # no subarrays, maxUsed -1
        for P in pairs:
            print(f'{P=}')
            (A, B) = P
            newCounts = set()
            for (oldCount, maxUsed) in answers:
                if maxUsed < A <= B:
                    newCounts.add(oldCount + 1)
                else:
                    break
            newAnswer = (
                max(newCounts),
                B,
            )
            print(f'  A={newAnswer}')
            # should instead insert with bisection -- insort?
            answers.append(newAnswer)
            answers.sort(
                key=lambda x: x[1]  # sort by maxUsed ASC
            )
        print(f'{answers=}')
        (answer, maxUsed) = max(answers)
        return answer

# NOTE: giving Time Limit Exceeded error for huge inputs
