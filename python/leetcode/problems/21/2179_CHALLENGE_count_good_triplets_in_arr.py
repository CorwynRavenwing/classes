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
        # TODO: use a normal List and sort it ourselves
        left_sorted = SortedList()
        for idx in indices:
            left_counts.append(left_sorted.bisect_left(idx))
            left_sorted.add(idx)

        right_counts = []
        right_sorted = SortedList()
        for idx in reversed(indices):
            right_counts.append(len(right_sorted) - right_sorted.bisect_right(idx))
            right_sorted.add(idx)
        right_counts.reverse() 
        
        return sum(left * right for left, right in zip(left_counts, right_counts))



        #####



        left = [0] * N
        right = [0] * N

        for i in range(N):
            for j in range(N):
                # print(f'[{i}:{j}]:')
                if i == j:
                    continue
                if pos1[i] < pos1[j] and pos2[i] < pos2[j]:
                    # print(f'  YES {pos1[i]} < {pos1[j]} and {pos2[i]} < {pos2[j]}')
                    right[i] += 1
                    left[j] += 1
                # else:
                #     # print(f'  NO! {pos1[i]} > {pos1[j]}, or {pos2[i]} > {pos2[j]}')
        # print(f'{left =}')
        # print(f'{right=}')

        answers = [
            A * B
            for (A, B) in zip(left, right)
        ]
        # print(f'{answers=}')

        return sum(answers)

# NOTE: Acceptance Rate 44.1% (HARD)

# NOTE: Needed a hint that actually hinted at the solution :-(
# NOTE: Accepted on first Submit
# NOTE: Runtime 771 ms Beats 73.83%
# NOTE: Memory 47.94 MB Beats 32.71%

# NOTE: TODO clean this up a bit

