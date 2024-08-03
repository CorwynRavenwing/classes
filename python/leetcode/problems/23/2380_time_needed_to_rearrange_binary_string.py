class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        answer = 0
        print(f'{answer}: {s=}')
        while '01' in s:
            s = s.replace('01', '10')   # all of them at once
            answer += 1
            print(f'{answer}: {s=}')

        return answer
# NOTE: this gives Output Limit Exceeded with the print statements
# NOTE: Runtime 102 ms Beats 58.75%
# NOTE: O(N)
# NOTE: Memory 16.42 MB Beats 87.50%
# NOTE: O(1)
