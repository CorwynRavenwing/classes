class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        steps = 0
        water = capacity
        print(f'We start with {water} in the can')
        print()

        for pos in range(len(plants)):
            need = plants[pos]
            if need > water:
                water = capacity
                refill_steps = (2 * pos)
                print(f'We fill the can ({refill_steps} steps) and now have {water}')
                steps += refill_steps
            water -= need
            steps += 1
            print(f'We water #{pos} ({need}) (1 step) and now have {water}')

        return steps
# NOTE: Runtime 51 ms Beats 41.30%
# NOTE: Memory 16.64 MB Beats 53.50%
