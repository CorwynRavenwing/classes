class Solution:
    def minCost(self, nums: List[int], x: int) -> int:

        # O(N^2), but N < 1000, therefore this will be fast enough
        possible_costs_per_chocolate_by_rotation = [
            [
                nums[
                    (chocolate - rotations) % len(nums)
                ]
                for rotations in range(len(nums))
            ]
            for chocolate in range(len(nums))
        ]
        # print(f'Possible costs per chocolate, by rotation:')
        # for chocolate, PCPC in enumerate(possible_costs_per_chocolate_by_rotation):
        #     # print(f'  C={chocolate}: costs={PCPC}')

        min_cost_per_chocolate_by_rotation = [
            tuple(accumulate(cost_list, min))
            for cost_list in possible_costs_per_chocolate_by_rotation
        ]
        # print(f'Min costs per chocolate, by rotation:')
        # for chocolate, MCPC in enumerate(min_cost_per_chocolate_by_rotation):
        #     # print(f'  C={chocolate}: costs={MCPC}')

        min_cost_per_rotation_by_chocolate = (
            tuple(zip(*min_cost_per_chocolate_by_rotation))
        )
        # print(f'Min costs per rotation, by chocolate:')
        # for rotations, MCPR in enumerate(min_cost_per_rotation_by_chocolate):
        #     # print(f'  R={rotations}: costs={MCPR}')
        
        total_costs_by_rotation = [
            (x * rotations) + sum(MCPR)
            for rotations, MCPR in enumerate(min_cost_per_rotation_by_chocolate)
        ]
        # print(f'Total costs, by rotation:')
        # for rotations, TCBR in enumerate(total_costs_by_rotation):
        #     # print(f'  R={rotations}: costs={TCBR}')
        
        return min(total_costs_by_rotation)
# NOTE: Runtime 3314 ms Beats 5.48%
# NOTE: Memory 42.74 MB Beats 9.59%
