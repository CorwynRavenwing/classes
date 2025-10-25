class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
        # We borrow some code from #3346:
        
        nums.sort()
        # print(f'{nums=}')
        count = Counter(nums)
        nums_sorted = tuple(sorted(count.keys()))
        # print(f'{nums_sorted=}')
        for (A, B) in pairwise(nums_sorted):
            diff = B - A
            if diff <= 1:
                # print(f'({A},{B}) < 1')
                continue
            if diff > 2 * k:
                # print(f'({A},{B}) > 2*{k}')
                continue
            C = (A + B) // 2
            # print(f'({A},{B}) -> {C}')
            count[C] += 0
        print()
        for A in nums_sorted:
            C = A + k
            # print(f'{A} -> {C}')
            count[C] += 0
        print()

        nums_freq = tuple(sorted(count.items()))
        answers = []
        for (N, freq) in nums_freq:
            A = N - k
            B = N + k
            # print(f'{N=} -> {A}:{B}')
            i = bisect_left(nums, A)
            j = bisect_right(nums, B)
            answer = min(j - i, freq + numOperations)
            # print(f'  [{i}]:[{j}] {j - i}:{freq + numOperations} = {answer}')
            answers.append(answer)

        # print(f'{answers=}')
        return max(answers)

# NOTE: Acceptance Rate 38.9% (HARD)

# NOTE: Used exactly the prior version's code
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1119 ms Beats 54.84%
# NOTE: Memory 79.06 MB Beats 6.45%
