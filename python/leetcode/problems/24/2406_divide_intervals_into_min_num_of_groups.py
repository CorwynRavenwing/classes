class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        overlap_dict = Counter()
        for (beginI, endI) in intervals:
            overlap_dict[beginI] += 1
            overlap_dict[endI + 1] -= 1
        # print(f'{overlap_dict=}')
        overlap_change_points = tuple(
            sorted(overlap_dict.items())
        )
        # print(f'{overlap_change_points=}')
        overlap = tuple(
            accumulate([
                count
                for changePoint, count in overlap_change_points
            ])
        )
        # print(f'{overlap=}')
        return max(overlap)

