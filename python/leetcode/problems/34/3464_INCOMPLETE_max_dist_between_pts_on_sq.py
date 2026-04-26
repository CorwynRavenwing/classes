class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        
        def get_ordered_points(side: int, points: List[List[int]]) -> List[int,List[int]]:
            points = tuple(map(tuple, points))
            # print(f'{points=}')
            IS_LEFT = lambda P: P[0] == 0
            IS_RIGHT = lambda P: P[0] == side
            IS_BOTTOM = lambda P: P[1] == 0
            IS_TOP = lambda P: P[1] == side
            MANHATTAN = lambda P: sum(P)

            manhattans = [
                (MANHATTAN(P), P)
                for P in points
            ]
            # print(f'{manhattans=}')

            ordered_points = [
                (
                    (
                        dist if IS_LEFT(P) or IS_TOP(P) else
                        (4 * side) - dist if IS_RIGHT(P) or IS_BOTTOM(P) else
                        'NOT T, B, R, or L !!!'
                    )
                )
                for (dist, P) in manhattans
            ]
            ordered_points.sort()
            return tuple(ordered_points)
        
        ordered_points = get_ordered_points(side, points)
        # print(f'I: {ordered_points=}')

        @cache
        def best_value_for_ordered_points(ordered_points: List[int]) -> int:
            pass

            def isPossible(target: int) -> bool:
                # print(f'isP({target}):')
                # can you place K points Target distance apart?
                # nonlocal ordered_points
                if target == 0:
                    return True
                local_K = k
                local_K -= 1   # point #0 can always fit
                last_val = 0
                last_index = 0
                assert ordered_points[last_index] == last_val
                while local_K:
                    next_point = last_val + target
                    next_index = bisect_left(ordered_points, next_point, last_index)
                    try:
                        next_val = ordered_points[next_index]
                    except IndexError:
                        # print(f'  NO: {local_K} {next_point=} {next_index=} OOB')
                        return False
                    # print(f'  {local_K}: {next_point=} {next_index=} {next_val=}')
                    local_K -= 1
                    last_index = next_index
                    last_val = next_val

                perimeter = 4 * side
                final_distance = perimeter - last_val
                if final_distance < target:
                    # print(f'  NO: {final_distance=} < {target}')
                    return False
                return True

            L = 0
            left = isPossible(L)
            if not left:
                # print(f'Strange, {L=} is false')
                return L
            R = 4 * side + 1
            right = isPossible(R)
            if right:
                # print(f'Strange, {R=} is true')
                return -1
            # print(f'[{L},{R}] ({left},{right})')
            while L + 1 < R:
                M = (L + R) // 2
                mid = isPossible(M)
                # print(f'[{L},{M},{R}] ({left},{mid},{right})')
                if mid:
                    # print(f'  True: replace Left')
                    (L, left) = (M, mid)
                else:
                    # print(f'  False: replace Right')
                    (R, right) = (M, mid)

            # print(f'[{L},{R}] ({left},{right})')
            # L is now the highest possible True value
            return L

        answers = []
        for _ in range(len(ordered_points)):
            first_point = ordered_points[0]
            ordered_points = ordered_points[1:] + (first_point + (4 * side),)
            min_point = ordered_points[0]
            ordered_points = tuple([
                N - min_point
                for N in ordered_points
            ])
            # print(f'{_}: {ordered_points=}')
            answers.append(
                best_value_for_ordered_points(ordered_points)
            )
        
        return max(answers)

# NOTE: Acceptance Rate 26.7% (HARD)

# NOTE: Incomplete:
#	version 1: fails for case where point (0,0) shouldn't be taken
#	version 2 (try all rotations): Time Limit Exceeded
#	version 3 (cache): Memory Exceeded
# --- above code is version 3
#	version 4 (throw out failing point (0,0)): wrong answer
