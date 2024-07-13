class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = list(zip(positions, directions, healths, range(len(positions))))
        robots.sort()
        round = 0
        while True:
            round += 1
            # print(f'{round=} {robots=}')
            Dirs = ''.join([
                dir
                for (pos, dir, health, id) in robots
            ])
            print(f'{round=} {Dirs[:25]=}')
            # collisions are only possible between pairs of adjacent robots,
            # the first one going Right and the second going Left.
            # any further collisions involving these robots will only happen
            # after this collision is played out
            if 'RL' not in Dirs:
                print(f'No further collisions possible')
                break
            while 'RL' in Dirs:
                index = Dirs.index('RL')
                (A, B) = robots[index:index + 2]  # A = robot at 'index'; B = robot at 'index + 1'
                (A_pos, A_dir, A_health, A_id) = A
                (B_pos, B_dir, B_health, B_id) = B
                if A_health < B_health:
                    print(f'  {A_health} <- {B_health}')
                    A = None
                    B = (B_pos, B_dir, B_health - 1, B_id)
                elif A_health > B_health:
                    print(f'  {A_health} -> {B_health}')
                    A = (A_pos, A_dir, A_health - 1, A_id)
                    B = None
                elif A_health == B_health:
                    print(f'  {A_health} XX {B_health}')
                    A = None
                    B = None
                robots[index:index + 2] = (A, B)
                Dirs = Dirs.replace('RL', 'XX', 1)     # or we could recalculate?
            # print(f'cleanup {robots=}')
            while None in robots:
                robots.remove(None)
        robots.sort(
            key=lambda x: x[3]  # sort by ID field
        )
        # print(f'ID sort: {robots=}')
        healths = [
            health
            for (pos, dir, health, id) in robots
        ]
        return healths
# NOTE: works, but Time Limit Exceeded for large inputs
