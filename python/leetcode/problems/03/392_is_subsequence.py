class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        start = 0
        for s0 in s:
            # print(f"{s0=}")
            pos = t.find(s0, start)
            # print(f"  {start=} {pos=}")
            if pos == -1:
                # print(f"    FAIL {pos=}")
                return False
            start = pos + 1
        return True

