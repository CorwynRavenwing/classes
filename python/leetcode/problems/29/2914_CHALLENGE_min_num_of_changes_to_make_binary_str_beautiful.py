class Solution:
    def minChanges(self, s: str) -> int:

        answer = 0
        prior = None
        for C in s:
            print(f'{prior}:{C}')
            if prior is None:
                print(f'  skip')
                prior = C
                continue
            
            if prior != C:
                print(f'  DIFF')
                answer += 1

            prior = None
            
        return answer

# NOTE: Runtime 324 ms Beats 5.29%
# NOTE: Memory 17.35 MB Beats 25.29%

# NOTE: re-ran later for challenge:
# NOTE: Runtime 302 ms Beats 5.40%
# NOTE: Memory 17.17 MB Beats 67.89%
# NOTE: ... slightly better memory; greatly better percentage!
