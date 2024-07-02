class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        changes = [
            (
                '+' if B > A
                else '=' if B == A
                else '-' if B < A
                else '?'
            )
            for (A, B) in zip(arr, arr[1:])
        ]
        print(f'{changes=}')
        changeStr = ''.join(changes)
        changeStr = changeStr.replace('++', '+=+')  # we do each replacement
        changeStr = changeStr.replace('++', '+=+')  # twice because they might
        changeStr = changeStr.replace('--', '-=-')  # overlap, i.e. "+++"
        changeStr = changeStr.replace('--', '-=-')  # needs to become "+=+=+"
        print(f'{changeStr=}')
        changeGroups = changeStr.split('=')
        print(f'{changeGroups=}')
        changeLengths = tuple(map(len, changeGroups))
        print(f'{changeLengths=}')
        L = max(changeLengths) + 1
        return L

# NOTE: 340 ms; Beats 73.53%
