class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        candies.sort(reverse=True)

        def CanAllocateTargetCandiesToKChildren(target: int) -> bool:
            children = 0
            for C in candies:
                if C < target:
                    # throw out all the other piles, and fail
                    return False
                children += C // target
                if children >= k:
                    # we have served all available children: succeed
                    return True
            # we got to the end of the candy piles: fail
            return False

        # try 1 candy
        L = 1
        left = CanAllocateTargetCandiesToKChildren(L)
        if not left:
            print(f'{L=} is false: not even 1 candy for each child')
            return 0

        # try dividing candy by children
        R = sum(candies) // k + 1
        right = CanAllocateTargetCandiesToKChildren(R)
        if right:
            print(f'Strange, {R=} is true')
            return -1

        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = CanAllocateTargetCandiesToKChildren(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace Right')
                (R, right) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # L is now the highest possible True value
        return L

# NOTE: Accepted on second Run (variable rename)
# NOTE: Accepted on first Submit
# NOTE: Runtime 279 ms Beats 80.17%
# NOTE: Memory 29.78 MB Beats 54.49%

# NOTE: re-ran for challenge:
# NOTE: Runtime 267 ms Beats 81.80%
# NOTE: Memory 29.91 MB Beats 9.02%
