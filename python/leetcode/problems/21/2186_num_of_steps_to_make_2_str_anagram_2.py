class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        countS = Counter(s)
        countT = Counter(t)
        # print(f'{countS=}')
        # print(f'{countT=}')
        SminusT = countS - countT
        TminusS = countT - countS
        # print(f'{SminusT=}')
        # print(f'{TminusS=}')
        Total = SminusT + TminusS
        print(f'{Total=}')
        answer = sum(Total.values())
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 148 ms Beats 72.35%
# NOTE: Memory 19.52 MB Beats 6.47%
