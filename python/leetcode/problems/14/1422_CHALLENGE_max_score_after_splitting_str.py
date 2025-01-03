class Solution:
    def maxScore(self, s: str) -> int:
        
        prefixSum = list(accumulate(map(int, tuple(s))))
        print(f'{prefixSum=}')

        totalOnes = prefixSum.pop(-1)   # shorten Ones list:
        # this makes the zip() shorter, which prevents
        # getting an answer for a zero-length right half
        zeros = 0
        answer = 0
        for (bit, onesSum) in zip(s, prefixSum):
            if bit == '0':
                zeros += 1
            ones = totalOnes - onesSum
            answer = max(answer, ones + zeros)
            print(f'{bit=} {onesSum=} {zeros=} {ones=} {answer=}')

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case for zero-length Ones)
# NOTE: Runtime 7 ms Beats 19.21%
# NOTE: Memory 18.04 MB Beats 9.48%
