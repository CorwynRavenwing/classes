class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        L = len(code)

        if k == 0:
            return [0] * L
        
        if k > 0:
            return [
                sum([
                    code[j % L]
                    for j in range(i + 1, i + 1 + k)
                ])
                for i in range(L)
            ]
        
        if k < 0:
            REV = lambda X: tuple(reversed(tuple(X)))
            return REV(self.decrypt(REV(code), -k))

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 38.94%
# NOTE: Memory 16.67 MB Beats 62.03%
