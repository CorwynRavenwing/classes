class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        NOT_FOUND = letters[0]
        L = 0
        R = len(letters) - 1
        left = letters[L]
        right = letters[R]
        if target < left:
            return left
        if target > right:
            return NOT_FOUND
        while L + 1 < R:
            M = (L + R) // 2
            mid = letters[M]
            print(f'[{L},{M},{R}] = ({left},{mid},{right})')
            
            # if target == mid:
            #     return M
            if target < mid:
                (R, right) = (M, mid)
                continue
            if target >= mid:
                (L, left) = (M, mid)
        print(f'after loop: [{L},{R}] = ({left},{right}) {target=}')
        if target == right:
            return NOT_FOUND
        if left == target:
            return right
        if left < target < right:
            return right
        return NOT_FOUND

