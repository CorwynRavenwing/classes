class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = list(zip(positions, directions, healths, range(len(positions))))
        robots.sort()
        round = 0
        while True:
            round += 1
            print(f'{round=} {len(robots)=}')
            survivor_stack = []
            collisions = 0
            # the stack contains everything except A and B
            A = None
            # print(f'{A=} from start')
            for B in robots:
                # print(f'\t{B=} stack')
                while B:
                    if A is None:
                        if survivor_stack:
                            # get a new A off the stack
                            A = survivor_stack.pop()
                            # print(f'{A=} survivors')
                        else:
                            A = B       # use this as A
                            B = None
                            # print(f'{A=} {B=} swap')
                            continue    # get a new B
                    (A_pos, A_dir, A_health, A_id) = A
                    (B_pos, B_dir, B_health, B_id) = B
                    dir_pair = f'{A_dir}{B_dir}'
                    if dir_pair != 'RL':
                        # they can't collide
                        survivor_stack.append(A)
                        A = B
                        B = None
                        continue    # new B
                    # collide them:
                    collisions += 1
                    if A_health < B_health:
                        # print(f'  {A_health} <- {B_health}')
                        A = None
                        B = (B_pos, B_dir, B_health - 1, B_id)
                    elif A_health > B_health:
                        # print(f'  {A_health} -> {B_health}')
                        A = (A_pos, A_dir, A_health - 1, A_id)
                        B = None
                    elif A_health == B_health:
                        # print(f'  {A_health} XX {B_health}')
                        A = None
                        B = None
                    # print(f'{A=} {B=} collision')
                    continue
                # wend B
            # endfor B
            if collisions:
                print(f'Total {collisions=}')
                if A:
                    survivor_stack.append(A)
                if B:
                    survivor_stack.append(B)
                robots = survivor_stack
                survivor_stack = []
                # while None in robots:
                #     robots.remove(None)
            else:
                print(f'No collisions')
                break
        # wend True

        robots.sort(
            key=lambda x: x[3]  # sort by ID field
        )
        # print(f'ID sort: {robots=}')
        healths = [
            health
            for (pos, dir, health, id) in robots
        ]
        return healths

