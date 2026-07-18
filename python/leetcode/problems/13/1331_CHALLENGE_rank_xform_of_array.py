class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        inRankOrder = sorted(set(arr))
        print(f'{inRankOrder=}')

        rank = {
            value: index + 1
            for (index, value) in enumerate(inRankOrder)
        }
        print(f'{rank=}')

        return [
            rank[value]
            for value in arr
        ]

# NOTE: Accepted on second Run (first was variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 255 ms Beats 28.17%
# NOTE: Memory 35.84 MB Beats 26.82%

# NOTE: Acceptance Rate 71.1% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 39 ms Beats 58.78%
# NOTE: Memory 37.59 MB Beats 60.61%
