class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        ROCK = float('+inf')

        def jumps_with_rocks(obstacle: int, jumps: List[int]) -> List[int]:
            answer = jumps[:]   # copy
            if obstacle:
                lane_id = obstacle - 1      # 1-index vs 0-index
                answer[lane_id] = ROCK
            return answer

        old_jumps = [ROCK, 0, ROCK]             # start in lane 2
        # print(f'-: [-] {old_jumps}')
        for position, obstacle in enumerate(obstacles):
            new_jumps = jumps_with_rocks(obstacle, old_jumps)
            for lane_id, jumps in enumerate(new_jumps):
                lane = lane_id + 1              # 1-index vs 0-index
                new_jumps[lane_id] = min([
                    jumps,                      # stay in current lane
                    min(new_jumps) + 1,         # jump to this lane from best prior
                ])
            old_jumps = jumps_with_rocks(obstacle, new_jumps)
            # print(f'{position}: [{obstacle}] {old_jumps}')

        print(f'{position}: [{obstacle}] {old_jumps}')
        return min(old_jumps)

# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 1962 ms Beats 23.73%
# NOTE: Memory 39.36 MB Beats 49.66%
