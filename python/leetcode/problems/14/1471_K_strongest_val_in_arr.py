class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        def median_ish(arr: List[int]) -> float:
            arr = sorted(arr)
            L = len(arr)
            index = (L - 1) // 2
            return arr[index]

        M = median_ish(arr)
        print(f'{M=}')

        BY_STRENGTH_DESC = lambda X: (-abs(X - M), -X)
        arr.sort(key=BY_STRENGTH_DESC)

        return arr[:k]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 319 ms Beats 10.78%
# NOTE: Memory 38.52 MB Beats 10.43%
