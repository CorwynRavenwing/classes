class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sort_p = sorted(list(p))
        answer = []
        L = len(p)
        for i in range(len(s)):
            test = s[i:i + L]
            if len(test) < L:
                continue
            # print(f'{i}: {test=}')
            sort_test = sorted(list(test))
            if sort_test == sort_p:
                # print(f'  YES')
                answer.append(i)

        return answer

