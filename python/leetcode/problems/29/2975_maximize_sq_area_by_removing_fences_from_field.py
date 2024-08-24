class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # we borrow some code from #2943:

        def distancesBetweenNumbers(fences: List[int]) -> Set[int]:
            fences.sort()
            answer = set()
            # print(f'DBNN({fences}):')
            for i, A in enumerate(fences):
                # print(f'[{i}] {A=}')
                for B in fences[i+1:]:
                    dist = B - A
                    # print(f'  {A},{B}: {dist}')
                    answer.add(dist)
            return answer

        mod = 10 ** 9 + 7

        H = distancesBetweenNumbers(hFences + [1, m])     # horiz edge is at vertical max
        V = distancesBetweenNumbers(vFences + [1, n])     # vertical edge is at horiz max

        # print(f'{H=}\n{V=}')
        I = H.intersection(V)   # make it square
        # print(f'{I=}')
        if len(I) == 0:
            # no intersection: impossible
            return -1
        S = max(I)      # largest possible
        return (S * S) % mod
# NOTE: Runtime 1122 ms Beats 84.62%
# NOTE: Memory 51.18 MB Beats 37.06%
