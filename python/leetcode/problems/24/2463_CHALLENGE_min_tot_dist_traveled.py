class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        # print(f'{robot=}')
        factory.sort()
        maxN = len(robot)
        factory_multiple = [
            X
            for X, N in factory
            for i in range(min(N, maxN))
        ]
        # print(f'{factory_multiple=}')

        cached_DP = [
            [None] * len(factory_multiple)
            for _ in range(len(robot))
        ]
        # print(f'{cached_DP=}')

        # @cache
        # roll your own cache: built-in method causes Memory Exceeded
        def DP(RobotIndex: int, FactoryIndex: int) -> int:
            # print(f'DP({RobotIndex},{FactoryIndex})')

            # MAXINT = 10 ** 9 + 1
            # no.  Maximum possible answer is:
            # ((max location) - (min location)) * (max robots)
            # = ((1e9) - (-1e9)) * 100
            # = 2 * 1e9 * 100
            # = 2e11
            MAXINT = 10 ** 12

            if RobotIndex < 0:
                # no robots: no moves
                return 0

            if FactoryIndex < 0:
                # no factories: impossible
                return MAXINT
            
            answer = cached_DP[RobotIndex][FactoryIndex]
            if answer is not None:
                return answer

            # if RobotIndex > FactoryIndex:
            #     # not enough Factories: impossible
            #     return MAXINT

            # if RobotIndex == FactoryIndex:
            #     answer = sum([
            #         abs(Robots[RobotIndex] - factory_multiple[FactoryIndex]),
            #         DP(RobotIndex - 1, FactoryIndex - 1),
            #     ])
            #     return answer

            answer_without_last_factory = DP(RobotIndex, FactoryIndex - 1)
            answer_without_last_robot_or_factory = DP(RobotIndex - 1, FactoryIndex - 1)
            link_last_robot_to_last_factory = abs(
                robot[RobotIndex] - factory_multiple[FactoryIndex]
            )

            answer = min([
                answer_without_last_factory,
                sum([
                    answer_without_last_robot_or_factory,
                    link_last_robot_to_last_factory,
                ]),
            ])
            cached_DP[RobotIndex][FactoryIndex] = answer
            return answer

        return DP(len(robot) - 1, len(factory_multiple) - 1)

# NOTE: Acceptance Rate 56.8% (HARD)
# NOTE: was the challenge 2024-10-31: did not complete it in time
# NOTE: Runtime 2704 ms Beats 8.00%
# NOTE: Memory 60.39 MB Beats 27.89%
