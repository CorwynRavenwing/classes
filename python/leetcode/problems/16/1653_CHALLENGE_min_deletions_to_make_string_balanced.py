class Solution:
    def minimumDeletions(self, s: str) -> int:

        REV = lambda x: tuple(reversed(tuple(x)))

        ones_for_A = [1 if char == 'a' else 0 for char in s]
        ones_for_B = [1 if char == 'b' else 0 for char in s]
        # print(f'{ones_for_A=}')
        # print(f'{ones_for_B=}')
        sumAsRight = REV(accumulate(REV(ones_for_A)))
        sumBsLeft = tuple(accumulate(ones_for_B))
        # print(f'{sumAsRight=}')
        # print(f'{sumBsLeft=}')

        A_Right_Of = sumAsRight[1:] + (0,)
        B_Left_Of = (0,) + sumBsLeft[:-1]
        # print(f'{A_Right_Of=}')
        # print(f'{B_Left_Of=}')
        ToDeleteAt = tuple(map(sum, zip(A_Right_Of, B_Left_Of)))
        # print(f'{ToDeleteAt=}')

        return min(ToDeleteAt)

# NOTE: Acceptance Rate 65.7% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 683 ms Beats 14.52%
# NOTE: Memory 36.00 MB Beats 5.21%
