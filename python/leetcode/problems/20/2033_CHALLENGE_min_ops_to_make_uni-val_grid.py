class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        def median_ish(arr: List[int]) -> float:
            arr = sorted(arr)
            L = len(arr)
            index = (L - 1) // 2
            return arr[index]
        
        flattened = [
            value
            for row in grid
            for value in row
        ]
        flattened.sort()

        modulos = {
            value % x
            for value in flattened
        }
        if len(modulos) > 1:
            print(f'NO: {modulos=}')
            return -1

        median_value = median_ish(flattened)
        print(f'{flattened=}')
        print(f'{median_value=}')

        operations = [
            abs(value - median_value) // x
            for value in flattened
        ]
        print(f'{operations=}')

        return sum(operations)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 243 ms Beats 18.52%
# NOTE: Memory 40.85 MB Beats 5.56%

# NOTE: re-ran for challenge:
# NOTE: Runtime 219 ms Beats 26.32%
# NOTE: Memory 41.09 MB Beats 12.72%
# NOTE: same numbers, better percentages
