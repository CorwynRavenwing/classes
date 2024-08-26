class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        
        counts = Counter(nums)
        Min = min(counts)
        print(f'{Min=} {counts=}')

        minCount = counts[Min]
        if minCount == 1:
            print(f'  Minimum occurs once')
            return 1

        for Other in counts:
            New = Other % Min
            if New != 0:
                print(f'  {Other} % {Min} = {New}')
                return 1
        
        return (minCount // 2) + (minCount % 2)     # === ceil(minCount / 2)

# NOTE: Accepted on first Run; Accepted on first Submit
# NOTE: Runtime 663 ms Beats 7.09%
# NOTE: Memory 45.86 MB Beats 8.66%
