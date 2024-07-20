class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:

        def removeKelements(k: int) -> List[str]:
            nonlocal s, removable
            R = removable[:k]
            return [
                char
                for index, char in enumerate(s)
                if index not in R
            ]

        def subsetOf(p: str, T: List[str]) -> bool:
            nextIndex = 0
            for ch in p:
                try:
                    nextIndex = 1 + T.index(ch, nextIndex)
                except ValueError:
                    return False
            return True

        def tryRemoval(k: int) -> bool:
            T = removeKelements(k)
            return subsetOf(p, T)
        
        L = 0
        left = tryRemoval(L)
        assert left
        R = len(removable)
        right = tryRemoval(R)
        if right:
            print(f'Found {R=}')
            return R
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = tryRemoval(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace right')
                (R, right) = (M, mid)
        print(f'[{L},{R}] ({left},{right})')
        # L is now defined as "the highest True value"
        return L
# NOTE: Time Limit Exceeded for large inputs
