from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # faster version (47 ms)
        cS = Counter(s)
        cT = Counter(t)
        # print(f"{cS=} {cT=}")
        # print(f"{cS.items()=} {cT.items()=}")
        return sorted(cS.items()) == sorted(cT.items())

        # original version (60ms)
        return sorted(s) == sorted(t)

