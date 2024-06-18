# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        LB = 0
        UB = n
        print(f"{LB} - {UB}")

        while LB + 1 < UB:
            MID = (LB + UB) // 2
            print(f"{LB} {MID} {UB}")
            if isBadVersion(MID):
                UB = MID
            else:
                LB = MID
        
        print(f"{LB} - {UB}")
        return UB

