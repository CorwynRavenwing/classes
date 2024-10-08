class Solution:
    def countSubstrings(self, s: str) -> int:

        DEBUG = False

        answer = 0
        endpoints = []

        # group A: every character is a length-1 palindrome
        endpoints.extend([
            (i, i)
            for i in range(len(s))
        ])
        # group B: any duplicated character is a length-2 palindrome
        endpoints.extend([
            (i, j)
            for ((i, A), (j, B)) in pairwise(enumerate(s))
            if A == B
        ])
        # print(f'{endpoints=}')
        answer += len(endpoints)
        while endpoints:
            new_endpoints = []
            for (i, j) in endpoints:
                i -= 1
                j += 1
                if DEBUG: print(f'try ({i},{j}):')
                if i < 0:
                    if DEBUG: print(f'  I too low')
                    continue
                if j >= len(s):
                    if DEBUG: print(f'  J too high')
                    continue
                A = s[i]
                B = s[j]
                if A != B:
                    if DEBUG: print(f'  "{A}/{B}"')
                    continue
                if DEBUG: print(f'  YES')
                new_endpoints.append(
                    (i, j)
                )
            endpoints = new_endpoints
            answer += len(endpoints)
        
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 222 ms Beats 33.69%
# NOTE: Memory 17.06 MB Beats 26.50%
