class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        print(f'{arr=}')
        new_array = [
            (x,) if x else (0, 0)
            for x in arr
        ]
        print(f'{new_array=}')
        new_array = [
            x
            for T in new_array
            for x in T
        ]
        print(f'{new_array=}')
        new_array = new_array[:len(arr)]
        print(f'{new_array=}')
        for i in range(len(arr)):
            arr[i] = new_array[i]
        """
        Do not return anything, modify arr in-place instead.
        """

