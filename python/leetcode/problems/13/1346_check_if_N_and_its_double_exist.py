class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        arrMax = arr[-1]
        if 0 in arr:
            arr.remove(0)
            if 0 in arr:
                # two different zeros exist
                return True
        for E in arr:
            if not E:
                continue
            twoE = 2 * E
            if twoE > arrMax:
                return False
            if twoE in arr:
                return True
        return False

