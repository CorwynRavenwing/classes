class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        assert len(s) == len(t)
        # Z = zip(s, t)
        D = [
            abs(ord(A) - ord(B))
            for (A, B) in zip(s, t)
        ]
        # print(f'{D=}')
        answer = 0
        i = 0
        j = i
        L = 1
        S = D[i]
        while i < len(D):
            print(f'{i=} {j=} {L=} {S=} {answer=}')
            if S <= maxCost:
                answer = max(answer, L)
                # slide right end of window up
                j += 1
                if j >= len(D):
                    break
                L += 1
                S += D[j]
            else:
                # slide left end of window up
                L -= 1
                S -= D[i]
                i += 1

        return answer

