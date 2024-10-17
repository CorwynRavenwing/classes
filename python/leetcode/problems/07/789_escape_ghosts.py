class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        # I could have created a set of "coordinates that the ghotst
        # might possibly have reached by now", which gets larger each
        # turn along its outer perimeter ...
        # but then I realized that the ghosts' optimal strategy is to run
        # straight for the target and ambush you there.
        def manhattan_distance(p1: Tuple[int,int], p2: Tuple[int,int]) -> int:
            (x1, y1) = p1
            (x2, y2) = p2
            return abs(x1 - x2) + abs(y1 - y2)
        
        distance_from_target = lambda pos: manhattan_distance(pos, target)
        
        player_distance = distance_from_target((0,0))
        ghost_distances = tuple(map(distance_from_target, ghosts))
        print(f'{player_distance=} {ghost_distances=}')

        return player_distance < min(ghost_distances)

# NOTE: Accepted on first Submit
# NOTE: Runtime 37 ms Beats 98.69%
# NOTE: Memory 16.77 MB Beats 11.55%
