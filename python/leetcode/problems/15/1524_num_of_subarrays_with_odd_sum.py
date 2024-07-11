class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        mod = 10 ** 9 + 7
        answer = 0

        leftSum = [None] * len(arr)
        for i, A in enumerate(arr):
            if i == 0:
                leftSum[i] = A
            else:
                leftSum[i] = A + leftSum[i - 1]
        print(f'{leftSum=}')
        (countEven, countOdd) = (0, 0)
        for L in leftSum:
            if L % 2 == 0:
                countEven += 1
                # even
                answer += countOdd      # any prior subarray starting on an Odd
            else:
                countOdd += 1
                # odd
                answer += 1             # the number itself
                answer += countEven     # any prior subarray starting on an Even

        return answer % mod

