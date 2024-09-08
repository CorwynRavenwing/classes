class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        # SHORTCUT: the limit is entirely irrelevant.
        #   We don't care about balls that don't have a color.

        # taking Hint #1:
        color_of_ball = {}
        balls_of_color = {}

        def doQuery(Q: Tuple[int,int]) -> int:
            nonlocal color_of_ball
            nonlocal balls_of_color
            (ball, new_color) = Q
            # print(f'{(ball, new_color)=}')
            if ball in color_of_ball:
                old_color = color_of_ball[ball]
                # print(f'  remove {old_color=} from {ball=}')
                balls_of_color[old_color].remove(ball)
                if not balls_of_color[old_color]:
                    del balls_of_color[old_color]
                    # print(f'    No more {old_color=} balls')
            # print(f'  add {new_color=} to {ball=}')
            color_of_ball[ball] = new_color
            balls_of_color.setdefault(new_color, set())
            balls_of_color[new_color].add(ball)
            total_balls = len(color_of_ball)
            total_colors = len(balls_of_color)
            # print(f'  {total_colors=} {total_balls=}')
            return total_colors
        
        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Runtime 1217 ms Beats 22.37%
# NOTE: Memory 82.27 MB Beats 7.02%
