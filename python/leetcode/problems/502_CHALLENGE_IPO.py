class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = list(zip(capital, profits))
        projects.sort(
            # sort by capital ASC, then profits DESC
            key=lambda x: (x[0], -x[1])
        )

        start = 0
        everything = []
        for i in range(k):
            print(f'[{i+1}/{k}] {w=} L(P)={len(projects)}')
            if everything:
                P = everything.pop()
                print(f'    => {P}')
                (cap, prof) = P
                # if cap > w:
                #     print(f'    Nothing to do! Min {cap=} {w=}')
                #     return w
                w += prof
                print(f'    Made {prof} profit')
                continue

            Pmax = bisect.bisect_left(projects, (w, 0), start)
            Pgroup = projects[:Pmax + 1]
            print(f'  #{Pmax}: ...{Pgroup[-3:]}')
            while Pgroup and Pgroup[-1][0] > w:
                print(f'    Delete P={Pgroup[-1]}')
                Pmax -= 1
                Pgroup = projects[:Pmax + 1]
            P = max(
                Pgroup,
                default=None,
                key=lambda x: x[1]  # maximize profit
            )
            start = Pmax
            print(f'    -> {P}')
            if P is None:
                print(f'Nothing to do! {P=} {w=}')
                return w
            projects.remove(P)
            (cap, prof) = P
            if cap > w:
                print(f'    Nothing to do! Min {cap=} {w=}')
                return w
            w += prof
            print(f'    Made {prof} profit')
            if Pmax >= len(projects) > 0:
                print(f'All projects are now possible!')
                everything = sorted(
                    projects,
                    key=lambda x: x[1]  # maximize profit
                )
                continue

        return w

