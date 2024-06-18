class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def byArr2Order(arr1Value: str) -> Tuple[int,str]:
            return (
                (arr2.index(arr1Value) if (arr1Value in arr2) else len(arr2) + 100),
                arr1Value
            )
        return sorted(arr1, key=byArr2Order)

