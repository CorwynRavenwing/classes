class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort(key=lambda x: abs(x))  # sort by magnitude
        while arr:
            A = arr.pop(0)
            twiceA = 2 * A
            if twiceA in arr:
                arr.remove(twiceA)
                print(f'found {A} {twiceA}')
            else:
                print(f'error: {A} has no double')
                return False
        return True

