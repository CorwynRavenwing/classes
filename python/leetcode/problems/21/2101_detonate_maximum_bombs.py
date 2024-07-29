# NOTE: seriously, what is with the question titles today?

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        Squared = lambda x: (x * x)

        def HypotenuseSquared(p1, p2) -> int:
            (x1, y1) = p1
            (x2, y2) = p2
            return Squared(x1 - x2) + Squared(y1 - y2)

        Location = lambda x: (x[0], x[1])
        RadiusSquared = lambda x: Squared(x[2])

        adjacent = {}
        for i in range(len(bombs)):
            # print(f'{i=}')
            B1 = bombs[i]
            p1 = Location(B1)
            r1 = RadiusSquared(B1)
            adjacent.setdefault(i, [])

            for j in range(i + 1, len(bombs)):
                # print(f'  {j=}')
                B2 = bombs[j]
                p2 = Location(B2)
                r2 = RadiusSquared(B2)
                adjacent.setdefault(j, [])

                distanceSquared = HypotenuseSquared(p1, p2)
                if r1 >= distanceSquared:
                    print(f'    {i=} can reach {j=} ({r1=} >= {distanceSquared})')
                    adjacent[i].append(j)
                if r2 >= distanceSquared:
                    print(f'    {j=} can reach {i=} ({r2=} >= {distanceSquared})')
                    adjacent[j].append(i)
        # print(f'{adjacent=}')
        print(f'adjacent:')
        for i, A in adjacent.items():
            print(f'  {i}: {A}')

        @cache
        def reachableFrom(b1: int) -> Set[int]:
            # print(f'reachableFrom({b1}):')
            answer = {b1}
            check = {b1}
            while check:
                B = check.pop()
                # print(f'  {B=}')
                for b2 in adjacent[B]:
                    if b2 in answer:
                        # print(f'    {b2} seen')
                        continue
                    # print(f'    +{b2}')
                    answer.add(b2)
                    check.add(b2)
            # print(f'rf({b1}) = {answer}')
            return answer

        reachables = [
            reachableFrom(i)
            for i in range(len(bombs))
        ]
        # print(f'{reachables=}')
        print(f'reachables:')
        for i, R in enumerate(reachables):
            print(f'  {i=} {R}')
        answers = [
            len(R)
            for R in reachables
        ]
        print(f'{answers=}')

        return max(answers)
# NOTE: Runtime 494 ms Beats 43.73%
# NOTE: Memory 17.96 MB Beats 8.31%
