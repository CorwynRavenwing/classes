class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        nums_str = ''.join(map(str, nums))
        print(f'{nums_str=}')
        groups = nums_str.split('1')
        print(f'{groups=}')
        if not len(groups):
            return True
        del groups[0]
        if not len(groups):
            return True
        del groups[-1]
        if not len(groups):
            return True
        lengths = tuple(map(len, groups))
        print(f'{lengths=}')
        distance = min(lengths)

        return (distance >= k)

# NOTE: Acceptance Rate 64.3% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (edge case; different edge case)
# NOTE: Runtime 55 ms Beats 5.14%
# NOTE: Memory 28.30 MB Beats 5.68%
