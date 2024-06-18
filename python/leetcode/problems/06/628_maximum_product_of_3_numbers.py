class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        # print(f"{nums}")

        positives = list(sorted([
            N
            for N in nums
            if N > 0
        ]))
        zeros = list(sorted([
            N
            for N in nums
            if N == 0
        ]))
        negatives = list(sorted([
            N
            for N in nums
            if N < 0
        ]))

        # print(f"{negatives} || {zeros} || {positives}")

        N = len(negatives)
        Z = len(zeros)
        P = len(positives)
        lo_3_pos = positives[:3]
        lo_2_pos = positives[:2]
        lo_1_pos = positives[:1]
        hi_3_pos = positives[-3:]
        hi_2_pos = positives[-2:]
        hi_1_pos = positives[-1:]

        zeros_3 = zeros[:3]
        zeros_2 = zeros[:2]
        zeros_1 = zeros[:1]

        lo_3_neg = negatives[:3]
        lo_2_neg = negatives[:2]
        lo_1_neg = negatives[:1]
        hi_3_neg = negatives[-3:]
        hi_2_neg = negatives[-2:]
        hi_1_neg = negatives[-1:]

        possibles = [
            hi_3_neg,
            hi_2_neg + zeros_1,
            lo_2_neg + hi_1_pos,
            hi_1_neg + zeros_2,
            hi_1_neg + zeros_1 + hi_1_pos,
            hi_1_neg + lo_2_pos,
            zeros_3,
            zeros_2 + hi_1_pos,
            zeros_1 + hi_2_pos,
            hi_3_pos,
        ]
        # print(f"{possibles=}")
        # print("CULL len<3")
        possibles = list([
            P
            for P in possibles
            if len(P) == 3
        ])
        # print(f"{possibles=}")
        answers = list([
            A * B * C
            for (A, B, C) in possibles
        ])
        # print(f"{answers=}")
        return max(answers)

