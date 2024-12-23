class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        @cache
        def first_index_GE_index_GT_value(min_index: int, min_value: int) -> int:
            # nonlocal heights      # read-only
            if min_index >= len(heights):
                return -1

            C = heights[min_index]
            if C > min_value:
                return min_index
            
            return first_index_GE_index_GT_value(min_index + 1, min_value)

        # def first_index_GE_index_GT_value(min_index: int, min_value: int) -> int:
        #     # nonlocal heights      # read-only
        #     for indexC in range(min_index, len(heights)):
        #         C = heights[indexC]
        #         if C > min_value:
        #             return indexC
        #     return -1

        def doQuery(Q: List[int]) -> int:
            print(f'{Q=}')
            # WLOG sort the indexes
            (indexA, indexB) = sorted(Q)

            if indexA == indexB:
                # print(f'  EQUAL')
                return indexA
            
            A = heights[indexA]
            B = heights[indexB]

            if A < B:
                # print(f'  JUMP TO B')
                return indexB
            
            min_index = indexB + 1
            min_C = max(A, B)

            return first_index_GE_index_GT_value(min_index, min_C)

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 40.6% (HARD)
# NOTE: Runtime 740 ms Beats 33.33%
# NOTE: Memory 82.98 MB Beats 5.21%
# NOTE: re-ran for challenge, and received:
# NOTE: Runtime 700 ms Beats 38.54%
# NOTE: Memory 82.89 MB Beats 5.21%
