class Solution:
    def numSplits(self, s: str) -> int:
        # start with the dividing line entirely on the left of everything
        Left = Counter()
        Right = Counter(s)

        # # invalid test case: no need to check for this
        # if len(Left) == len(Right):
        #     assert s == ""
        #     return 1
        
        answer = 0
        for char in s:
            # move this one character from Right into Left:
            Left[char] += 1
            Right[char] -= 1
            if not Right[char]:
                del Right[char]
            if len(Left) == len(Right):
                answer += 1
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 107 ms Beats 30.89%
# NOTE: Memory 16.95 MB Beats 74.15%
