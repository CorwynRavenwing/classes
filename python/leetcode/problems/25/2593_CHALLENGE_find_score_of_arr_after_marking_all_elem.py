class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        indexesByValue = {}
        for index, value in enumerate(nums):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        print(f'{indexesByValue=}')

        total = 0
        marked = set()
        for value, indexes in sorted(indexesByValue.items()):
            for i in indexes:
                if i in marked:
                    # print(f'[{i}]{value} marked')
                    continue
                total += value
                # print(f'[{i}]{value} found: {total=}')
                for j in [i - 1, i, i + 1]:
                    marked.add(j)

        return total

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 543 ms Beats 53.46%
# NOTE: Memory 59.17 MB Beats 5.47%
