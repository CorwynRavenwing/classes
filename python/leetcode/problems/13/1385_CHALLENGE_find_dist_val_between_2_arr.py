class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:

        arr2.append(float("-inf"))
        arr2.append(float("inf"))
        arr2.sort()
        print(f'{arr2=}')

        def min_distance(N: int) -> int:
            index = bisect.bisect_left(arr2, N)
            hit = arr2[index]
            if hit == N:
                # print(f'{N=} {index=} {hit=}')
                return 0
            frag = arr2[index-1:index+2]
            diffs = [
                abs(X - N)
                for X in frag
            ]
            # print(f'{N=} {index=} {frag=} {diffs=}')
            return min(diffs)

        distances = [
            min_distance(N)
            for N in arr1
        ]
        print(f'{distances=}')

        successes = [
            (
                1
                if D > d
                else 0
            )
            for D in distances            
        ]
        print(f'{successes=}')

        return sum(successes)

# NOTE: Acceptance Rate 72.6% (easy)

# NOTE: Accepted on third Run (typo, reverse polarity)
# NOTE: Accepted on first Submit
# NOTE: Runtime 10 ms Beats 72.81%
# NOTE: Memory 19.44 MB Beats 8.88%
