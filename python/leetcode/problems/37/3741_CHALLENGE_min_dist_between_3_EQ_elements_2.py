class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        # 3-wide version of pairwise:

        def triwise(iterable):
            a, b = tee(iterable)
            a, c = tee(iterable)
            next(b, None)
            next(c, None)
            next(c, None)
            return zip(a, b, c)

        # we borrow some code from #3740:
        
        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')

        good = set()

        for (value, indexes) in indexesByValue.items():
            # NOTE: no need to check *all* non-adjacent pairs;
            # minimal triplets will be *adjacent* triplets.
            # so instead, take first and last element from each trio
            # NOTE: only record distances, not pairs
            trios = set(triwise(indexes))
            # print(f'{trios=}')
            distances = {
                2 * (C - A)
                for (A, B, C) in trios
            }
            print(f'{distances=}')
            good |= distances
        print(f'{good=}')

        return min(good, default=-1)

# NOTE: Acceptance Rate 68.5% (medium)

# NOTE: re-used most of prior version, then tightened the algorithm
# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded, Memory Exceeded)
# NOTE: Runtime 1397 ms Beats 5.34%
# NOTE: Memory 54.55 MB Beats 8.02%
