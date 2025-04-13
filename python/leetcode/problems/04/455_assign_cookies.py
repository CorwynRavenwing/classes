class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        answer = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            G = g[i]
            S = s[j]
            if G <= S:
                print(f'Child #{i} ({G}) gets cookie #{j} ({S})')
                answer += 1
                i += 1
                j += 1
            else:
                print(f'Nobody wants cookie #{j} ({S})')
                j += 1
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 83 ms Beats 5.11%
# NOTE: Memory 19.78 MB Beats 89.09%
