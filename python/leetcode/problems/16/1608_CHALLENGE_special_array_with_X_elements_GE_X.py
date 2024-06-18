class Solution:
    def specialArray(self, nums: List[int]) -> int:

        def count_nums_GE(X: int) -> int:
            # GE === "greater than or equal to"
            nums_GE_X = [
                N
                for N in nums
                if N >= X
            ]
            answer = len(nums_GE_X)
            print(f'count({X}) == {answer}')
            return answer

        L = 0
        R = len(nums)
        print(f'[{L},{R}]')
        if L == count_nums_GE(L):
            return L
        if R == count_nums_GE(R):
            return R
        while L + 1 < R:
            M = (L + R) // 2
            print(f'[{L},{M},{R}]')
            C = count_nums_GE(M)
            if C == M:
                return M
            if C > M:
                print(f'  remove L')
                L = M
                continue
            if C < M:
                print(f'  remove R')
                R = M
                continue
            raise Exception(f'cannot compare {C} <=> {M}')
        print(f'[{L},{R}]')

        return -1

