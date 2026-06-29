class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        prior = 1
        for index, A in enumerate(arr):
            if A > prior:
                print(f'{index}: {A} -> {prior}')
                arr[index] = prior
            else:
                prior = A
            prior += 1
        
        return prior - 1

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 99 ms Beats 5.10%
# NOTE: Memory 27.44 MB Beats 10.90%

# NOTE: Acceptance Rate 65.9% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 99 ms Beats 7.09%
# NOTE: Memory 28.37 MB Beats 36.17%
