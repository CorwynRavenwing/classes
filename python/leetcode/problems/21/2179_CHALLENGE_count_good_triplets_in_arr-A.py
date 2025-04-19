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
        pos2 = [None] * N
        for index, value in enumerate(nums1):
            pos1[value] = index
        for index, value in enumerate(nums2):
            pos2[value] = index
        # print(f'{pos1=}')
        # print(f'{pos2=}')

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

# NOTE: correct, but Timeout Exceeded for large inputs
