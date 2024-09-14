class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()

        def canFitMBallsAtTargetDistance(target: int) -> bool:
            # print(f'CFMBATD({target}):')
            nonlocal position
            nonlocal m

            balls = m
            # always put first ball in first basket
            index = 0
            prior_ball = position[index]
            # print(f'  #{balls} ball in {prior_ball}')
            balls -= 1

            while balls:
                next_pos = prior_ball + target
                index = bisect_left(position, next_pos, index + 1)
                try:
                    prior_ball = position[index]
                except IndexError:
                    # print(f'  #{balls} ball: no room')
                    return False
                # print(f'  #{balls} ball in {prior_ball}')
                balls -= 1

            return True

        L = 0
        left = canFitMBallsAtTargetDistance(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = max(position) - min(position) + 1
        right = canFitMBallsAtTargetDistance(R)
        if right:
            print(f'Strange, {R=} is true')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canFitMBallsAtTargetDistance(M)
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

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 842 ms Beats 64.96%
# NOTE: Memory 30.62 MB Beats 11.13%
