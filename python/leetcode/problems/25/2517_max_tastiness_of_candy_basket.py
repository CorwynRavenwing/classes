class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        # we borrow some code from #1552:

        price.sort()

        def canGetKCandiesAtTargetDistance(target: int) -> bool:
            # print(f'CFMBATD({target}):')
            nonlocal price
            nonlocal k

            candies = k
            # always put first candy in first basket
            index = 0
            prior_candy = price[index]
            # print(f'  #{candies} candy in {prior_candy}')
            candies -= 1

            while candies:
                next_pos = prior_candy + target
                index = bisect_left(price, next_pos, index + 1)
                try:
                    prior_candy = price[index]
                except IndexError:
                    # print(f'  #{candies} candy: no room')
                    return False
                # print(f'  #{candies} candy in {prior_candy}')
                candies -= 1

            return True

        L = 0
        left = canGetKCandiesAtTargetDistance(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = max(price) - min(price) + 1
        right = canGetKCandiesAtTargetDistance(R)
        if right:
            print(f'Strange, {R=} is true')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canGetKCandiesAtTargetDistance(M)
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

# NOTE: Used all of prior version's code, with variable renames
# NOTE: Accepted on third Run (variable name typos)
# NOTE: Accepted on first Submit
# NOTE: Runtime 1042 ms Beats 5.17%
# NOTE: Memory 30.40 MB Beats 6.34%
