class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        changes = [
            (
                '+' if A <= B
                else '-' if A > B
                else '?'
            )
            for (A, B) in zip(arr, arr[1:])
        ]
        # print(''.join(changes))
        (begin, end) = (1, 1)
        while changes and changes[0] == '+':
            begin += 1
            changes = changes[1:]
        left = arr[:begin]
        if changes:
            while changes and changes[-1] == '+':
                end += 1
                changes = changes[:-1]
            right = arr[-end:]
        else:
            end = 0
            right = []
        leftDisplay = (
            f'left=[{left[0]} .. {left[-1]}]'
            if len(left) > 2 else
            f'{left=}'
        )
        rightDisplay = (
            f'right=[{right[0]} .. {right[-1]}]'
            if len(right) > 2 else
            f'{right=}'
        )
        print(f'{begin=} {leftDisplay} {end=} {rightDisplay}')

        def length_merge_if_sorted(L: List[int], R: List[int]) -> int:
            # print(f'Try {L=} {R=}')
            if not L:
                # print(f'Use right only')
                return len(R)
            if not R:
                # print(f'Use left only')
                return len(L)
            if L[-1] <= R[0]:
                # print(f'Sorted: use both')
                return len(L) + len(R)
            # print(f'incompatible')
            return 0

        def elements_GE_value(value: int, R: List[int]) -> List[int]:
            if value is None:
                return R
            else:
                return [
                    x
                    for x in R
                    if x >= value
                ]

        fragments_of_left = (
            left[:i]
            for i in reversed(range(len(left) + 1))
        )
        # print(f'{fragments_of_left=}')

        min_deleted = float('+inf')

        if not right:
            return len(arr) - len(left)
        elif not left:
            return len(arr) - len(right)
        
        min_right = (right[0] if right else float('+inf'))
        max_left = (left[-1] if left else float('-inf'))
        if max_left < min_right:
            return len(arr) - (len(left) + len(right))
        
        for frag_L in fragments_of_left:
            max_possible_length = (
                len(frag_L) + len(right)
            )
            min_possible_deleted = len(arr) - max_possible_length
            if min_possible_deleted > min_deleted:
                print(f'No later (shorter) frag_left will be better')
                break
            last_val_frag_L = (frag_L[-1] if frag_L else None)
            frag_R = elements_GE_value(last_val_frag_L, right)
            length = length_merge_if_sorted(frag_L, frag_R)
            len_deleted = len(arr) - length
            min_deleted = min(min_deleted, len_deleted)

        return min_deleted

