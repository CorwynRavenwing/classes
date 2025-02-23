class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        OTHER = lambda x: ('1' if x == '0' else '0')
        answer = []
        for i, N in enumerate(nums):
            Ni = N[i]
            A = OTHER(Ni)
            print(f'"{N}"[{i}]: {Ni=} -> {A=}')
            answer.append(A)
        return ''.join(answer)

# NOTE: Accepted on second Run (logic reversal)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.66 MB Beats 78.38%

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.74 MB Beats 69.31%
