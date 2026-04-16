class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        # circularize array:
        orig_len = len(nums)
        nums = nums + nums

        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')

        distances = [
            []
            for _ in range(orig_len)
        ]
        # print(f'{distances=}')
        for value, indexes in indexesByValue.items():
            # print(f'  {value}: {indexes}')
            for (C, D) in pairwise(indexes):
                diff = D - C
                (A, B) = (C, D)
                if A >= orig_len:
                    A -= orig_len
                if B >= orig_len:
                    B -= orig_len
                # print(f'    {(C,D)} -> {(A,B)}: {diff}')
                distances[A].append(diff)
                distances[B].append(diff)
        # print(f'{distances=}')
        distances = [
            min(distList, default=None)
            for distList in distances
        ]
        # print(f'{distances=}')
        distances = [
            (
                -1 if dist == orig_len
                else dist
            )
            for dist in distances
        ]
        # print(f'{distances=}')

        # NOTE: yes, we just precomputed all the possible answers;
        #   and yes, it was easier than doing it for each query

        def doQuery(Q: List[int]) -> int:
            # print(f'{Q=}')
            return distances[Q]

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 35.1% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded)
# NOTE: Runtime 579 ms Beats 13.28%
# NOTE: Memory 71.17 MB Beats 5.47%
