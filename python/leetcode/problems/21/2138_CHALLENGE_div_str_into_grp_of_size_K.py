class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        answer = []
        while s:
            A = s[:k]
            s = s[k:]
            if len(A) < k:
                A += (fill * (k - len(A)))
            assert len(A) == k
            answer.append(A)
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case with unexpected length)
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.84 MB Beats 36.31%
