class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)
        countT = Counter(t)
        extraS = countS - countT
        extraT = countT - countS
        print(f'{extraS=}\n{extraT=}')

        return sum(extraT.values())

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 66 ms Beats 76.41%
# NOTE: Memory 17.16 MB Beats 36.45%
