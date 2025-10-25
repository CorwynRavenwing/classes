class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
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

# NOTE: Acceptance Rate 22.2% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge case; Output Exceeded)
# NOTE: Runtime 686 ms Beats 43.60%
# NOTE: Memory 46.14 MB Beats 9.88%
