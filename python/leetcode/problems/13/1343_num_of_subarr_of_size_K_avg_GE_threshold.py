class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        limitK = k * threshold   # multiply, don't divide
        I = 0
        J = I + k
        Total = sum(arr[I:J])
        answer = 0
        while 0 <= I < J <= len(arr):
            if Total >= limitK:
                answer += 1
                print(f'Y {answer}: [{I}:{J}] ({arr[I]}..{arr[J-1]}) {Total}/{limitK}')
            else:
                print(f'N {answer}: [{I}:{J}] ({arr[I]}..{arr[J-1]}) {Total}/{limitK}')
            Total -= arr[I]
            try:
                Total += arr[J]
            except IndexError:
                # ran off end of array
                break
            I += 1
            J += 1
        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 327 ms Beats 5.01%
# NOTE: Memory 27.22 MB Beats 68.02%
