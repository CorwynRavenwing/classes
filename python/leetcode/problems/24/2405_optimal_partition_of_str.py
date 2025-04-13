class Solution:
    def partitionString(self, s: str) -> int:
        
        if not s:
            return 0
        
        answer = 1
        seen = set()
        for char in s:
            if char in seen:
                print(f'partition #{answer} = {seen}')
                answer += 1
                seen = {char}
            else:
                seen.add(char)
        print(f'partition #{answer} = {seen}')
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 240 ms Beats 5.03%
# NOTE: Memory 18.01 MB Beats 57.75%
