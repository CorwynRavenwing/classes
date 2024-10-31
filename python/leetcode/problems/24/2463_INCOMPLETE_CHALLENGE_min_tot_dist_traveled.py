class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        print(f'{robot=}')
        factory.sort()
        maxN = len(robot)
        factory_multiple = [
            X
            for X, N in factory
            for i in range(min(N, maxN))
        ]
        print(f'{factory_multiple=}')

        @cache
        def DP(Robots: List[int], Factories: List[int]) -> int:
            MAXINT = 10 ** 9 + 1
            ELIPSIS = lambda X: (
                f'{X}({len(X)})'
                if (len(X) <= 2)
                else f'[{X[0]}..{X[-1]}]({len(X)})'
                )

            print(f'DP({ELIPSIS(Robots)},{ELIPSIS(Factories)})')
            if len(Robots) > len(Factories):
                # not enough Factories: impossible
                return MAXINT
            if (not Robots):
                # no Robots: no moves
                return 0
            if len(Robots) == len(Factories):
                answer = sum([
                    abs(Robots[-1] - Factories[-1]),
                    DP(Robots[:-1], Factories[:-1]),
                ])
                # print(f'  EQUAL {answer}')
                return answer
            max_skip = min(len(Robots), len(Factories))
            all_possible_groups = [
                (
                    (Robots[:index], Robots[index:]),
                    # use all Robots, but skip Factories[index]
                    (Factories[:index], Factories[index + 1:]),
                )
                for index in range(max_skip)
            ]
            all_possible_skips = [
                (
                    DP(rA, fA),
                    DP(rB, fB),
                )
                for ((rA, rB), (fA, fB)) in all_possible_groups
            ]
            print(f'DP({ELIPSIS(Robots)},{ELIPSIS(Factories)})')
            print(f'  {max_skip=}')
            print(f'  {all_possible_groups=}')
            # print(f'  {tuple(range(max_skip))=}')
            print(f'  {all_possible_skips=}')
            all_sums = tuple(map(sum, all_possible_skips))
            print(f'  {all_sums=}')
            answer = min(all_sums)
            # print(f'  SKIP: {answer}')
            return answer

        return DP(tuple(robot), tuple(factory_multiple))

# NOTE: Acceptance Rate 56.8% (HARD)
# NOTE: Time Limit Exceeded for large values, plus some wrong answers
