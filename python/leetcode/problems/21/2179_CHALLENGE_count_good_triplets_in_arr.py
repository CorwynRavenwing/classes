class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        # EXPLANATION 0: You are seeking triplets whose
        # members are in the same order between lists.

        # SHORTCUT 1: You can build these triplets up
        # out of *pairs*  whose members are in the same
        # order between lists.

        N = len(nums1)
        assert N == len(nums2)

        pos1 = [None] * N
        for index, value in enumerate(nums1):
            pos1[value] = index
        # print(f'{pos1=}')

        pos2a = [None] * N
        for index, value in enumerate(nums2):
            pos2a[value] = index
        # print(f'{pos2a=}')

        # map2 = {num: i for i, num in enumerate(nums2)}
        # pos2b = [map2[i] for i in range(N)]
        # print(f'{map2=}')
        # print(f'{pos2b=}')

        # assert pos2a == pos2b
        pos2 = pos2a
        print(f'{pos2=}')

        # indices[index] === num1[index]'s position in num2
        indices = [pos2[num] for num in nums1]
        print(f'{indices=}')
        
        left_counts = []
        left_sorted = []
        for idx in indices:
            index = bisect_left(left_sorted, idx)
            count = index
            print(f'Left  {idx}: {index} {count}')
            left_counts.append(count)
            left_sorted.insert(index, idx)

        right_counts = []
        right_sorted = []
        for idx in reversed(indices):
            index = bisect_left(right_sorted, idx)
            count = len(right_sorted) - index
            print(f'Right {idx} : {index} {count}')
            right_counts.append(count)
            right_sorted.insert(index, idx)
        right_counts.reverse()

        answers = [
            L * R
            for (L, R) in zip(left_counts, right_counts)
        ]
        # print(f'{answers=}')

        return sum(answers)

# NOTE: Acceptance Rate 44.1% (HARD)

# NOTE: Runtime 3850 ms Beats 5.00%
# NOTE: Memory 51.98 MB Beats 5.96%
