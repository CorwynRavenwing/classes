class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        highest_L_jumps = []
        sum_of_other_jumps = 0
        building_number = 0
        for (A, B) in pairwise(heights):
            diff = B - A
            # print(f'{building_number}: {diff=}')
            if diff > 0:
                bisect.insort(highest_L_jumps, diff)
                if len(highest_L_jumps) > ladders:
                    lowest = highest_L_jumps.pop(0)
                    sum_of_other_jumps += lowest
                # print(f'  B={sum_of_other_jumps}/{bricks} L={len(highest_L_jumps)}/{ladders}')
                if sum_of_other_jumps > bricks:
                    # print(f'    (not enough bricks)')
                    return building_number
            building_number += 1
        
        # reached the last building
        return building_number

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 623 ms Beats 5.04%
# NOTE: Memory 27.54 MB Beats 93.10%
